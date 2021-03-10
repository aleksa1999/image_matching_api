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
