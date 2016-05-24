# -*- coding:utf-8 -*-
import paramiko
def Login_account():   #登陆口令
	global IP , User ,Port ,Passwd
	IP = input('Please input your SSH IP address: ')
	User = input("Please input your username(defult:'root'): ")
	if User == '' :User = 'root'
	else :pass
	Port = input("Please input SSH Port(defult:22): ")
	if Port == '':Port = 22
	else:Port = int(Port)
	Passwd = input("Please input your password(defult:'password'): ")
	if Passwd == '':Passwd = 'javenxww'
	else:pass

def SSH_connect():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(IP,Port,User,Passwd)
	print('\n')
	stdin,stdout,stderr = ssh.exec_command('uname -a')
	system_info = ' ' + str(stdout.read(),encoding='utf8')
	stdin,stdout,stderr = ssh.exec_command('head -n 1 /etc/issue')
	OS_info = ''.join(str(stdout.read(),encoding='utf8').split())
	print(system_info,OS_info)
	stdin,stdout,stderr = ssh.exec_command('hostname')
	hostname = ''.join(str(stdout.read(),encoding='utf8').split())
	Command = ''
	while Command != 'quit pyssh':
		s = str(stdout.read(),encoding = 'utf8'),str(stderr.read(),encoding = 'utf8')
		for x in s:
			print(x)
		stdin,stdout,stderr = ssh.exec_command('pwd')
		path = ''.join(str(stdout.read(),encoding='utf8').split())
		Command = input('%s@%s:%s #'%(User,hostname,path))
		stdin,stdout,stderr=ssh.exec_command(Command)
	ssh.close

if __name__ == "__main__":
	paramiko.util.log_to_file('paramiko.log') 
	Login_account()
	SSH_connect()