import sys
if sys.prefix == '/home/sachinator/Desktop/ros/test/.pixi/envs/default':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sachinator/Desktop/ros/test/install/py_pubsub'
