# importing the python open cv library
import cv2
import numpy as np
import pytesseract as pyt
import os
from PIL import Image
pyt.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"


def main():
    # get_pictures()
    get_instructions()

def get_pictures():
    # intialize the webcam and pass a constant which is 0
    cam = cv2.VideoCapture(0)
    # title of the app
    cv2.namedWindow('python webcam screenshot app')
    # let's assume the number of images gotten is 0
    img_counter = 0
    # while loop
    while True:
        # intializing the frame, ret
        ret, frame = cam.read()
        # if statement
        if not ret:
            print('failed to grab frame')
            break
        # the frame will show with the title of test
        cv2.imshow('test', frame)
        # to get continuous live video feed from my laptops webcam
        k = cv2.waitKey(1)
        # if the escape key is been pressed, the app will stop
        if k % 256 == 27:
            print('escape hit, closing the app')
            break
        # if the spacebar key is been pressed
        # screenshots will be taken
        elif k % 256 == 32:
            # the format for storing the images scrreenshotted
            img_name = f'images/opencv_frame_{img_counter}.png'
            # saves the image as a png file
            cv2.imwrite(img_name, frame)
            print('screenshot taken')
            # the number of images automaticallly increases by 1
            img_counter += 1
    # release the camera
    cam.release()
    # stops the camera window
    cv2.destroyAllWindows()


def get_instructions():
    directory = "images"
    for filename in os.listdir(directory):
        im = Image.open(directory + "/" + filename)
        ret, img = cv2.threshold(np.array(im), 125, 255, cv2.THRESH_BINARY)
        text = pyt.image_to_string(im)
        if text == "":
            print("Couldn't read the text.")
        else:
          print(text)

def parse_text(sentence):
    inst_arr = sentence.split()



if __name__ == "__main__":
    main()
