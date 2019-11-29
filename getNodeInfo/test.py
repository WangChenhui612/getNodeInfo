import paramiko
import json
import sys




def chkfunc(uname, upasswd):
    #创建一个通道
    transport = paramiko.Transport(('10.166.15.243', 22))
    transport.connect(username='root', password='zzzzzz')


    ssh = paramiko.SSHClient()
    ssh._transport = transport

    #获取节点
    stdin0, stdout0, stderr0 = ssh.exec_command("cat /etc/hosts | awk '{print $1}'")
    node_info = stdout0.read().decode('utf-8')
    print(node_info)

    #获取系统版本号
    stdin1, stdout1, stderr1 = ssh.exec_command('cat /proc/version')
    sys_version = stdout1.read().decode('utf-8')
    print("系统版本号: ", sys_version)

    #获取GPU类型
    stdin2, stdout2, stderr2 = ssh.exec_command('lspci | grep -i nvidia')
    gpu_type = stdout2.read().decode('utf-8')
    print("GPU类型:", gpu_type)

    #获取GPU卡个数
    stdin3, stdout3, stderr3 = ssh.exec_command('lspci | grep -i nvidia | wc -l')
    gpu_num = stdout3.read().decode('utf-8')
    print("GPU卡个数:", gpu_num)

    #获取CPU总核数
    stdin4, stdout4, stderr4 = ssh.exec_command('cat /proc/cpuinfo | grep processor | wc -l')
    cpu_core_num = stdout4.read().decode('utf-8')
    print("CPU总核数:", cpu_core_num)

    #获取分区大小和名称
    stdin5, stdout5, stderr5 = ssh.exec_command("lsblk | sed '/docker/d' | awk '{print $1, $4}' ")
    system_part = stdout5.read().decode('utf-8')
    print(system_part)

    #判断是否为最小化安装
    stdin6, stdout6, stderr6 = ssh.exec_command('cat /root/anaconda-ka.cfg')
    system = stdout6.read().decode('utf-8')

    if 'onboot=on' in system:
        print("It's not a mini-system")
    else:
        print("It's mini-system")

    '''
    1.      提供nodes
    cat /etc/hosts
    2.      系统版本
    cat /etc/rehat-release
    cat /etc/issue
    或者
    cat /proc/version
    3.      GPU卡类型
    nvidia-smi -a | grep 'Product Name'’'     (安装GPU驱动的时候)
    lspci | grep -i nvidia                  (没有安装GPU驱动的时候)
    4.      GPU卡个数
    nvidia-smi -a | grep 'Product Name' | wc -l (安装GPU驱动的时候)
    lspci | grep -i nvidia | wc -l             (没有安装GPU驱动的时候)
    5.      CPU总核数
    cat /proc/cpuinfo | grep processor | wc -l
    6.      CPU总颗数
    cat /proc/cpuinfo | grep 'physical id'
    7.      系统分区
    lsblk
    8.      判断最小化安装
    cat /root/paramiko | grep onboot=off    (参考网页收藏链接)
    '''

    transport.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:python checnevn.py root zzzzzz')
        exit(1)
    chkfunc(sys.argv[1], sys.argv[2])

