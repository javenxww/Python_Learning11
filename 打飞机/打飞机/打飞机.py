﻿加载背景音乐
播放背景音乐（单曲循环）
加载背景图片
我方飞机诞生
interval = 0

while True:
	if 用户是否点开关闭：
		推出
		break

	interval += 1
	if interval == 50:
		interval = 0
		小飞机诞生	

	小飞机向下移动一个位置
	屏幕刷新
		
	if 用户鼠标移动
		我方飞机中心位置=鼠标位置
		屏幕刷新

	if 我方飞机位置与敌方飞机接触
		我方飞机挂，播放死亡音乐
		修改飞机图片
		切换死亡界面
		停止音乐
