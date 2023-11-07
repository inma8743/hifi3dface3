import tensorflow as tf

# TensorFlow가 GPU를 인식하는지 확인합니다.
gpu_device_name = tf.test.gpu_device_name()
if gpu_device_name:
    gpu_confirmation = 'Default GPU Device: {}'.format(gpu_device_name)
else:
    gpu_confirmation = "TensorFlow GPU device not found"

# 간단한 연산을 통해 GPU 사용을 확인합니다.
with tf.device('/GPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)

# cudnn이 설치되어 있는지 확인합니다.
cudnn_confirmation = tf.test.is_built_with_cuda()

# 결과 출력
gpu_confirmation, c.numpy(), cudnn_confirmation
