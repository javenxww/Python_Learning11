#!/usr/bin/python3
# -*- coding:utf8 -*-
import paramiko
server = {'Vultr':['45.32.27.223',22,'root','javenxww'],
	   'Banwagon':['23.83.226.209',29972,'root','javenxww'],
	   'AlphaRacks':['104.129.0.186',22,'root','javenxww'],
	   'HostUs':['45.58.55.54',22,'root','javenxww']}

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
	Reboot_VPS('Banwagon')
	Reboot_VPS('Vultr')
	Reboot_VPS('HostUs')
	Reboot_VPS('AlphaRacks')