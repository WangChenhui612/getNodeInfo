
import paramiko
import sys


def chkfunc():
    # 创建一个通道
    transport = paramiko.Transport(('10.166.15.243', 22))
    transport.connect(username='root', password='zzzzzz')

    ssh = paramiko.SSHClient()
    ssh._transport = transport

    # 查看nodes中的节点
    stdin, stdout, stderr = ssh.exec_command('cat /etc/hosts')
    print(stdout.read().decode('utf-8'))

    # 查看系统版本号
    # stdin, stdout, stderr = ssh.exec_command('cat /proc/version')
    # system_version = (stdout.read().decode('utf-8'))
    # print("系统版本：")
    # print(system_version)
    #
    # # 查看GPU类型
    # stdin, stdout, stderr = ssh.exec_command('lspci | grep -i nvidia')
    # gpu_type = (stdout.read().decode('utf-8'))
    # print("GPU类型：")
    # print(gpu_type)
    #
    # # 查看GPU卡个数
    # stdin, stdout, stderr = ssh.exec_command('lspci | grep -i nvidia | wc -l')
    # gpu_number = (stdout.read().decode('utf-8'))
    # print("GPU卡个数：")
    # print(gpu_number)

    # # 查看CPU总核数
    # stdin, stdout, stderr = ssh.exec_command('cat /proc/cpuinfo | grep processor | wc -l')
    # cpu_prosessors = stdout.read().decode('utf-8')
    # print("CPU总核数：")
    # print(cpu_prosessors)
    #
    # # 系统分区大小,分区名称（不统计/var/lib/docker的分区情况）
    # # stdin, stdout, stderr = ssh.exec_command("lsblk | sed '/docker/d' | awk '{printf '%-10s%-10s',$1,$4}'")
    # stdin, stdout, stderr = ssh.exec_command("lsblk | sed '/docker/d' | awk '{print $1,$4}' ")
    # system_part = stdout.read().decode('utf-8')
    # print("系统分区情况：")
    # print(system_part)
    #
    # # 判断最小化安装
    # stdin, stdout, stderr = ssh.exec_command('cat /root/anaconda-ks.cfg | grep onboot=on | wc -l')
    # onboot_number = int(stdout.read().decode('utf-8'))
    # if onboot_number > 0:
    #     print("系统是否最小化安装：\n 否")
    # else:
    #     print("系统是否最小化安装：\n 是")

    transport.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:python checkevn.py root zzzzzz')
        exit(1)
    chkfunc(sys.argv[1], sys.argv[2])

