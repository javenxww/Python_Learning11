# -*- conding:utf-8 -*-
#file:PytOptimize.py
import tkinter
import tkinter.messagebox
class Window():
	def __init__(self):
		self.root = tkinter.Tk()

		#创建菜单
		menu = tkinter.Menu(self.root)
		#创建系统子菜单
		submenu = tkinter.Menu(menu,tearoff = 0)
		submenu.add_command(label = "关于...",command = self.MenuAbout)
		submenu.add_separator()
		submenu.add_command(label = "退出",command = self.MenuExit)
		menu.add_cascade(label = "系统",menu = submenu)
		#创建清理子菜单
		submenu = tkinter.Menu(menu,tearoff=0)
		submenu.add_command(label = "扫描垃圾文件",command = RubbishScan)
		submenu.add_command(label = "清除垃圾文件",command = RubbishDel)
		menu.add_cascade(label = "清理",menu = submenu)
		#创建查找子菜单
		submenu = tkinter.Menu(menu,tearoff = 0)
		submenu.add_command(label = "搜索大文件",command = SearchBigFile)
		submenu.add_separator()
		submenu.add_command(label = "按名称搜索文件",command = SearchByName)
		menu.add_cascade(label = "查找",menu = submenu)
		
		self.root.config(menu=menu)

		#创建标签用于显示状态
		self.progress = tkinter.Label(self.root,anchor = tkinter.W,text = '状态',bitmap = 'hourglass',compound = 'left')
		self.progress.place(x = 10,y = 10,width = 480,heigh = 15)

		#创建文本框，显示文件列表
		self.flist = tkinter.Text(self.root)
		self.flist.place(x = 10, y = 10,width = 480,heigh = 350)

		#为文本框添加滚动条
		self.vscroll = tkinter.Scrollbar(self.flist)
		self.vscroll.pack(side = 'right',fill = 'y')
		self.flist['yscrollcommand'] = self.vscroll.set
		self.vscroll['command'] = self.flist.yview

	def MenuAbout(self):
		tkinter.messagebox.showinfo('PyOptimize','自制')

	def MenuExit(self):
		self.root.quit()

	def RubbishScan(self):
		result = tkinter.messagebox.askquestion('PyOptimize','扫描垃圾文件需要很长时间，是否继续')
		if result == 'no':
			return
		tkinter.messagebox.showinfo('Pyoptimize','马上删除垃圾文件')


	def MainLoop(self):
		self.root.title('PyOptimize')
		self.root.minsize(500,400)
		self.root.maxsize(500,400)
		self.root.mainloop()

if __name__ == "__main__":
	window = Window()
	window.MainLoop()