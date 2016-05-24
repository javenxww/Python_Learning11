#!/usr/bin/python3
# -*- coding:utf8 -*-
import paramiko
<<<<<<< HEAD
server = {'servername':['ip',port,'user','password']}   #change it as your own ssh account
=======
server = {'Vultr':['xxx.xxx.xxx.xxx',22,'root','password'], # change it as your own SSH account,use ','to split them
	   'Linode':['xxx.xxx.xxx.xxx',22,'root','password']}	# 'server name':['ip',port,'user','password']
>>>>>>> origin/master

def Reboot_VPS(server_name):
	server_account = server[server_name]
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(*server_account)
		stdin,stdout,stderr = ssh.exec_command('uname -a')
		system_info = ' ' + str(stdout.read(),encoding='utf8')
		stdin,stdout,stderr = ssh.exec_command('head -n 1 /etc/issue')
		OS_info = ' '.join(str(stdout.read(),encoding='utf8').split())
		print('***********************************************')
		print(system_info,OS_info)
		stdin,stdout,stderr = ssh.exec_command('reboot')
		print(' %s Reboot'%server_name)
		print('***********************************************')
	except TimeoutError as e:
		print('***********************************************')
		print(' %s connect ERROR'%server_name)
		print('***********************************************')




if __name__ == "__main__":
<<<<<<< HEAD
	Reboot_VPS('servername')  #change it as your own server name
=======
	Reboot_VPS('Vultr')  #change it as your own server name
	Reboot_VPS('Linode')
>>>>>>> origin/master
