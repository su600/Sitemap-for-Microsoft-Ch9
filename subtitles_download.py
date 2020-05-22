urls = subtitle_list1  # 英文字幕
for i in urls:
    name = str(i).split('/ca')[0].split('/')[-1]+'.srt'
    ## 直接修改扩展名为srt
    try:
        num = str(i).split('/ca')[0].split('-of-')[1]+'-' + \
            str(i).split('/ca')[0].split('-of-')[0].split('-')[-1]+' '
        name = num+name
    except Exception as e:
        print(e)
    else:
        pass
    
    # 下载字幕文件
    r = requests.get(i)

    with open(name, "wb") as f:
        f.write(r.content)
        f.close()

    ## 按srt格式转换
    with open(name, "r", encoding="utf-8") as fin:
        fileContent = fin.readlines()
        lineNum = 2
        fileMaxLineNum = len(fileContent)
        with open(name, "w", encoding="gbk") as fout:
            fout.write("1\n")
            for i in range(2, fileMaxLineNum):
                fout.write(fileContent[i].replace(".", ","))
                if(fileContent[i].strip() == "" and i+1 < fileMaxLineNum and fileContent[i+1].strip() != ""):
                    fout.write(str(lineNum)+"\n")
                    lineNum += 1
    print(name)

print('字幕已下载完成')