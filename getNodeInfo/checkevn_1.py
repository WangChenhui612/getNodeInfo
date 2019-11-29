import paramiko
import sys
import re

def chkfunc(uname, upasswd, hostIP):
    #创建一个通道
    transport = paramiko.Transport((hostIP, 22))
    transport.connect(username=uname, password=upasswd)


    ssh = paramiko.SSHClient()
    ssh._transport = transport

    #获取节点
    # stdin0, stdout0, stderr0 = ssh.exec_command("cat /etc/hosts | awk '{print $1}'")
    # node_info = stdout0.read().decode('utf-8')
    # print(node_info)

    #获取系统版本号
    # stdin1, stdout1, stderr1 = ssh.exec_command('cat /proc/version')
    # sys_version = stdout1.read().decode('utf-8')
    # print("系统版本号: ", sys_version)
    stdinc, stdoutc, stderrc = ssh.exec_command('cat /etc/redhat-release | grep -i centos')
    centos_version = stdoutc.read().decode('utf-8')
    stdinu, stdoutu, stderru = ssh.exec_command('cat /etc/issue | grep -i ubuntu')
    ubuntu_version = stdoutu.read().decode('utf-8')
    isCentos = re.search('centos', centos_version, re.IGNORECASE)
    isUbuntu = re.search('ubuntu', ubuntu_version, re.IGNORECASE)
    # if bool(isCentos):
    #     print("系统版本号: ", centos_version)
    # elif bool(isUbuntu):
    #     print("系统版本号: ", ubuntu_version)
    # else:
    #     print("系统版本号: unknown os")


    #获取GPU类型
    stdin2, stdout2, stderr2 = ssh.exec_command('lspci | grep -i nvidia | cut -d \'[\' -f 2 | cut -d \']\' -f 1 | sort | uniq')
    gpu_type = stdout2.read().decode('utf-8')
    # print("GPU类型:", gpu_type)

    #获取GPU卡个数
    stdin3, stdout3, stderr3 = ssh.exec_command('lspci | grep NVIDIA | awk -F \':\' \'{print $1}\' | sort | uniq | wc -l')
    gpu_num = stdout3.read().decode('utf-8')
    # print("GPU卡个数:", gpu_num)

    #获取CPU总核数
    stdin4, stdout4, stderr4 = ssh.exec_command('cat /proc/cpuinfo | grep processor | wc -l')
    cpu_core_num = stdout4.read().decode('utf-8')
    # print("CPU总核数:", cpu_core_num)

    #获取分区名称
    stdin5, stdout5, stderr5 = ssh.exec_command("lsblk | sed '/docker/d' | awk 'NR>1{print $1}' ")
    system_part_name = stdout5.read().decode('utf-8')
    # print("机器分区:")
    # print(system_part)

    # 获取分区大小
    stdin6, stdout6, stderr6 = ssh.exec_command("lsblk | sed '/docker/d' | awk 'NR>1{print $4}' ")
    system_part_space = stdout6.read().decode('utf-8')

    # 获取分区类型
    stdin7, stdout7, stderr7 = ssh.exec_command("lsblk | sed '/docker/d' | awk 'NR>1{print $6}' ")
    system_part_type = stdout7.read().decode('utf-8')

    #判断是否为最小化安装
    stdin8, stdout8, stderr8 = ssh.exec_command('cat /root/anaconda-ka.cfg')
    system_part = stdout8.read().decode('utf-8')

    # if 'onboot=on' in system_part:
    #     print("It's not a mini-system")
    # else:
    #     print("It's mini-system")

    # if bool(isCentos):
    #     stdin7, stdout7, stderr7 = ssh.exec_command('rpm -qa | wc -l')
    #     num_part = stdout7.read().decode('utf-8')
    #     print("已最安装文件包数目: ", num_part)
    # elif bool(isUbuntu):
    #     stdin8, stdout8, stderr8 = ssh.exec_command('dpkg -l | wc -l')
    #     num_part = stdout8.read().decode('utf-8')
    #     print("已最安装文件包数目: ", num_part)

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



    import prettytable as pt

    # tb = pt.PrettyTable( ["City name", "Area", "Population", "Annual Rainfall"])
    tb = pt.PrettyTable()
    tb.field_names = ["节点", "系统版本号", "GPU类型", "GPU卡个数", "CPU总核数", "分区大小", "分区名称", "分区类型", "是否为最小化安装"]
    tb.add_row([hostIP, centos_version, gpu_type, gpu_num, cpu_core_num, system_part_name, system_part_space, system_part_type, '是'])
    # tb.add_row(["Brifasdfae", 5905, 1857594, 1146.4])
    # tb.add_row(["Darwin", 112, 120900, 171423423423423424.7])
    # tb.add_row(["Hobart", 1357, 205556, 619.5])

    print(tb)

    transport.close()

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage:python checnevn.py root zzzzzz 10.166.15.243')
        exit(1)
    chkfunc(sys.argv[1], sys.argv[2], sys.argv[3])

