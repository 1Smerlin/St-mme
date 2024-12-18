import os
import time
import json
from PIL import Image
import pyautogui as pg
import keyboard

# >>> Variablen

image_folder = "./img/"

triger_file = "./triger.json"

run = True


def stop():
    global run
    run = False


# >>> keyboard
keyboard.add_hotkey("esc", stop)


# >>> Image
def get_image_center(image_path):
    with Image.open(image_path) as img:
        width, height = img.size  # Breite und Höhe des Bildes
        # x_center = width // 2  # Horizontale Mitte
        x_center = 5
        y_center = height // 2  # Vertikale Mitte
        return (x_center, y_center)


# def checkNettle(item_name, image_name):
#     image_path = image_folder + item_name + "/" + image_name
#     if os.path.exists(image_path):
#         try:
#             pos = pg.locateOnScreen(image_path, confidence=0.75)
#             center = get_image_center(image_path)
#             pg.moveTo(pos.left + center[0], pos.top + center[1])
#             pg.click()
#             print(f"left: {pos.left} top: {pos.top}")
#             print(f"Klick auf Bild: {image_path} an Position: {pos}")
#             time.sleep(10)
#         except Exception as e:
#             print(f"{image_path} nicht gefunden.")
#             # print(f"Fehler bei der Bildsuche: {e}")
#     else:
#         print("path not exist")


# while run:
#     for search_number in search_item:
#         item_name = item_list[search_number]
#         image_list = [file for file in os.listdir(f"{image_folder}{item_name}") if os.path.isfile(os.path.join(f"{image_folder}{item_name}", file))]
#         for image_name in image_list:
#             checkNettle(item_name, image_name)
#             if not run:
#                 break
#         print(f"{item_name} Search Finish")


def checkNettle(image_name):
    image_path = image_folder + image_name
    if os.path.exists(image_path):
        try:
            pos = pg.locateOnScreen(image_path, confidence=0.8)
            center = get_image_center(image_path)
            pg.moveTo(pos.left + center[0], pos.top + center[1])
            pg.click()
            print(f"left: {pos.left} top: {pos.top}")
            print(f"Klick auf Bild: {image_path} an Position: {pos}")
            # time.sleep(10)
        except Exception as e:
            print(f"{image_path} nicht gefunden.")
            # print(f"Fehler bei der Bildsuche: {e}")
    else:
        print("path not exist")


checkNettle("axt.png")
# axt.png
# leicht.png
# paladin.png
# schwer.png
# schwert.png
# speer.png
