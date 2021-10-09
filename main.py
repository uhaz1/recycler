import cameraPi
import client

if __name__ == "__main__":
    imagesNames, containerId, actualTimeString = cameraPi.takePictures()
    client.sendImages(imagesNames, containerId, actualTimeString)