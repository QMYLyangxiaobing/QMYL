#coding:utf-8
#各个文件夹的深度可以参差不齐

import os
import os.path
import shutil
import cv2

def make_list(file_list,save_name):
    with open(save_name, mode='w') as fin:
        for line in file_list:
            fin.write('%s\n'%(line.strip()))

rootdir='D:/1011/3_LG/'
save_path='D:/1011/3_LG/save_1.txt'

new_set = []
img_num=0
fake_num=0
Fake_num=0
for idx, (root, path,files) in enumerate(os.walk(rootdir)):
    #print (path)
    # print (len(path))
    # print (idx, files) 
    for file in files:
        if file.endswith('.bmp'):
            img_path = os.path.join(root, file)
            img_path_label = '{} {}\n'.format(img_path, 1)
            img_num+=1
            if 'fake' in img_path:
                img_path_label = '{} {}\n'.format(img_path,0)
                fake_num+=1
            if 'Fake' in img_path:
                img_path_label = '{} {}\n'.format(img_path,0)
                Fake_num+=1
            new_set.append(img_path_label)
        
make_list(new_set, save_path)
lins=open(save_path).readlines()
fp=open(save_path,'w')
for s in lins:
    fp.write(s.replace('\\','/'))
fp.close()
print "The image number: ",img_num
print "Live image: ",img_num-fake_num-Fake_num
print "Fake image: ",fake_num+Fake_num
print("Hello,My Host,I Am OK!")
