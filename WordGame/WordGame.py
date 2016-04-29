# -*- coding:utf-8 -*-
import random
secret = random.randint(1,10)
temp = input("请输入一个10以内的数字：")
while temp.isdigit() != True:
	temp = input("你的输入有误，请输入一个10以内的数字：")
guess = int(temp)
while guess < 0 or guess > 10 :
	temp = input("你输入的范围不对哦！请输入一个10以内的数字：")
	guess = int(temp) 
t = 0
if guess == secret:
	print("太厉害了!")
	print("你只用一次就猜对了!!!")
	t = 4
while t < 3:
	if guess == secret:
		print("你猜对啦！！")
		t = 4
	else:
		if guess > secret :
			t = t + 1
			print("猜的太大啦~你只剩%d次机会啦" % (3-t))
			temp = input("请重新输入:")
			guess = int(temp)
		else:
			t = t + 1
			print("猜小啦~你只剩%d次机会啦" % (3-t))
			temp = input("请重新输入:")
			guess = int(temp)
			
if t == 3:
	print("你的机会用光啦~")