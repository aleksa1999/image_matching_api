### Packages

        pip install opencv-python==4.2.*
        pip install tesnsorflow==1.14.*
        pip install requests
        pip install pillow
        pip install flask
        pip install flask-restful
       

### Run script

        python engine.py  filename
        
        
### Run flask server

        python flask_server.py
        
        
### Request format

- get feature request for image file name

        {
            "type": "get_feature_filename",
            "image": img_file_name
        }
        
- get feature request for base64 of image

        {
            "type": "get_feature_base64",
            "image": base64 of image
        }
        
- get feature request for image link

        {
            "type": "get_feature_link",
            "image": link of image
        }

- find match result for image file name ("accuracy" can be ignored, and then will use default value in setting.py)

        {
            "type": "match_filename",
            "accuracy": accuracy_threshold,
            "image": img_file_name
        }
        
- find match result for base64 of image ("accuracy" can be ignored, and then will use default value in setting.py)

        {
            "type": "match_base64",
            "accuracy": accuracy_threshold,
            "image": base64 of image
        }
        
- find match result for image link ("accuracy" can be ignored, and then will use default value in setting.py)

        {
            "type": "match_link",
            "accuracy": accuracy_threshold,
            "image": link of image
        }
        
- find match result for feature string ("accuracy" can be ignored, and then will use default value in setting.py)

        {
            "type": "match_feature",
            "accuracy": accuracy_threshold,
            "image": feature string
        }
        
    sample of feature stringL
        
        "{\"result\":{\"feature\":\"[0.13205051, 0.16701862, 0.18179958, 0.0, 0.32239312, ... , 0.0060263807]\"}}\n"
        