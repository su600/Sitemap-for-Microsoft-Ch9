# aa='<title>Demo: Introducing Anaconda | Even More Python for Beginners - Data Tools [4 of 31] | Even More Python for Beginners - Data Tools  | Channel 9</title>'
# nn=((aa.split('|')[0])+(aa.split('|')[0])).replace('<title>','')
# print(nn)

import os

path = r"C:\Users\su514\Desktop\ss"

filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
# fix 获取的文件列表顺序并非按顺序，而是 1,10,11,12,2,3,4,5 
# filelist=sorted(filelist, key=lambda x:int(x.split("-")[1].split(' ')[0]))
# filelist.sort(key = lambda x: int(x[:5])) ##文件名按数字排序
print(filelist)
input()


path = r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\Even-More-Python-for-Beginners-Data-Tools"
mp4_list=[]


filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
for files in filelist:   #遍历所有文件
    if '.srt' in files:
        # srt_list.append(files)
        mp4_list.append(files.replace('.srt','.mp4'))

mp4_list =sorted(mp4_list, key=lambda x:int(x.split("-")[1].split(' ')[0]))
print(mp4_list)
# input()
# fix 获取的文件列表顺序并非按顺序，而是 1,10,11,12,2,3,4,5 

# print(filelist)
# a=input()
# srt_list=[]

# for files in filelist:   #遍历所有文件
#     # print(files,type(files))
#     # if os.path.isdir(Olddir):       #如果是文件夹则跳过
#     #         continue

#     # if '.srt' in files:
#     #     # srt_list.append(files)
#     #     mp4_list.append(files.replace('.srt','.mp4'))
# # print(mp4_list)
newpath=r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\Even-More-Python-for-Beginners-Data-Tools\mp4"
i=0
for files in filelist:
    if '.mp4' in files:
            os.rename(os.path.join(path, files), os.path.join(newpath, mp4_list[i]))
            i+=1