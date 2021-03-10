from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from engine import Engine
import base64
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

        result = {}
        if req_type == 'get_feature_filename':
            img_feature = class_engine.get_feature(req_img_file)
            result['feature'] = str(img_feature)
        elif req_type == 'get_feature_base64':
            temp_file = 'temp_{}.jpg'.format(datetime.now()).replace(":", "-").replace(" ", "-")
            img_decode_b64(req_img_file, temp_file)
            img_feature = class_engine.get_feature(temp_file)
            result['feature'] = str(img_feature)
            os.remove(temp_file)

        return jsonify(dict(result=result))


class_engine = Engine()

app = Flask(__name__)
api = Api(app)
api.add_resource(ImageApi, '/image_service/v1.0')


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT", 3000)),
            debug=False,
            threaded=True)
