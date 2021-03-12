from db import DatabaseProcess
from Func import Func
import numpy as np
import json
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

    def compare_feature(self, feature, acc_threshold):
        # ------------ find the match result --------------
        info_list = []
        acc_list = []

        for fid in self.db_features:
            dist = np.linalg.norm(feature - self.db_features[fid])
            acc = max(0, 1 - dist / 50)

            if acc >= acc_threshold:
                ret_field = self.class_db.find_id(fid)
                ret_field['accuracy'] = acc

                acc_list.append(acc)
                info_list.append(ret_field)

        # ---------------- sort result -----------------
        result = {}
        while len(acc_list) > 0:
            max_ind = int(np.argmax(acc_list))
            result[len(result) + 1] = info_list[max_ind]
            acc_list.pop(max_ind)
            info_list.pop(max_ind)

        return result

    def compare_image(self, img_file, acc_threshold):
        img_feature = self.get_feature(img_file)
        img_feature = np.array(img_feature)

        return self.compare_feature(img_feature, acc_threshold)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../1.jpg'

    class_engine = Engine()

    # class_engine.get_feature(filename)
    print(json.dumps(class_engine.compare_image(filename, acc_threshold=0.8), indent=4))
