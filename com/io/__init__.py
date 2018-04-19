import os
def dir_l(path1):
    for x in os.listdir(path1) :
#         print("lasdf")
#         print(x)
        if os.path.isdir(x):
            print("asdfasdf")
            print(os.path.join(path1,os.path.sep,x))

dir_l("D:\QQMusicCache")