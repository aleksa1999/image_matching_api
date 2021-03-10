from tensorflow.python.platform import gfile
import tensorflow as tf
import numpy as np
import os


class Func:

    def __init__(self):
        self.sess_inc = self.create_graph_inc('model/inception.pb')
        self.next_to_last_tensor = self.sess_inc.graph.get_tensor_by_name('pool_3:0')

    @staticmethod
    def get_file_list(root_dir):
        """
            get all files in root_dir directory
        """
        path_list = []
        file_list = []
        join_list = []
        for path, _, files in os.walk(root_dir):
            for name in files:
                path_list.append(path)
                file_list.append(name)
                join_list.append(os.path.join(path, name))

        return path_list, file_list, join_list

    @staticmethod
    def rm_file(filename):
        if os.path.isfile(filename):
            os.remove(filename)

    @staticmethod
    def get_ext(filename):
        return filename.split(".")[-1].upper()

    @staticmethod
    def remove_duplicate(list_data):
        return list(set(list_data))

    def get_inception_feature(self, jpg_name):
        img_file = gfile.FastGFile(jpg_name, 'rb').read()
        feature_org = self.sess_inc.run(self.next_to_last_tensor, {'DecodeJpeg/contents:0': img_file})
        feature = np.squeeze(feature_org)
        return list(feature)

    @staticmethod
    def create_graph_inc(model_name):
        tf.reset_default_graph()
        with gfile.FastGFile(model_name, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')
            session = tf.Session()

        return session
