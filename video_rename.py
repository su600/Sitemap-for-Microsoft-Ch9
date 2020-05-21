import os

def rename():
    path = r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\Even-More-Python-for-Beginners-Data-Tools"

    filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
    # 视频文件名不太明确，且播放器会自动加载文件名一致的字幕文件，需要根据下载的字幕文件名批量修改
    # 获取的字幕文件列表顺序并非按数字顺序，而是 1,10,11,12 按字符排序 需要修改列表顺序 依次修改视频文件名
  
    # print(filelist)
    # a=input() 
    srt_list=[]
    mp4_list=[]
    for files in filelist:   #遍历所有文件
        
        # 字幕文件列表 提取文件名并修改扩展名 作为视频文件名称
        if '.srt' in files:
            # srt_list.append(files)
            srt_list.append(files.replace('.srt','.mp4'))
    # 字幕文件重新排序
    srt_list=sorted(srt_list, key=lambda x:int(x.split("-")[1].split(' ')[0]))
    # print(srt_list)

    # 所有mp4文件
    i=0
    for files in filelist:
        if '.mp4' in files:
            print(files)
            print(srt_list[i])
            # 根据字幕文件 顺序重命名视频文件
            os.rename(os.path.join(path, files), os.path.join(path, srt_list[i]))
            i+=1

if __name__ == '__main__':
    rename()
