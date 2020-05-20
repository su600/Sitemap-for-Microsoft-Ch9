import os

def rename():
    # i = 0
    path = r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\More-Python-for-Beginners"

    filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
    # fix 获取的文件列表顺序并非按顺序，而是 1,10,11,12,2,3,4,5 
    filelist.sort(key = lambda x: int(x[:-9])) ##文件名按数字排序
    print(filelist)
    a=input()
    # srt_list=[]
    mp4_list=[]
    for files in filelist:   #遍历所有文件
        # print(files,type(files))
        # if os.path.isdir(Olddir):       #如果是文件夹则跳过
        #         continue

        if '.srt' in files:
            # srt_list.append(files)
            mp4_list.append(files.replace('.srt','.mp4'))
    # print(mp4_list)
    i=0
    for files in filelist:
        if '.mp4' in files:
             os.rename(os.path.join(path, files), os.path.join(path, mp4_list[i]))
             i+=1

if __name__ == '__main__':
    rename()
