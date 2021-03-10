from Func import Func
import time
import sys


class Engine:

    def __init__(self):
        self.class_func = Func()

    def get_feature(self, img_file):
        img_feature = self.class_func.get_inception_feature(img_file)
        return img_feature


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '../1.jpg'

    class_engine = Engine()
    t1 = time.time()
    for i in range(10):
        class_engine.get_feature(filename)
        print(time.time() - t1)
        t1 = time.time()
