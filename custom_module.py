import tensorflow as tf

def jaccard_loss(y_true, y_pred, smooth=1e-6):
    intersection = tf.reduce_sum(y_true * y_pred, axis=[1, 2, 3])
    sum_ = tf.reduce_sum(y_true + y_pred, axis=[1, 2, 3])
    jac = (intersection + smooth) / (sum_ - intersection + smooth)
    return 1 - jac
