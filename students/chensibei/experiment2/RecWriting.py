#utf-8
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)#����mnist����

import sys
import tensorflow as tf

# coding=gbk

from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt
sys.setrecursionlimit(1000000)#�������ݹ�


INPUT_NODE = 784
OUTPUT_NODE = 10

count = 0


def ImageToMatrix(filename):#����ͼƬ��������ʽ������ͼƬ��
    im = Image.open(filename)
    width, height = im.size
    im = im.convert("L")#תΪ�ڰ׵�ͨ��

    data = np.array(im)
    new_data = np.reshape(data, (height, width))#������ͼƬͬ��С�Ķ�ά����

    print"data finished"
    return new_data#��������


def gotoBinary(filename, data):#���ɺڵװ���ͼƬ��ʽ������ͼƬ����ͼƬ��������ʽ
    im = Image.open(filename)#pillow��ͼƬ
    width, height = im.size#�õ�ͼƬ�Ĵ�С
    new_data = np.zeros((height, width))
    for i in range(0,height):
        for j in range(0,width):
            if (data[i,j] > 100):#���ԭͼ���ػҶȴ���100��ƫ�ף�
                new_data[i,j] = 0#����ͼ������Ϊ0����ɫ��
            else:
                new_data[i,j] = 255#������Ϊ��ɫ

    im = Image.fromarray(new_data.astype(np.uint8))#������תΪpillowͼƬ��ʽ
    print "binarydata finished"
    return new_data,im#���غڵװ���ͼƬ��������ʽ��pillowͼƬ��ʽ



def CLASS(data):#��ȡ��Ч�������أ����࣬�и�ĵ�һ��������ͨ����ʶ��Class����������������һ����ͨ������Class��һ�����ѵ�ǰClass����������
    width = data.shape[0]
    height = data.shape[1]
    new_data = np.zeros((width, height),int)#����һ�������飬�����������
    Class = 1#��ʼʱ���Ϊ1
    for i in range(0,width):#ÿ��ÿ�е���������
        for j in range(0,height):
            global count#count�ǵ�ǰ��ͨ��������������
            count = 0
            if (data[i,j] == 255 and new_data[i,j] == 0):#���ԭͼ�������ǰ�ɫ�����ֲ��֣����������������������û������
                check(data, i, j, Class, height, width, new_data)#�������࣬��ʼ�ݹ�
                if(count >=10):#��������ͨ������������������10����Ϊ������������
                    Class = Class+1#���������һ����ʼѰ����һ����ͨ����

    print (Class)
    return new_data, Class



def check(data, i, j, tap, height, width, new_data):#�ݹ�Ѱ����ͨ��������������
    global count
    new_data[i,j] = int(tap)#��������鵱ǰ����������ΪĿǰ����
    count = count+1#��ͨ����������ֵ+1
    if (i > 0):#����Ȧ��8�����صݹ�
        if (data[i - 1,j] == 255 and new_data[i - 1,j] == 0):#����������Ҳ��ͬ�࣬��ݹ��������
            check(data, i - 1, j, tap, height, width, new_data)
    if (i < width - 2):
        if (data[i + 1,j] == 255 and new_data[i + 1 ,j] == 0):#����ұ�����Ҳ��ͬ�࣬��ݹ��ұ�����
            check(data, i + 1, j, tap, height, width, new_data)
    if (j > 0):
        if (data[i,j - 1] == 255 and new_data[i,j - 1] == 0):#����ϱ�����Ҳ��ͬ�࣬��ݹ��ϱ�����
            check(data, i, j - 1, tap, height, width, new_data)
    if (j < height - 2):
        if (data[i,j+1] == 255 and new_data[i,j + 1] == 0):#����±�����Ҳ��ͬ�࣬��ݹ��±�����
            check(data, i, j + 1, tap, height, width, new_data)
    if(i>0 and j>0):
        if(data[i-1,j-1] == 255 and new_data[i-1,j-1]==0):#������ϱ�����Ҳ��ͬ�࣬��ݹ����ϱ�����
            check(data,i-1,j-1,tap,height,width,new_data)
    if(i>0 and j<height -2):
        if(data[i-1,j+1] == 255 and new_data[i-1,j+1]==0):#������±�����Ҳ��ͬ�࣬��ݹ����±�����
            check(data,i-1,j+1,tap,height,width,new_data)
    if(i<width-2 and j>0):
        if(data[i+1,j-1] == 255 and new_data[i+1,j-1] ==0):#������ϱ�����Ҳ��ͬ�࣬��ݹ����ϱ�����
            check(data,i+1,j-1,tap,height,width,new_data)
    if(i<width-2 and j<height -2):
        if(data[i+1,j+1]==255 and new_data[i+1,j+1]==0):#������±�����Ҳ��ͬ�࣬��ݹ����±�����
            check(data,i+1,j+1,tap,height,width,new_data)

    if (i > 1):#�ڶ�Ȧ��8�����صݹ�
        if (data[i - 2,j] == 255 and new_data[i - 2,j] == 0):#�����ߵڶ�������Ҳ��ͬ�࣬��ݹ��������
            check(data, i - 2, j, tap, height, width, new_data)
    if (i < width - 3):
        if (data[i + 2,j] == 255 and new_data[i + 2 ,j] == 0):#����ұߵڶ�������Ҳ��ͬ�࣬��ݹ��ұ�����
            check(data, i + 2, j, tap, height, width, new_data)
    if (j > 1):
        if (data[i,j - 2] == 255 and new_data[i,j - 2] == 0):#����ϱߵڶ�������Ҳ��ͬ�࣬��ݹ��ϱ�����
            check(data, i, j - 2, tap, height, width, new_data)
    if (j < height - 3):
        if (data[i,j+2] == 255 and new_data[i,j + 2] == 0):#����±ߵڶ�������Ҳ��ͬ�࣬��ݹ��±�����
            check(data, i, j + 2, tap, height, width, new_data)
    if(i>1 and j>1 ):
        if(data[i-2,j-2] == 255 and new_data[i-2,j-2]==0):#������ϵ����ϵ�����Ҳ��ͬ�࣬��ݹ����ϵ���������
            check(data,i-2,j-2,tap,height,width,new_data)
    if(i>1 and j<height -3):
        if(data[i-2,j+2] == 255 and new_data[i-2,j+2]==0):#������µ����µ�����Ҳ��ͬ�࣬��ݹ����µ���������
            check(data,i-2,j+2,tap,height,width,new_data)
    if(i<width-3 and j>1):
        if(data[i+2,j-2] == 255 and new_data[i+2,j-2] ==0):#������ϵ����ϵ�����Ҳ��ͬ�࣬��ݹ����ϵ���������
            check(data,i+2,j-2,tap,height,width,new_data)
    if(i<width-3 and j<height -3):
        if(data[i+2,j+2]==255 and new_data[i+2,j+2]==0):#������µ����µ�����Ҳ��ͬ�࣬��ݹ����µ���������
            check(data,i+2,j+2,tap,height,width,new_data)

    if (i > 2):#����Ȧ��8�����صݹ�
        if (data[i - 3,j] == 255 and new_data[i - 3,j] == 0):
            check(data, i - 3, j, tap, height, width, new_data)
    if (i < width - 4):
        if (data[i + 3,j] == 255 and new_data[i + 3 ,j] == 0):
            check(data, i + 3, j, tap, height, width, new_data)
    if (j > 2):
        if (data[i,j - 3] == 255 and new_data[i,j - 3] == 0):
            check(data, i, j - 3, tap, height, width, new_data)
    if (j < height - 4):
        if (data[i,j+3] == 255 and new_data[i,j + 3] == 0):
            check(data, i, j + 3, tap, height, width, new_data)
    if(i>2 and j>2):
        if(data[i-3,j-3] == 255 and new_data[i-3,j-3]==0):
            check(data,i-3,j-3,tap,height,width,new_data)
    if(i>2and j<height -4):
        if(data[i-3,j+3] == 255 and new_data[i-3,j+3]==0):
            check(data,i-3,j+3,tap,height,width,new_data)
    if(i<width-4 and j>2):
        if(data[i+3,j-3] == 255 and new_data[i+3,j-3] ==0):
            check(data,i+3,j-3,tap,height,width,new_data)
    if(i<width-4 and j<height -4):
        if(data[i+3,j+3]==255 and new_data[i+3,j+3]==0):
            check(data,i+3,j+3,tap,height,width,new_data)


def SPLIT(data, Class):#��¼ÿ�������߾࣬�ϱ߾࣬�ұ߾࣬�±߾࣬�ָ�ڶ���
    width = data.shape[0]
    height = data.shape[1]   

    Class = Class+1
    left = np.zeros((Class),int)#�����������ұ߾���������飬�±������ţ������Ǳ߾�����ֵ
    top = np.zeros((Class),int)
    botton = np.zeros((Class),int)#���µ�ֵΪͼƬ��������
    I = np.zeros((Class),int)#���ҵ�ֵΪͼƬ��������

    for m in range(0,Class):#��ʼ��
        left[m] = height #�����ֵΪͼƬ��������
        top[m] = width#���ϵ�ֵΪͼƬ��������

    for i in range(0,width):#ÿ��ÿ�е���Ѱ�������
        for j in range(0,height):
            if (data[i,j] > 0):#�������������ĳ�����
                x = data[i,j]#�������
                if (i <= top[x]):#���Ŀǰ���رȵ�ǰ�ϱ߾�С�����޸��ϱ߾�
                    top[x] = i
                if (i >= botton[x]):#���Ŀǰ���رȵ�ǰ�±߾�����޸��±߾�
                    botton[x] = i
                if (j <= left[x]):#���Ŀǰ���رȵ�ǰ��߾�С�����޸���߾�
                    left[x] = j
                if (j >= I[x]):#���Ŀǰ���رȵ�ǰ�ұ߾�����޸��ұ߾�
                    I[x] = j

    center_x = (I + left) / 2#��ø���Ĵ�ֱ��������
    center_y = (top+botton)/2#��ø����ˮƽ��������
    high = botton - top#��ø���ĸ߶�
    true_high = high*3/2#���Ը߶ȱ�������ֹ���ֳ���ͼƬ
    top=center_y - true_high/2#���޸ĺ�ĸ߶�Ϊ�߳���������С��Ϊ������
    botton=center_y + true_high/2#�޸��������µı߾�ֵ
    left = center_x - true_high / 2
    I = center_x + true_high / 2
    return top, botton, left, I#���ر߾�����
#        print i/100

countt = 0
y_r=np.array([0,8,5,6,7,4,9,1,2,3,6,7,8,9,0,4,5,3,1,2,1])
y_r6 = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,99,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,99,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,99,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9])
y_r5=np.array([99,9,3,5,6,7,8,0,2,4,1,3,5,6,0,2,7,9,1,8,4,3,5,6,4,0,2,7,8,1,9,6,5,7,3,99,8,4,2,0,1,6,4,5,8,3,7,0,2,1,6,3,5,4,2,0,1,8,9,7,5,6,3,4,8,0,2,9,7,1])
y_r2=np.array([1,4,3,4,1,2,1,9,1,6,0,4,1,5,9,9,6,3,8,2,1,3,7,5])
y_r3=np.array([99,9,1,2,1,99,5,9,3,99,4,6,2,9,99])
def test(left, top, right, botton, Class, im):#�иʶ��
    for i in range(1,Class):#Class��ͼƬ�е���������
        i1 = bytes(i+1)#����ת�ַ���
        left1 = bytes(left[i])
        top1 = bytes(top[i])
        right1 = bytes(right[i])
        botton1 = bytes(botton[i])

        box = (left[i], top[i], right[i], botton[i])
        region = im.crop(box)#�и�Ŀǰ���ŵ�����ͼƬ

        re = ResizeImage(region, 28, 28, type)#��ͼƬתΪ28X28���ش�С��
        re = re.convert("L")#תΪ��ͨ��ͼ
        re.save("C:/Users/BPEI/desktop/new/cut"+i1+".jpeg")#���и���ͼƬ��ΪjpegͼƬ
        width, height = re.size
        
        data = np.array(re)#�и���pillowͼת����
        data = data.flatten()#��28X28תΪ784��һά����
        new_data = np.zeros([1, 784])
        new_data[0]=data
        new_data=new_data.astype("float32")#ת����������
        new_data=new_data/255#��һ
      
        new_j = np.zeros([1,10])#������ȷ������
        for j in range(10):
            if (y_r3[i] == j):
                new_j[0, j] = 1

        new_j = new_j.astype("float32")
        saver.restore(sess, "C:/Users/BPEI/desktop/new/model.ckpt-19901")#���뱣���ѵ���õ�ģ��

        true = sess.run(tf.argmax(y_real, 1), feed_dict={x: new_data, y_real: new_j, keep_prob: 1.0})#��ʵ��ֵ
        test = sess.run(tf.argmax(y_conv, 1), feed_dict={x: new_data,y_real:new_j,keep_prob:1.0})#Ԥ���ֵ
        if(test == true):#�����ͬ ��ȷ��ֵ�ͼ�1
            countt=countt+1
        print sess.run(tf.argmax(y_real, 1), feed_dict={x: new_data, y_real: new_j, keep_prob: 1.0})#��ӡ��ʵֵ
        print sess.run(tf.argmax(y_conv, 1), feed_dict={x: new_data,y_real:new_j,keep_prob:1.0})#��ӡԤ���ֵ
        print "......."


data = [[]]
binarydata = [[]]
classform = [[]]
Class = 0
top = []
botton = []
left = []
right = []


filename = "C:/Users/BPEI/Documents/Tencent Files/670185712/FileRecv/MobileFile/mmexport1511837902518.jpg"#���ļ�
im = Image.open(filename)#��ʼ����
data = ImageToMatrix(filename)
binarydata,im = gotoBinary(filename, data)
classform, Class = CLASS(binarydata)
top, botton, left, right = SPLIT(classform, Class)
test(left, top, right, botton, Class,im)

