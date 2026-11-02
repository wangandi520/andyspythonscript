# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from ftplib import FTP, error_perm
from pathlib import Path
import fnmatch
import posixpath

# 适用于有tf卡2的安伯尼克H700掌机，要打开wifi，在rg34xx上测试通过，其他未测试
# FTP连接设置，注意可能只有在保持亮屏状态下才能下载成功
# 只需要修改host和local_path
CONFIG = {
    'host': '192.168.1.100',  # 远程主机IP，修改成你的机器ip
    'port': 21,               # FTP端口，默认21
    'username': 'admin',   # 用户名
    'password': 'admin',   # 密码
    'remote_paths': [
        '/android/roms/save' # 多个文件夹的话，在本行结尾添加逗号，下一行添加新的路径，结尾无逗号。
    ],
    'local_path': r'.'  # 本地保存路径，和py同目录的话，填英文句号.
}


def download_files_via_ftp(pattern: str = '*') -> None:
    """
    使用FTP连接远程服务器并下载文件到本地

    Args:
        pattern: 文件匹配模式，默认下载所有文件
    """
    host = CONFIG.get('host')
    port = CONFIG.get('port', 21)
    username = CONFIG.get('username')
    password = CONFIG.get('password')
    remote_paths = CONFIG.get('remote_paths', [])
    local_path = CONFIG.get('local_path')

    if not all([host, username, password, remote_paths, local_path]):
        print('FTP配置不完整，请检查CONFIG中的设置')
        return

    local_dir = Path(local_path)
    local_dir.mkdir(parents=True, exist_ok=True)

    ftp = FTP()
    try:
        print(f'正在连接到 {host}:{port}...')
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)

        def is_zip_file(remote_path):
            return posixpath.splitext(remote_path)[1].lower() == '.zip'

        def is_directory(remote_path):
            if is_zip_file(remote_path):
                return False

            current_dir = ftp.pwd()
            try:
                ftp.cwd(remote_path)
                return True
            except error_perm:
                return False
            finally:
                ftp.cwd(current_dir)

        def download_file(remote_file_path, local_file_path):
            print(f'正在下载: {remote_file_path}')
            with open(local_file_path, 'wb') as output_file:
                ftp.retrbinary(
                    f'RETR {remote_file_path}',
                    output_file.write
                )
            print(f'已下载到: {local_file_path}')

        def download_dir(remote_dir, local_dir_path):
            local_dir_obj = Path(local_dir_path)
            local_dir_obj.mkdir(parents=True, exist_ok=True)

            print(f'进入远程目录: {remote_dir}')

            try:
                items = ftp.nlst(remote_dir)
                for item in items:
                    filename = posixpath.basename(item.rstrip('/'))
                    if filename in ('', '.', '..'):
                        continue

                    remote_file_path = posixpath.join(remote_dir, filename)
                    local_file_path = local_dir_obj / filename

                    if is_directory(remote_file_path):
                        print(f'发现子目录: {filename}')
                        download_dir(remote_file_path, local_file_path)
                    elif fnmatch.fnmatch(filename, pattern):
                        download_file(remote_file_path, local_file_path)
            except Exception as e:
                print(f'处理目录 {remote_dir} 时出错: {str(e)}')

        for remote_path in remote_paths:
            print(f'\n开始处理远程路径: {remote_path}')
            path_name = posixpath.basename(remote_path.rstrip('/'))
            current_local_path = local_dir / path_name

            try:
                if is_directory(remote_path):
                    print(f'开始下载目录: {remote_path}')
                    download_dir(remote_path, current_local_path)
                    print(f'目录 {remote_path} 下载完成')
                else:
                    filename = posixpath.basename(remote_path.rstrip('/'))
                    local_file = local_dir / filename
                    print(f'正在下载单个文件: {filename}')
                    download_file(remote_path, local_file)
            except Exception as e:
                print(f'远程路径不存在或无法访问: {remote_path}')
                print(f'错误: {str(e)}')

    except Exception as e:
        print(f'FTP操作失败: {str(e)}')
        return
    finally:
        ftp.close()

    input('\n所有下载任务完成...按回车键继续...或者直接关闭本窗口')


def main():
    try:
        download_files_via_ftp()
    except Exception as e:
        print(f'程序执行出错：{str(e)}')


if __name__ == '__main__':
    main()
