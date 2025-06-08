import os
from PIL import Image
from datetime import datetime
import time
import platform
import math

mainmenutext ='''-----------------------------------
 InstaResizer   |   Yusuf Acemoglu
-----------------------------------'''

def cls():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def validate_hex(hex_code):
    if hex_code.startswith("#"):
        hex_code = hex_code[1:]
    if len(hex_code) == 6:
        try:
            int(hex_code, 16)
            return True
        except ValueError:
            return False
    else:
        return False

def start_program():
    cls()
    print(mainmenutext)
    directory = os.listdir("./")
    images = []
    print("\nItems to resize:\n-----------------------------------")
    for item in directory:

        if item.split(".",)[-1].lower() in ("jpg", "png", "webp", "jpeg"):
            images.append(item)
            print(str(len(images)) + ": " + str(item))
    if len(images) > 0:
        print(f"Total number of images: {len(images)}\n-----------------------------------\nAspect Ratio Settings\n(Type any letter to quit)\n")

        try:
            aspect_x = int(input("X Aspect Ratio? : "))
            aspect_y = int(input("Y Aspect Ratio? : "))
            print(f"Total number of images: {len(images)}\n-----------------------------------\nSelect Background Color\n(Type any letter to quit)\n\n1: Black\n2: White\n3: Custom\n")
            colorselection = int(input("Selection: "))
            if colorselection == 1:
                color = "Black"
            elif colorselection == 2:
                color = "White"
            elif colorselection ==3:
                while True:
                    color = str(input("-----------------------------------\nEnter HEX code (Type 'q' to quit): ")).strip(" ")
                    if not color.startswith("#"):
                        color = "#" + str(color)

                    if not validate_hex(color):
                        if "q" in color.lower() or "e" in color.lower():
                            raise
                        print("-----------------------------------\nInvalid HEX Code.")
                    else:
                        break
                    
            else:
                raise
            quit = False
        except:
            print("-----------------------------------\nQuitting..\n-----------------------------------")
            quit = True
            time.sleep(2)

        if not quit == True:
            start_time = datetime.now()
            dirname = f"{aspect_x} by {aspect_y} resized " + str(datetime.now()).split(".")[0].replace(":", ".") 
            os.mkdir(dirname)

            for Item in images:
                img = Image.open(Item)
                #img_resized = img.resize((13aspect_x0, 3212), Image.Resampling.LANCZOS)
                imgsize= img.size
                imgsize_x= imgsize[0]
                imgsize_y= imgsize[1]

                if imgsize_x > imgsize_y:
                    #yatay
                    print("-----------------------------------")
                    Mode = "Horizontal"
                    new_y = int(imgsize_x / aspect_x * aspect_y)
                    new_x = imgsize_x
                    if not new_y < imgsize_y:
                        newres = (new_x, new_y)
                        #print(f"1 -- : {newres}")
                        Method = "1"
                    else:
                        new_x = int(imgsize_y / aspect_y * aspect_x)
                        new_y = imgsize_y
                        newres = (new_x, new_y)
                        Method = "2"

                elif imgsize_x < imgsize_y:
                    #dikey
                    print("-----------------------------------")
                    Mode = "Vertical"
                    new_x = int(imgsize_y / aspect_y * aspect_x)
                    new_y = imgsize_y
                    if not new_x < imgsize_x:
                        newres = (new_x, new_y)
                        Method = "1"
                    else:
                        new_y = int(imgsize_x / aspect_x * aspect_y)
                        new_x = imgsize_x
                        newres = (new_x, new_y)
                        Method = "2"

                else:
                    print("-----------------------------------")
                    #kare
                    #print("kare")
                    Mode = "Square"

                    if aspect_x > aspect_y:
                        new_x = int(imgsize_x / aspect_y * aspect_x)
                        new_y = imgsize_y
                        Method = 3
                    else:
                        new_y = int(imgsize_y / aspect_x * aspect_y)
                        new_x = imgsize_x
                        Method = 4

                    newres = (new_x, new_y)

                if Item.lower().endswith(".jpg") or Item.lower().endswith(".jpeg"):
                    rgbmode= "RGB"
                else:
                    rgbmode = "RGBA"


                background = Image.new(rgbmode, newres, color)
                newpos = (int((new_x / 2) - (imgsize_x / 2 )), int((new_y / 2) - (imgsize_y / 2 )))

                background.paste(img, newpos)
                background.save(f"./{dirname}/{aspect_x} by {aspect_y} resized {Item}")
                gcdd= math.gcd(imgsize_x, imgsize_y)
                print(f"Item: {Item}\nOrientation: {Mode}\nMethod: {Method}")
                print("Original Resolution: " + f"{imgsize_x} x {imgsize_y}")
                print(f"Original Aspect Ratio: {int(imgsize_x / gcdd)}:{int(imgsize_y / gcdd)}")
                print("New Resolution: " + f"{newres[0]} x {newres[1]}")
                print(f"New Aspect Ratio: {aspect_x}:{aspect_y}")
                print('Position: '+ f"{newpos[0]} x {newpos[1]}")



            print("-----------------------------------")
            Elapsed = datetime.now() - start_time
            print(f"{len(images)} Images were resized and saved.\nSelected Aspect Ratio: {aspect_x}:{aspect_y}\nSelected Background Color: {color}\nFolder Name: {dirname}\nTime Elapsed: {Elapsed}")
            print("-----------------------------------")
            mainmenudialog = str(input("Press enter to go back to the main menu, type q to quit. : "))
            if "q" in mainmenudialog or "e" in mainmenudialog:
                print("-----------------------------------\nQuitting..\n-----------------------------------")
                quit = True
                time.sleep(2)
            else:
                cls()
                start_program()
    else:
        print("No compatible images found in the same directory as the program.\nPlease put images in the same folder as this executable and try again.\nTo scan this directory again, press Enter. To quit, type 'q'\n-----------------------------------")
        rescan = str(input()).lower()
        if "q" in rescan:
            print("-----------------------------------\nQuitting..\n-----------------------------------")
            time.sleep(2)
        else:
            cls()
            print("-----------------------------------\nScanning..\n-----------------------------------")
            time.sleep(1)
            start_program()
start_program()

#yusuf acemoglu