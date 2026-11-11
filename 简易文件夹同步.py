# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from pathlib import Path
import hashlib
import shutil
import sys
import os
import msvcrt

# 把可以更改的设置都放在这里
CONFIG = {
    # 每组把 fromLocation 中的文件同步到 toLocation
    "syncFolders": [
        {
            "fromLocation": r'D:\资料',
            "toLocation": r'E:\备份\资料',
        },
        # 可以继续添加同步组
        # {
        #     "fromLocation": r'D:\资料',
        #     "toLocation": r'E:\备份\资料',
        # },
    ],
    "makeChoice"   : True,  # 是否在复制前让用户确认
    "deleteFiles"  : False, # 是否删除目标文件夹中源文件夹没有的文件
}


def get_sha1(file_path):
    digest = hashlib.sha1()
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def doSyncFile(source_location, target_location):
    source_dir = Path(source_location).resolve()
    target_dir = Path(target_location).resolve()

    if not source_dir.is_dir():
        raise ValueError(f"源文件夹不存在或不是文件夹: {source_dir}")
    if target_dir.exists() and not target_dir.is_dir():
        raise ValueError(f"目标路径不是文件夹: {target_dir}")
    if source_dir == target_dir:
        raise ValueError("源文件夹和目标文件夹不能相同。")
    try:
        target_dir.relative_to(source_dir)
    except ValueError:
        pass
    else:
        raise ValueError("目标文件夹不能位于源文件夹内部。")

    files_to_copy = []
    source_relative_paths = set()
    same_count = 0
    for source_file in source_dir.rglob("*"):
        if not source_file.is_file():
            continue

        relative_path = source_file.relative_to(source_dir)
        source_relative_paths.add(relative_path)
        target_file = target_dir / relative_path
        source_sha1 = get_sha1(source_file)
        if target_file.exists() and not target_file.is_file():
            raise ValueError(f"目标路径已存在但不是文件: {target_file}")
        if target_file.is_file():
            if get_sha1(target_file) == source_sha1:
                same_count += 1
                continue
            reason = "SHA1不同"
        else:
            reason = "目标文件不存在"
        files_to_copy.append((source_file, target_file, relative_path, source_sha1, reason))

    files_to_delete = []
    if CONFIG["deleteFiles"] and target_dir.is_dir():
        files_to_delete = [
            target_file
            for target_file in target_dir.rglob("*")
            if target_file.is_file()
            and target_file.relative_to(target_dir) not in source_relative_paths
        ]

    print(f"SHA1相同，跳过: {same_count} 个文件")
    if not files_to_copy and not files_to_delete:
        print("没有需要复制或删除的文件。")
        return

    if files_to_copy:
        print(f"\n以下 {len(files_to_copy)} 个文件需要复制:")
        for _, _, relative_path, _, reason in files_to_copy:
            print(f"  [{reason}] {relative_path}")

    if files_to_delete:
        print(f"\n以下 {len(files_to_delete)} 个目标文件在源文件夹中不存在，将被删除:")
        for target_file in files_to_delete:
            print(f"  {target_file.relative_to(target_dir)}")

    if CONFIG["makeChoice"] and files_to_copy:
        actions = "复制和删除" if files_to_delete else "复制"
        answer = input(f"\n是否执行上述{actions}操作？(y/N): ").strip().lower()
        if answer != "y":
            print("已取消操作。")
            return

    for source_file, target_file, relative_path, expected_sha1, _ in files_to_copy:
        if get_sha1(source_file) != expected_sha1:
            raise RuntimeError(f"源文件在确认后发生变化，已停止复制: {relative_path}")
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target_file)
        if get_sha1(target_file) != expected_sha1:
            raise OSError(f"复制后 SHA1 校验失败: {relative_path}")
        print(f"已复制: {relative_path}")

    deleted_count = 0
    if files_to_delete:
        if not (CONFIG["makeChoice"] and files_to_copy):
            answer = input("\n是否删除以上目标文件？(y/N): ").strip().lower()
            if answer != "y":
                print("已取消删除。")
                files_to_delete = []
        for target_file in files_to_delete:
            target_file.unlink()
            print(f"已删除: {target_file.relative_to(target_dir)}")
            deleted_count += 1

    print(f"\n操作完成，复制 {len(files_to_copy)} 个文件，删除 {deleted_count} 个文件。")


def main():
    try:
        sync_folders = CONFIG["syncFolders"]
        if not sync_folders:
            raise ValueError("请至少配置一组同步文件夹。")

        for index, folder_pair in enumerate(sync_folders, start=1):
            print(f"\n=== 同步组 {index}/{len(sync_folders)} ===")
            doSyncFile(folder_pair["fromLocation"], folder_pair["toLocation"])

        print("\n所有同步组处理完成。")
        print("按任意键退出程序，按y键打开目标文件夹: ", end="", flush=True)
        if msvcrt.getch().decode().lower() == "y":
            if len(sync_folders) == 1:
                os.startfile(sync_folders[0]["toLocation"])
            else:
                for index, folder_pair in enumerate(sync_folders, start=1):
                    print(f"{index}: {folder_pair['toLocation']}")
                selection = input("请输入要打开的目标文件夹编号: ").strip()
                if selection.isdigit() and 1 <= int(selection) <= len(sync_folders):
                    os.startfile(sync_folders[int(selection) - 1]["toLocation"])
                else:
                    print("未打开目标文件夹。")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"同步失败: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()