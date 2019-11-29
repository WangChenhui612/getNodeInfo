import paramiko

def chkfunc(uname, upasswd):
    #创建一个通道
    transport = paramiko.Transport(('10.166.15.243', 22))
    transport.connect(username='root', password='zzzzzz')


    ssh = paramiko.SSHClient()
    ssh._transport = transport

    stdin, stdout, stderr = ssh.exec_command('cat /etc/hosts')
    node_info = stdout.read().decode('utf-8')
    stdin, stdout, stderr = ssh.exec_command('cat /etc/hosts | wc -l')
    node_num = stdout.read().decode('utf-8')
    for i in node_num:
        #获取GPU版本信息
        print('----------------------------------------------------')
        stdin, stdout, stderr = ssh.exec_command('cat /proc/version')
        OS_info = stdout.read().decode('utf-8')
        OS_ID = 'CentOS'
        if 'Ubuntu' in OS_ID:
            OS_ID = 'Ubuntu'

        print(stdout.read().decode('utf-8'))

    transport.close()