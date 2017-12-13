#utf-8
import tensorflow as tf
import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)#����minist���ݼ�
sess = tf.InteractiveSession()

x = tf.placeholder("float", shape=[None, 784])#x��ռλ������ʾ����ͼƬ��������ʽ����״Ϊ[None,784]����һλ��ͼƬ������784��������
y_real = tf.placeholder("float", shape=[None, 10])#y_real��ռλ������ʾͼƬ������ʵ���֣���״Ϊ[None,10]����һλ��ͼƬ�������ڶ�λ��ȷ������Ϊ�±��ֵΪ1������Ϊ0


def weight_variable(shape):#����WȨ�أ���ʼ��Ϊ��̬�ֲ�
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):#����bƫ��������ʼ��Ϊ0
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):#�������㣬x������������W�Ǿ���ˣ�����Ϊ1��û�б߾�
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):#����ػ��㣬ģ��Ϊ2X2������Ϊ2��û�б߾�
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')
#��һ������
W_conv1 = weight_variable([5, 5, 1, 32])#��һ�����ˣ�32��5X5�ľ����
b_conv1 = bias_variable([32])#��һ��ƫ������32������

x_image = tf.reshape(x, [-1,28,28,1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)#��һ�㼤����
h_pool1 = max_pool_2x2(h_conv1)#��һ��ػ���
#�ڶ�������
W_conv2 = weight_variable([5, 5, 32, 64])#�ڶ������ˣ�5X5X32 64��
b_conv2 = bias_variable([64])#�ڶ���ƫ������64������

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)#�ڶ��㼤����
h_pool2 = max_pool_2x2(h_conv2)#�ڶ���ػ���
#��ȫ��
W_fc1 = weight_variable([7 * 7 * 64, 1024])#��ȫ���Ȩ��
b_fc1 = bias_variable([1024])#��ȫ���ƫ����

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)#����

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#�ڶ�����ȫ�㣬תΪ���10������
W_fc2 = weight_variable([1024, 10])#Ȩ��
b_fc2 = bias_variable([10])#ƫ����

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)#����������������Ϊ10��������ȡ��ÿ�����ֵĸ��ʡ�softmaxʹ����Ϊ0-1֮�䡣

cross_entropy = -tf.reduce_sum(y_real*tf.log(y_conv))#��ʧ������������=y_real*log(y_cov)
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)#ѵ�����̣���AdamOptimizer���Ż����̷����Ż�����
correct_prediction = tf.equal(tf.argmax(y_realconv,1), tf.argmax(y_real,1))#ȡ�������ֵ���±�Ƚϣ�Ԥ���Ƿ���ȷ������true����ȷ������false�����
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))#��correct_predictionת��Ϊ����������ȷΪ1������Ϊ0

sess.run(tf.initialize_all_variables())#��ʼ�����в��� 
#��ʼѵ�����ұ���ѵ�����ģ��
saver = tf.train.Saver()
for i in range(20000):
    batch_xs, batch_ys = mnist.train.next_batch(25)#��25��Ϊһ��ȡmnist����
    sess.run(train_step, feed_dict={x: batch_xs, y_real: batch_ys, keep_prob: 0.5})#ѵ��
    if i % 100 == 0:
        saver.save(sess, 'C:/Users/BPEI/desktop/new/model.ckpt', global_step=i + 1)
        print i/100