import tensorflow as tf

# TensorFlow가 GPU를 인식하는지 확인합니다.
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("TensorFlow GPU device not found")

# 간단한 연산을 통해 GPU 사용을 확인합니다.
with tf.device('/GPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)

print(c)