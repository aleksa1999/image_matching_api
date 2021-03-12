from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from setting import THRESHOLD_ACCURACY
from engine import Engine
from Func import Func
import numpy as np
import requests
import base64
import ast
import os


def img_decode_b64(img_date, img_name):
    img_out = open(img_name, 'wb')
    img_out.write(base64.b64decode(img_date))
    img_out.close()


class ImageApi(Resource):

    def __init__(self):
        pass

    def post(self):
        request_json = request.get_json()

        print("Received request!")
        req_type = request_json['type']
        req_img_file = request_json['image']
        if 'accuracy' in request_json:
            req_accuracy = float(request_json['accuracy'])
        else:
            req_accuracy = THRESHOLD_ACCURACY

        result = {}
        temp_file = 'temp_{}.jpg'.format(datetime.now()).replace(":", "-").replace(" ", "-")
        try:
            if req_type == 'get_feature_filename':
                img_feature = class_engine.get_feature(req_img_file)
                result['feature'] = str(img_feature)

            elif req_type == 'get_feature_base64':
                img_decode_b64(req_img_file, temp_file)
                img_feature = class_engine.get_feature(temp_file)
                result['feature'] = str(img_feature)

            elif req_type == 'get_feature_link':
                with open(temp_file, 'wb') as f:
                    r = requests.get(req_img_file)
                    f.write(r.content)

                if r.status_code == 200:
                    ret_match = class_engine.get_feature(temp_file)
                    result['feature'] = str(ret_match)

            elif req_type == 'match_filename':
                ret_match = class_engine.compare_image(req_img_file, acc_threshold=req_accuracy)
                result['match'] = ret_match

            elif req_type == 'match_base64':
                img_decode_b64(req_img_file, temp_file)
                ret_match = class_engine.compare_image(temp_file, acc_threshold=req_accuracy)
                result['match'] = ret_match

            elif req_type == 'match_link':
                with open(temp_file, 'wb') as f:
                    r = requests.get(req_img_file)
                    f.write(r.content)

                if r.status_code == 200:
                    ret_match = class_engine.compare_image(temp_file, acc_threshold=req_accuracy)
                    result['match'] = ret_match

            elif req_type == 'match_feature':
                field_feature = ast.literal_eval(req_img_file)
                feature_str = field_feature['result']['feature']
                feature = np.array(ast.literal_eval(feature_str))
                ret_match = class_engine.compare_feature(feature, acc_threshold=req_accuracy)
                result['match'] = ret_match

        except Exception as e:
            print(e)

        class_func.rm_file(temp_file)

        return jsonify(dict(result=result))


class_engine = Engine()
class_func = Func()

app = Flask(__name__)
api = Api(app)
api.add_resource(ImageApi, '/image_service/v1.0')


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT", 3000)),
            debug=False,
            threaded=True)
