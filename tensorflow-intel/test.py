import os
import tensorflow as tf
os.environ["KMP_BLOCKTIME"] = "1"
os.environ["KMP_SETTINGS"] = "1"
os.environ["KMP_AFFINITY"]= "granularity=fine,verbose,compact,1,0"
os.environ["OMP_NUM_THREADS"]= "1"
config = tf.ConfigProto()
config.intra_op_parallelism_threads = 21
config.inter_op_parallelism_threads = 11
inference_sess = tf.Session(config=config)