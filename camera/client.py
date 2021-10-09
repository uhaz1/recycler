import base64
import json                    
from storing_information import api
import requests

def sendImages(imagesArray, containerId, actualTimeString):
    decodedImagesArray = []
    
    for imageName in imagesArray:
        with open(imageName, "rb") as f:
            im_bytes = f.read()
        im_b64 = base64.b64encode(im_bytes).decode("utf8")
        decodedImagesArray.append(im_b64)

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = json.dumps({"images" : decodedImagesArray, "containerId" : containerId, "actualTimeString" : actualTimeString})

    response = requests.post(api, data=payload, headers=headers)
    try:
        data = response.json()     
        print(data)
        return data
    except requests.exceptions.RequestException:
        print(response.text)
        return response.text