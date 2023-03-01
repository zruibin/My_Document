####docker常用命令

```
docker images 查看所有镜像
docker ps  查看当前正在运行的容器
docker ps -a 查看所有容器
docker run -d -t -i 容器id /bin/bash  运行一个容器
docker start/stop/restart 容器id 启动/停止/重启一个容器
docker attach 容器id /bin/bash 进入容器，但exit会停止运行容器
docker exec -it 容器id /bin/bash 进入容器，但exit不会停止运行容器
“exit”或者按键“Ctrl + C” 退出容器

docker run -d -i -t -v 宿主绝对目录:容器绝对目录 容器id /bin/bash 挂载本地目录及实现文件共享
docker run -d -i -t -p 宿主端口:容器端口 容器id /bin/bash 运行容器并端口映射，可-p多个端口


docker system df  查看 Docker 的磁盘使用情况
docker system prune --volumes   清除命令


docker commit -a "runoob.com" -m "my apache" 容器名称或id 打包的镜像名称:标签 
OPTIONS说明： 
-a :提交的镜像作者； 
-c :使用Dockerfile指令来创建镜像； 
-m :提交时的说明文字； 
-p :在commit时，将容器暂停。

docker save ubuntu:load>/root/ubuntu.tar
docker load<ubuntu.tar

docker save保存的是镜像（image），docker export保存的是容器（container）；
docker load用来载入镜像包，docker import用来载入容器包，但两者都会恢复为镜像；
docker load不能对载入的镜像重命名，而docker import可以为镜像指定新名称。
```