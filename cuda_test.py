import tensorflow as tf

# Check if TensorFlow can detect the GPU
gpu_available = tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)

# Additional line to test cuDNN installation.
# This will try to load the cuDNN library and raise an error if it cannot.
cudnn_available = tf.test.is_built_with_cuda()

# Print the findings
gpu_status = 'Available' if gpu_available else 'Not available'
cudnn_status = 'Available' if cudnn_available else 'Not available'

(gpu_status, cudnn_status)