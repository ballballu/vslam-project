# Vslam-project
## notice
*	plateform hasee mini pc
* 	password:robot223
* 	run the gui software: xslam_viewer.run
* 	has c++ sdk and a sample code
*	server.py作为手机和pc通讯进程，所得内容保存在received.txt里
*	receiver.py作为处理接收到的内容进程，并把结果写入command.txt。具体
	命令定义看程序前的注释。


* 	receiver.py 里用到了thulac作为分词工具用下面命令安装
        ```
		sudo pip install thulac
		```