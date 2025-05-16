# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1
# pip install paramiko

from pathlib import Path
import sys
import os
import paramiko
import fnmatch
import stat

# 适用于有tf卡2的安伯尼克H700掌机，要打开wifi，在rg34xx上测试通过，其他未测试
# SFTP连接设置，注意可能只有在保持亮屏状态下才能下载成功
# 需要安装paramiko，pip install paramiko
# 只需要修改host和local_path
CONFIG = {
    'host': '192.168.1.100',  # 远程主机IP，修改成你的机器ip
    'port': 22,               # 端口，默认22，不用改
    'username': 'root',   # 用户名，不用改
    'password': 'root',   # 密码，不用改
    'remote_paths': [
        '/mnt/sdcard/saves_RA',  # tf卡2，全能模拟器retroarch游戏存档
        '/mnt/sdcard/states_RA',  # tf卡2，全能模拟器retroarch即时存档
        '/mnt/sdcard/save_nds'      # tf卡2，nds模拟器drastic存档
    ],
    # 'local_path': 'C:\\Users\\Public\\Downloads'  # 本地保存路径，修改成你要保存存档的文件夹路径，注意斜杠，使用\的话要写成\\
    'local_path': 'C:/Users/Public/Downloads'  # 本地保存路径，修改成你要保存存档的文件夹路径，注意斜杠，使用\的话要写成\\
}

def download_files_via_sftp(pattern: str = '*') -> None:
    """
    使用SFTP连接远程服务器并下载文件到本地
    
    Args:
        pattern: 文件匹配模式，默认下载所有文件
    """
    host = CONFIG.get('host')
    port = CONFIG.get('port', 22)
    username = CONFIG.get('username')
    password = CONFIG.get('password')
    remote_paths = CONFIG.get('remote_paths', [])
    local_path = CONFIG.get('local_path')
    
    if not all([host, username, password, remote_paths, local_path]):
        print('SFTP配置不完整，请检查CONFIG中的设置')
        return
    
    # 确保本地目录存在
    local_dir = Path(local_path)
    if not local_dir.exists():
        local_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # 创建SSH客户端
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f'正在连接到 {host}:{port}...')
        ssh.connect(hostname=host, port=port, username=username, password=password)
        
        # 创建SFTP客户端
        sftp = ssh.open_sftp()
        
        # 递归下载文件夹函数
        def download_dir(remote_dir, local_dir_path):
            # 确保本地目录存在
            local_dir_obj = Path(local_dir_path)
            if not local_dir_obj.exists():
                local_dir_obj.mkdir(parents=True, exist_ok=True)
                
            print(f'进入远程目录: {remote_dir}')
            
            try:
                # 列出远程目录中的所有项目
                items = sftp.listdir_attr(remote_dir)
                
                for item in items:
                    remote_path = f"{remote_dir}/{item.filename}"
                    local_path = local_dir_obj / item.filename
                    
                    # 检查是否为目录
                    if stat.S_ISDIR(item.st_mode):
                        print(f'发现子目录: {item.filename}')
                        # 递归下载子目录
                        download_dir(remote_path, str(local_path))
                    else:
                        # 下载文件
                        # 使用fnmatch检查文件是否匹配模式
                        if fnmatch.fnmatch(item.filename, pattern):
                            print(f'正在下载: {remote_path}')
                            sftp.get(remote_path, str(local_path))
                            print(f'已下载到: {local_path}')
            except Exception as e:
                print(f'处理目录 {remote_dir} 时出错: {str(e)}')
        
        # 处理每个远程路径
        for remote_path in remote_paths:
            print(f'\n开始处理远程路径: {remote_path}')
            
            # 为每个远程路径创建对应的本地子目录
            path_name = os.path.basename(remote_path)
            current_local_path = local_dir / path_name
            
            # 检查远程路径是否存在
            try:
                remote_attr = sftp.stat(remote_path)
                
                # 检查是否为目录
                if stat.S_ISDIR(remote_attr.st_mode):
                    print(f'开始下载目录: {remote_path}')
                    download_dir(remote_path, str(current_local_path))
                    print(f'目录 {remote_path} 下载完成')
                else:
                    # 单个文件下载
                    filename = os.path.basename(remote_path)
                    local_file = local_dir / filename
                    print(f'正在下载单个文件: {filename}')
                    sftp.get(remote_path, str(local_file))
                    print(f'已下载到: {local_file}')
            except IOError as e:
                print(f'远程路径不存在或无法访问: {remote_path}')
                print(f'错误: {str(e)}')
        
        # 关闭连接
        sftp.close()
        ssh.close()
        input('\n所有下载任务完成...按回车键继续...或者直接关闭本窗口')
        
    except Exception as e:
        print(f'SFTP操作失败: {str(e)}')

def main():
    try:
        download_files_via_sftp()
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    main()