import paramiko
import json
import sys



#创建一个通道
transport = paramiko.Transport(('10.166.15.243', 22))
transport.connect(username='root', password='zzzzzz')


ssh = paramiko.SSHClient()
ssh._transport = transport

#
# #获取节点
# stdin0, stdout0, stderr0 = ssh.exec_command("cat /etc/hosts | awk '{print $1}'")
# node_info = stdout0.read().decode('utf-8')
# print(node_info)


#获取节点
stdin0, stdout0, stderr0 = ssh.exec_command("lsblk | sed '/docker/d' | awk '{print $1, $4, $6}'")
node_info = stdout0.read().decode('utf-8')
print(node_info)