from db import DatabaseProcess
from Func import Func
import numpy as np
import time
import sys


class Engine:

    def __init__(self):
        self.class_func = Func()
        self.class_db = DatabaseProcess(local=True)
        self.db_features = self.class_db.load_database(field_limit=0)

    def get_feature(self, img_file):
        img_feature = self.class_func.get_inception_feature(img_file)
        return img_feature

    def compare_image(self, img_file):
        img_feature = self.get_feature(img_file)

        # --------------- find nearest feature -----------------
        min_dist = -1
        min_id = -1

        for fid in self.db_features:
            dist = np.linalg.norm(np.array(img_feature) - np.array(self.db_features[fid]))

            if min_dist == -1 or dist < min_dist:
                min_dist = dist
                min_id = fid

        # ---------------- extract field info from db ------------
        ret = self.class_db.find_id(min_id)

        return ret


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../1.jpg'

    class_engine = Engine()

    # class_engine.get_feature(filename)
    print(class_engine.compare_image(filename))
