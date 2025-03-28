#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
cd $CURRENT_DIR
if [[ -f $CURRENT_DIR/usr/ ]]; then
    echo 运行库已安装，按回车键退出
    read
    exit
fi
aria2c -x 16 -s 16 -d /tmp https://sourceforge.net/projects/deep-wine-runner-wine-download/files/bwrap-runtime/library.tar.xz/download
if [[ $? != 0 ]]; then
    echo 安装包下载失败！按回车键退出
    read
fi
chmod 777 -Rv .
tar -xvf /tmp/library.tar.xz
rm -vf /tmp/library.tar.xz
echo 安装完成！按回车键退出
read