from picamera import PiCamera
from time import sleep
from storing_information import savePath
from qr_decomposer import decodeQR
import datetime 


def takePictures():
    actualTime = datetime.datetime.now()
    actualTimeString = actualTime.strftime("%d_%m_%Y_%H_%M_%S")[:-4]
    qrCapture = savePath + f"container_QR_code_{actualTimeString}.jpeg"

    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    camera.capture(qrCapture)
    containerId = decodeQR(qrCapture)
    sleep(2)

    imagesNames = []
    for idx in range(1):
        sleep(2)
        imageName = savePath + f"image{idx}_{containerId}_{actualTimeString}.jpeg"
        camera.capture(imageName)
        imagesNames.append(imageName)

    camera.stop_preview()
    return imagesNames, containerId, actualTimeString


if  __name__ == '__main__':
    takePictures()
