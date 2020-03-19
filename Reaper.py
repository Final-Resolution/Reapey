# coding=UTF-8
# Author：FinalRun
# Date：2020年3月19日

from __future__ import division
import os
import time
import sys
import jieba





localdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



filelist = {}  # 文件名
dict_temp = {}  # 字典
is_ok = {}  # 交作业判断符

# 打开名单读取信息保存到字典和词库
def load_dict_from_file():
    global dict_temp, is_ok
    dict_temp.clear()
    is_ok.clear() 
    with open('list.txt', 'r', encoding = 'utf-8') as dict_file:  # 打开文件
        for line in dict_file.readlines():
            (key, value) = line.strip().split(':')
            dict_temp[key] = value  # 添加班级信息字典
            is_ok[key] = 0  # 交作业判断字典
            jieba.add_word(key)  # 保存名字到jieba词库

#找文件名
def get_file_list():
    global filelist
    rootdir = 'file' #作业文件路径
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        paths = os.path.join(rootdir, list[i])
        (key, value) = os.path.basename(paths).split('.')  # 每个文件的名字做一个列表元素
        filelist[key] = value

#work_name = input("请输入当前作业的名称：")

load_dict_from_file()
get_file_list()

m = len(filelist)  # 打印出目录下所有的文件
#计算未提交人数（减去list列表的第一行）
listnum =len(dict_temp) - (m + 1)

del dict_temp['姓名']

for n in filelist:
    words = jieba.lcut(n)
    # print (word)  # 分词测试
    for key in dict_temp:
        for word in words:
            if word == key:
                oldname = './file/' + n + '.' + filelist[n]
                newname = './file/' + dict_temp[key] + key + '.' + filelist[n]
                # print (oldname)  # 测试语句
                # print (newname)  # 测试语句
                os.rename(oldname, newname)
                is_ok[key] = 1
                break

# 打印统计
print ('目前共有{}人已交作业'.format(m))
print ("剩余: %d " % listnum + "未提交作业\n")
time.sleep(2)
# 分辨没有交作业的
# print (is_ok.keys())
print("未提交作业名单如下：\n")
del is_ok['姓名']

for key in is_ok:
    if is_ok[key] == 0:
            print ("{}".format(key))
print ("---------------------")
print ("作业已统计完成")







#生成文件统计记录文件logs.txt

print ("正在生成统计记录文件")
#日志文件名 
filename = 'logs.txt'

#打开文件并写入内容
with open(filename, 'w', encoding="UTF-8") as file_object:
	file_object.write("文件统计日志记录如下：\n")
	file_object.write('目前共有 {} 人已交作业'.format(m) + '\n')
	file_object.write("剩余" + " %d " % listnum + "人未提交作业\n")
	file_object.write('\n' + "----------------------------------------------" + '\n')
	file_object.write("\n" + "未提交作业具体名单如下：\n")
	
	#循环写入名单
	for key in is_ok:
		if is_ok[key] == 0:
			file_object.write("{}".format(key) + '\n')

	file_object.write('\n' + "----------------------------------------------" + '\n')
	file_object.write("\n" + "文件统计日期：")
	file_object.write(localdate + '\n')


#关闭记录文件
file_object.close()


#极度虚伪の加载条
if __name__ == '__main__':
    for i in range(1,10):
        sys.stdout.write('#'+'->'+"\b\b")
        sys.stdout.flush()
        time.sleep(0.5)
print

#程序退出
print('\n' +"统计记录文件生成完毕！\n")
time.sleep(2)
print("程序将于三秒后退出\n")
time.sleep(3)
