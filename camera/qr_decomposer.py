from typing import TextIO
import qrcode
import cv2

def createQR(string):
    QRimage = qrcode.make(string)
    QRimage.save(f"{string}.png")
    return True

def decodeQR(containerQR):
    image = cv2.imread(containerQR)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
        return data
    else:
        print("There was some error")
        return None
