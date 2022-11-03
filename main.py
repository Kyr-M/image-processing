import os
from urllib.error import URLError
from urllib.request import Request, urlopen

import cv2
import urllib
import numpy as np


def switch(v): yield lambda *c: v in c


loop = True
imgs = []


def image_url():
    url = input("enter image URL...\n")
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print("We failed to load the URL image")
            print("Reason", e.reason)
        elif hasattr(e, 'code'):
            print("We failed to load the URL image")
            print("Error code", e.code)
    else:
        print("URL image of good, loading.....")
        url_response = urllib.request.urlopen(url)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        cv2.imshow('URL Image', img)
        cv2.waitKey(0)
        save_image = input("do you want to save the image as .JPG? Yes/No\n")

        if ((save_image == "yes") or (save_image == "Yes")):
            filename = input("save image as...\n")
            cv2.imwrite(filename, img)
        else:
            cv2.destroyAllWindows()


def grey_scale():
    while True:
        print("================     GreyScale Image    ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            img_edit_final = cv2.cvtColor(image_edit, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Grey Scale Image', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def noise_reduce():
    while True:
        print("================     Reduce Noise Image    ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            img_edit_final = cv2.fastNlMeansDenoisingColored(image_edit, None, 20, 10, 7, 21)
            cv2.imshow('Reduce Noise Image', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def add_blur():
    while True:
        print("================     Add Blur Noise Image    ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            img_edit_final = cv2.GaussianBlur(image_edit, (25, 25), 0)
            cv2.imshow('GaussianBlur Image', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def add_canny_filter():
    while True:
        print("================     Add Canny Edge filter Image   ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            # Setting parameter values
            t_lower = 50  # Lower Threshold
            t_upper = 150  # Upper threshold
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            img_edit_final = cv2.Canny(image_edit, t_lower, t_upper)
            cv2.imshow('Canny Edge filter', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def detect_face():
    while True:
        print("================  Detect Face  ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            model = cv2.CascadeClassifier(
                r"C:\Users\kmichailidis\PycharmProjects\Image_process\haarcascade_frontalface_default.xml")
            img_edit_final = model.detectMultiScale(image_edit)
            for x, y, width, height in img_edit_final:
                img_edit_final = cv2.rectangle(image_edit, (x, y), (x + width, y + height), (0, 255, 255), 2)
            cv2.imshow('Detect Face', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, image_edit)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def resize_img():
    while True:
        print("================  resize image   ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            # Setting parameter values
            new_width = int(input("give new Width\n"))
            new_height = int(input("give new Height\n"))
            img_edit_final = cv2.resize(image_edit, (new_width, new_height))
            cv2.imshow('image resize', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")


def img2sketch(k_size):
    while True:
        print("================  Sketch Noise Image  ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)
            # Convert to Grey Image
            grey_img = cv2.cvtColor(image_edit, cv2.COLOR_BGR2GRAY)

            # Invert Image
            invert_img = cv2.bitwise_not(grey_img)
            # invert_img=255-grey_img

            # Blur image
            blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), 0)

            # Invert Blurred Image
            invblur_img = cv2.bitwise_not(blur_img)
            # invblur_img=255-blur_img

            # Sketch Image
            img_edit_final = cv2.divide(grey_img, invblur_img, scale=256.0)
            # Display sketch
            cv2.imshow('sketch image', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")

def cartoon_img():
    while True:
        print("================  resize image   ======================")
        file = input("Input filename or q to exit>>> ")
        if file == "q":
            break
        if os.path.exists(file):
            image_edit = cv2.imread(file)
            imgs.append(image_edit)

            # Edges
            gray = cv2.cvtColor(image_edit, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 9, 9)

            # Cartoonization
            color = cv2.bilateralFilter(image_edit, 9, 250, 250)
            img_edit_final = cv2.bitwise_and(color, color, mask=edges)

            cv2.imshow('image resize', img_edit_final)
            cv2.waitKey(0)
            save_image_grey = input("do you want to save the image as .JPG? Yes/No\n")
            if ((save_image_grey == "yes") or (save_image_grey == "Yes")):
                filename = input("save image as...\n")
                cv2.imwrite(filename, img_edit_final)
            else:
                cv2.destroyAllWindows()
        else:
            print("File not found.")



while (loop):

    print("===================================================")
    print("================     Menu    ======================")
    print("===================================================")
    print("1)  load image from URL and save it on your pc.....")
    print("2)  edit your images and make them GreyScale       ")
    print("3)  edit your images and reduce noise              ")
    print("4)  edit your images and add blur                  ")
    print("5)  edit your images and add Canny Edge filter     ")
    print("6)  Detect Face from image                         ")
    print("7)  resize image                                   ")
    print("8)  sketch image                                   ")
    print("9)  Cartoonifying image                            ")
    print("0)                  Exit                           ")
    print("===================================================")

    menu = int(input("Choose from Menu above...\n"))
    for case in switch(menu):
        if case(1):
            image_url()
        elif case(2):
            grey_scale()
        elif case(3):
            noise_reduce()
        elif case(4):
            add_blur()
        elif case(5):
            add_canny_filter()
        elif case(6):
            detect_face()
        elif case(7):
            resize_img()
        elif case(8):
            img2sketch(k_size=7)
        elif case(9):
            cartoon_img()
        elif case(0):
            exit()
        else:
            print("Choose something from the menu\n")
