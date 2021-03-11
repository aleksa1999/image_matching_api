import requests
import base64
import json
import sys


def make_request_get_feature_img_filename(img_file_name):
    json_data = {
        "type": "get_feature_filename",
        "image": img_file_name
    }
    return json_data


def make_request_get_feature_img_base64(img_file):
    file_data = open(img_file, 'rb')
    json_data = {
        "type": "get_feature_base64",
        "image": base64.b64encode(file_data.read()).decode('UTF-8')
    }
    return json_data


def make_request_get_feature_img_link(img_file_name):
    json_data = {
        "type": "get_feature_link",
        "image": img_file_name
    }
    return json_data


def make_request_match_img_filename(img_file_name):
    json_data = {
        "type": "match_filename",
        "image": img_file_name
    }
    return json_data


def make_request_match_img_base64(img_file):
    file_data = open(img_file, 'rb')
    json_data = {
        "type": "match_base64",
        "image": base64.b64encode(file_data.read()).decode('UTF-8')
    }
    return json_data


def make_request_match_img_link(img_file_name):
    json_data = {
        "type": "match_link",
        "image": img_file_name
    }
    return json_data


def send_request(server, req_json):
    response = requests.post(url=server, json=req_json)
    print("Server responded with %s" % response.status_code)

    response_json = response.json()
    return response_json


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        # filename = '../1.png'
        filename = 'https://asset.conrad.com/media10/isa/160267/c1/-/en/301550_BB_00_FB/image?x=400&y=400&ex=400&ey=400&align=center&format=jpg'

    url_server = 'http://localhost:3000/image_service/v1.0'
    # url_server = 'http://149.202.76.203:3000/image_service/v1.0'

    # json_request = make_request_get_feature_img_filename(filename)
    # json_request = make_request_get_feature_img_base64(filename)
    # json_request = make_request_get_feature_img_link(filename)
    # json_request = make_request_match_img_filename(filename)
    # json_request = make_request_match_img_base64(filename)
    json_request = make_request_match_img_link(filename)

    ret_response = send_request(url_server, json_request)

    print(json.dumps(ret_response, indent=4))
