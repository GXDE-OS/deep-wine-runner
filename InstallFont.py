#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi
# 版本：2.1.0
# 更新时间：2022年08月25日
# 感谢：感谢 wine 以及 deepin-wine 团队，提供了 wine 和 deepin-wine 给大家使用，让我能做这个程序
# 基于 Python3 构建
###########################################################################################
#################
# 引入所需的库
#################
import os
import sys
import json
import shutil
import updatekiller
import req as requests
homePath = os.path.expanduser('~')
try:
    sourcesList = [
        "http://fonts.wine-runner.gfdgdxi.top/list.json",
        "https://code.gitlink.org.cn/gfdgd_xi/wine-runner-list/raw/branch/master/fonts/list.json"
        ]
    change = False
    for i in sourcesList:
        try:
            fontList = json.loads(requests.get(i).text)
            change = True
            break
        except:
            pass
    if not change:
        fontList = json.loads(requests.get(sourcesList[0]).text)
except:
    print("使用离线列表")
    fontList = [
    [
        "fake_simsun.ttc",
        "http://fonts.wine-runner.gfdgdxi.top/fake_simsun.ttc",
        "simsun.ttc",
        "fake_simsun.ttc（会替换容器内的宋体）"
    ],
    [
        "simsun.ttc",
        "http://fonts.wine-runner.gfdgdxi.top/simsun.ttc",
        "simsun.ttc",
        "simsun.ttc"
    ],
    [
        "simsunb.ttf",
        "http://fonts.wine-runner.gfdgdxi.top/simsunb.ttf",
        "simsunb.ttf",
        "simsunb.ttf"
    ],
    [
        "msyh.ttc",
        "http://fonts.wine-runner.gfdgdxi.top/msyh.ttc",
        "msyh.ttc",
        "msyh.ttc"
    ],
    [
        "msyhl.ttc",
        "http://fonts.wine-runner.gfdgdxi.top/msyhl.ttc",
        "msyhl.ttc",
        "msyhl.ttc"
    ],
    [
        "msyhbd.ttc",
        "http://fonts.wine-runner.gfdgdxi.top/msyhbd.ttc",
        "msyhbd.ttc",
        "msyhbd.ttc"
    ]
]
def Download(wineBotton: str, id: int) -> int:
    return os.system(f"aria2c -x 16 -s 16 -d '{wineBotton}/drive_c/windows/Fonts/' -o '{fontList[id][0]}' \"{fontList[id][1]}\"")

if __name__ == "__main__":
    if "--help" in sys.argv:
        print("作者：gfdgd xi")
        print("版本：1.0.0")
        print("本程序可以更方便的在 wine 容器中安装指定应用")
        sys.exit()
    if len(sys.argv) <= 1 or sys.argv[1] == "":
        print("您未指定需要安装的容器，无法继续")
        print("参数：")
        print("XXX 参数一")
        print("参数一为需要安装的容器")
        sys.exit()
    while True:
        os.system("clear")
        print('''                                   
 mmmmmm                 m          
 #       mmm   m mm   mm#mm   mmm  
 #mmmmm #" "#  #"  #    #    #   " 
 #      #   #  #   #    #     """m 
 #      "#m#"  #   #    "mm  "mmm" 
                                   
                                   
''')
        if not os.path.exists(f"{sys.argv[1]}/drive_c/windows/Fonts"):
            input("您选择的不是 Wine 容器，无法继续，按回车键退出")
            exit()
        
        for i in range(0, len(fontList)):
            print(f"{i} {fontList[i][3]}")
        while True:
            try:
                choose = input("请输入要选择的 字体（输入“exit”退出）：").lower()
                if choose == "exit":
                    break
                choose = int(choose)
            except:
                print("输入错误，请重新输入")
                continue
            if 0 <= choose and choose < len(fontList):
                break
        if choose == "exit":
            exit()
        print(f"您选择了字体 {fontList[choose][0]}")
        if os.path.exists(f"{homePath}/.cache/deepin-wine-runner/font/{fontList[choose][0]}"):
            print("已经缓存，使用本地版本")
            if os.path.exists(f"{sys.argv[1]}/drive_c/windows/Fonts/{fontList[choose][2]}"):
                print("字体已存在，覆盖")
            shutil.copy(f"{homePath}/.cache/deepin-wine-runner/font/{fontList[choose][0]}", f"{sys.argv[1]}/drive_c/windows/Fonts/{fontList[choose][2]}")
            input("安装结束，按回车键继续")
            continue
        print("开始下载")
        os.system(f"rm -rf '{homePath}/.cache/deepin-wine-runner/font/{fontList[choose][0]}'")
        os.system(f"mkdir -p '{homePath}/.cache/deepin-wine-runner/font'")
        os.system(f"aria2c -x 16 -s 16 -d '{homePath}/.cache/deepin-wine-runner/font' -o '{fontList[choose][0]}' \"{fontList[choose][1]}\"")
        if os.path.exists(f"{sys.argv[1]}/drive_c/windows/Fonts/{fontList[choose][2]}"):
            print("字体已存在，覆盖")
        try:
            shutil.copy(f"{homePath}/.cache/deepin-wine-runner/font/{fontList[choose][0]}", f"{sys.argv[1]}/drive_c/windows/Fonts/{fontList[choose][2]}")
        except:
            print("拷贝失败！")
        input("安装结束，按回车键继续")