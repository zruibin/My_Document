
# https://blog.csdn.net/AtlanSI/article/details/87892016
# https://blog.csdn.net/weixin_44666068/article/details/100546398
# https://www.cnblogs.com/all-smile/p/16789104.html



# Set the base image to use to centos 
FROM ubuntu:22.04

# Set the file maintainer 
MAINTAINER Ruibin.Chow<ruibin.chow@qq.com>

# Set env varibles used in this Dockerfile (add a unique prefix, such as DOCKYARD) 
# Local directory with project source 
ENV DOCKYARD_SRCHOME=/home

WORKDIR $DOCKYARD_SRCHOME

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y git
RUN apt-get install -y bzip2
RUN apt-get install -y libssl-dev
RUN apt-get install -y curl
RUN apt-get install -y libncurses5-dev
RUN apt-get install -y automake autoconf libtool make
RUN apt-get install -y vim
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libreadline-dev
RUN apt-get install -y tree

RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN pip install virtualenv
RUN ln -s /usr/bin/python3 /usr/bin/python

# 中文显示
RUN apt-get install -y language-pack-zh-hans*
RUN apt-get install -y locales
RUN apt-get install -y fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming
RUN echo '\n\n\
export LANG=zh_CN.UTF-8\n\
export LANGUAGE=zh_CN:zh:en_US:en\n\n'  >> /root/.bashrc

# https://github.com/Kitware/CMake/releases/download/v3.25.2/cmake-3.25.2.tar.gz
RUN apt-get install -y cmake


# WORKDIR $software_dir
# WORKDIR $software_dir/nginx-1.8.0 
# RUN ./configure --prefix=/usr/local/nginx --with-threads --with-http_stub_status_module --with-ipv6 --with-http_ssl_module
# RUN tar -xzvf nginx-1.8.0.tar.gz
# RUN make && make install 


WORKDIR $DOCKYARD_SRCHOME

# COPY requirements.txt $DOCKYARD_SRCPROJ

# Install Python dependencies 
# RUN pip install --upgrade pip
# RUN pip install virtualenv
# RUN cd $DOCKYARD_SRCPROJ
# RUN virtualenv env
# RUN cd $DOCKYARD_SRCHOME
# RUN tar -xvf nginx-1.8.0.tar.gz 


# Port to expose 
# EXPOSE 5000
# EXPOSE 3306
# EXPOSE 6379
# EXPOSE 8080
# EXPOSE 80

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
# CMD ["/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf", "-g", "daemon off;"]

RUN echo '\n\nexport CLICOLOR=1\n\
export LSCOLORS=gxfxcxdxbxegedabagacad\n\
export PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\$"\n\
export TERM=xterm-256color\n\n' >> /root/.bashrc


WORKDIR $DOCKYARD_SRCHOME




#docker run -d -i -t -v /Users/ruibin.chow/Desktop/zruibin_service/home:/home -p 88:80 -p 8181:8080 -p 5001:5000 6f745b190168 /bin/bash
# docker build .



