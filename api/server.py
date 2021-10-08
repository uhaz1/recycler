import io                    
import base64                  
import logging
from PIL import Image

from flask import Flask, request, abort

app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)

@app.route("/test", methods=['POST'])
def test_method():     
    if not request.json or 'images' not in request.json or 'containerId' not in request.json or 'actualTimeString' not in request.json: 
        abort(400)
             
    im_b64 = request.json['images']
    containerId = request.json['containerId']
    actualTimeString = request.json['actualTimeString']

    # convert it into bytes
    for idx in range(len(im_b64)):
        element = im_b64[idx]
        img_bytes = base64.b64decode(element.encode('utf-8'))
        img = Image.open(io.BytesIO(img_bytes))
        filename = f"{containerId}_{actualTimeString}_{idx}"
        img.save(f"{filename}.jpeg")

    result_dict = {'output': 'output_key'}
    return result_dict
  
def run_server_api():
    app.run(host='0.0.0.0', port=8080)
  
if __name__ == "__main__":     
    run_server_api()