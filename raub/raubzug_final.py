#
# >>> >S Notic
# > Pro Rohstoff Packet
# Legende
#  : Rohst. : p  : r  :  a  : l  : s  : pl
# 1:  40    :
# 2: 100    : 48 : 80 : 120 : 15 : 24 : 12
# 3: 200    :
# 4: 300    :

# > Pro Rohstoff
# Legende
#  : Rohst. : p  : r  :  a  : l  : s  : pl
# 1: 0.4  :
# 2: 1    : 0.48 : 0.8 : 1.2 : 0.15 : 0.24 : 0.12
# 3: 2    :
# 4: 3    :

# > Packet relati zu 1
# Legende
#  : Rohst. : p   :  r  :  a  : l    : s  : pl
# 1: 100    : 120 : 200 : 300 : 37.5 : 60 : 30
# 2: 250    :
# 3: 500    :
# 4: 750    :

# > r.1 Pro Rohstoff
# Legende
#  : Rohst. : p   : r : a : l     : s   : pl
# 1: 1      : 1.2 : 2 : 3 : 0.375 : 0.6 : 0.3
# 2: 2.5    :
# 3: 5      :
# 4: 7.5    :

# > Pro Mann
# Legende
#  : Raub. : p       :  r  : a      : l      : s      : pl
# 1: 1     : 0.83... : 0.5 : 0.3... : 2.6... : 1.6... : 3.3...
# 2: 2     :
# 3: 3     :
# 4: 4     :


# > Größe
#  : Rohst. : a : r : p   : s   : l     : pl
# 1: 1      : 3 : 2 : 1.2 : 0.6 : 0.375 : 0.3

# > Kosten
#           :130:130: 90  : 950 : 475   : 80


# >>> !>S Notic


# >>> >S modul
import pyautogui
import time
import json
import numpy as np
import multiprocessing
import time
import keyboard

# >>> !>S modul
# >>> >S variable

trup = {
    "p": {
        "Spitz_name": "picke",
        "name": "Speerträger",
        "pro_Roh": 1.2,
    },
    "r": {
        "Spitz_name": "Ritter",
        "name": "Schwertkämpfer",
        "pro_Roh": 2,
    },
    "a": {
        "Spitz_name": "Axt",
        "name": "Axtkämpfer",
        "pro_Roh": 3,
    },
    "l": {
        "Spitz_name": "leicht",
        "name": "leichte Kavallerie",
        "pro_Roh": 0.375,
    },
    "s": {
        "Spitz_name": "schwer",
        "name": "schwere Kavallerie",
        "pro_Roh": 0.6,
    },
    "pl": {
        "Spitz_name": "Paladin",
        "name": "Paladin",
        "pro_Roh": 0.3,
    },
}
raub = {
    "1": {
        "sum": 0,
        "skal": 1,
        "trup": {
            "p": 0,
            "r": 0,
            "a": 0,
            "l": 0,
            "s": 0,
            "pl": 0,
        },
    },
    "2": {
        "sum": 0,
        "skal": 2.5,
        "trup": {
            "p": 0,
            "r": 0,
            "a": 0,
            "l": 0,
            "s": 0,
            "pl": 0,
        },
    },
    "3": {
        "sum": 0,
        "skal": 5,
        "trup": {
            "p": 0,
            "r": 0,
            "a": 0,
            "l": 0,
            "s": 0,
            "pl": 0,
        },
    },
    "4": {
        "sum": 0,
        "skal": 7.5,
        "trup": {
            "p": 0,
            "r": 0,
            "a": 0,
            "l": 0,
            "s": 0,
            "pl": 0,
        },
    },
}


resurce_time = {
    100: {"h": 0, "m": 52, "s": 27},
    200: {"h": 1, "m": 11, "s": 54},
    300: {"h": 1, "m": 30, "s": 21},
    400: {"h": 1, "m": 48, "s": 11},
    500: {"h": 2, "m": 5, "s": 34},
    600: {"h": 2, "m": 22, "s": 37},
    700: {"h": 2, "m": 39, "s": 22},
    800: {"h": 2, "m": 55, "s": 54},
    900: {"h": 3, "m": 12, "s": 13},
    1000: {"h": 3, "m": 28, "s": 21},
    1100: {"h": 3, "m": 44, "s": 19},
    1500: {"h": 4, "m": 46, "s": 53},
    5000: {"h": 13, "m": 9, "s": 9},
    8000: {"h": 19, "m": 48, "s": 53},
    10000: {"h": 24, "m": 6, "s": 38},
    15000: {"h": 34, "m": 30, "s": 31},
}


# >>> !>S variable
# >>> >S Functions


# >>> >S logik


# >> Time
def convert_s(zeit_obj):
    seconds = zeit_obj["h"] * 3600 + zeit_obj["m"] * 60 + zeit_obj["s"]
    return seconds


# >>> !>S logik


# >> Read Time Function
def read_s(stoff_menge):
    zeit_obj = resurce_time[stoff_menge]
    seconds = convert_s(zeit_obj)
    return seconds


def read_func(resurce_time):
    rohstoffe = np.array([stoff_key for stoff_key in resurce_time])  # Rohstoffmengen

    zeiten = np.array([read_s(stoff_key) for stoff_key in resurce_time])

    # Polynomiale Regression 2. Grades (quadratische Funktion)
    koeffizienten = np.polyfit(rohstoffe, zeiten, 10)  # a, b, c für ax^2 + bx + c
    funktion = np.poly1d(koeffizienten)
    return funktion


funktion = read_func(resurce_time)


def time_for_resurce(rohstoffe, funktion):
    sekunden = funktion(rohstoffe)
    h = int(sekunden // 3600)
    m = int((sekunden % 3600) // 60)
    s = int(sekunden % 60)
    return {"h": h, "m": m, "s": s}


def print_time(stoff_menge):
    zeit_test = time_for_resurce(stoff_menge, funktion)

    def time_in_string(time_dic):
        return f"{time_dic['h']} Stunden, {time_dic['m']} Minuten, {time_dic['s']} Sekunden"

    new_time_string = time_in_string(zeit_test)

    print(f"{stoff_menge} Rohstoffe:")
    print(f"new_time: {new_time_string}")
    if stoff_menge in resurce_time:
        new_time = convert_s(zeit_test)
        old_time = read_s(stoff_menge)
        old_time_string = time_in_string(resurce_time[stoff_menge])
        if new_time > old_time:
            deferent = new_time - old_time
            print(f"new_time ist {deferent} Größer")
            print(f"old_time: {old_time_string}")
        elif new_time < old_time:
            deferent = old_time - new_time
            print(f"old_time ist {deferent} Größer")
            print(f"old_time: {old_time_string}")
        else:
            print(f"old_time: {old_time_string}")
            print(f"new_time und old_time sind gleich Größ")


def resurce_h(stoff_menge):
    seconds = read_s(stoff_menge)
    pro_stoff = stoff_menge / seconds * 3600
    print(f"Bei {stoff_menge} ist umsatz {pro_stoff} pro Stunde")


# >> Use Time Function


# >> Raub


def find_next_raub(raub):
    # Initialisiere den kleinsten Raubzug
    geringster_raub = None
    geringste_summe = float("inf")

    # Iteriere über die Raubzüge
    for key, value in raub.items():
        if value["sum"] < geringste_summe:
            geringster_raub = key
            geringste_summe = value["sum"]
        elif value["sum"] == geringste_summe:
            # Falls Gleichstand, nimm den mit der kleineren Zahl
            if int(key) < int(geringster_raub):
                geringster_raub = key

    return geringster_raub


# >> sum


def sum_all_raub():
    for raub_key in raub:
        raub[raub_key]["sum"] = 0
        for trup_key in raub[raub_key]["trup"]:
            if raub[raub_key]["trup"][trup_key] > 0:
                raub[raub_key]["sum"] += raub[raub_key]["trup"][trup_key] / trup[trup_key]["pro_Roh"] * raub[raub_key]["skal"]


# >> Trup


def all_roh():
    return (p / trup["p"]["pro_Roh"]) + (r / trup["r"]["pro_Roh"]) + (a / trup["a"]["pro_Roh"]) + (l / trup["l"]["pro_Roh"]) + (s / trup["s"]["pro_Roh"]) + (pl / trup["pl"]["pro_Roh"])


def add_trup(p, r, a, l, s, pl):
    all_trup = {"p": p, "r": r, "a": a, "l": l, "s": s, "pl": pl}
    trup_series = ["pl", "l", "s", "p", "r", "a"]
    for trup_key in trup_series:
        for i in range(all_trup[trup_key]):
            next_raub = find_next_raub(raub)
            raub[next_raub]["trup"][trup_key] += 1
            sum_all_raub()


# >> Ausgabe


def print_resurce(more=None):
    gesammt = 0
    big_resurce = 0
    for raub_key in raub:
        resurce = raub[raub_key]["sum"]
        print("Raub: ", raub_key)
        print("sum: ", resurce)
        gesammt += resurce
        if big_resurce < resurce:
            big_resurce = resurce
        print("gesammt: ", gesammt)
        if more:
            for trup_key in raub[raub_key]["trup"]:
                print(f"{trup_key}: ", raub[raub_key]["trup"][trup_key])
    new_time = time_for_resurce(big_resurce, funktion)
    print(f"Time: ", new_time)
    print(f"Time Second: ", convert_s(new_time))
    print(f"Gesammt Summe: ", gesammt)
    print(f"pro Stunde: ", gesammt / convert_s(new_time) * 3600)
    print(f"Biggest Summe: ", big_resurce)
    print(f"Biggest pro Stunde: ", big_resurce / convert_s(new_time) * 3600)


# >>> !>S Functions

# >>> >S Bot


def klick_und_eingabe(x, y, zahl):
    # Maus zur angegebenen Position bewegen und klicken
    pyautogui.moveTo(x, y, duration=0.5)  # Optional: duration für sanfte Bewegung
    pyautogui.click()

    # Kurze Verzögerung, um sicherzustellen, dass das Eingabefeld fokussiert ist
    time.sleep(0.2)

    # Zahl eingeben
    pyautogui.typewrite(str(zahl), interval=0.1)  # Optional: interval für Tippen-Verzögerung


def click_to(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


def send_all_trup(coordinat):
    for raub_key in raub:
        for trup_key in raub[raub_key]["trup"]:
            if raub[raub_key]["trup"][trup_key] > 0:
                klick_und_eingabe(coordinat["trup"][trup_key]["x"], coordinat["trup"][trup_key]["y"], raub[raub_key]["trup"][trup_key])

        click_to(coordinat["raub"][raub_key]["x"], coordinat["raub"][raub_key]["y"])


# >>> !>S Bot
# >>> >S main


# >> 1 coordinat
coordinat = {
    "vorlage": {
        "trup": {
            "p": {
                "x": 0,
                "y": 0,
            },
            # x 86
            "r": {
                "x": 0 + 86,
                "y": 0,
            },
            # x 91
            "a": {
                "x": 0 + 86 + 91,
                "y": 0,
            },
            # x 89
            "l": {
                "x": 0 + 86 + 91 + 89,
                "y": 0,
            },
            # x 88
            "s": {
                "x": 0 + 86 + 91 + 89 + 88,
                "y": 0,
            },
            # x 87
            "pl": {
                "x": 0 + 86 + 91 + 89 + 88 + 87,
                "y": 0,
            },
        },
        # x 27
        # y 520
        "raub": {
            "1": {
                "x": 27,
                "y": 520,
            },
            # x 248
            "2": {
                "x": 27 + 248,
                "y": 520,
            },
            # x 263
            "3": {
                "x": 27 + 248 + 263,
                "y": 520,
            },
            # x 250
            "4": {
                "x": 27 + 248 + 263 + 250,
                "y": 520,
            },
        },
    },
    "vor_2": {
        "trup": {
            "p": {
                "x": 0,
                "y": 0,
            },
            # x 86
            "r": {
                "x": 0 + 86,
                "y": 0,
            },
            # x 91
            "a": {
                "x": 0 + 86 + 91,
                "y": 0,
            },
            # x 89
            "l": {
                "x": 0 + 86 + 91 + 89,
                "y": 0,
            },
            # x 88
            "s": {
                "x": 0 + 86 + 91 + 89 + 88,
                "y": 0,
            },
            # x 87
            "pl": {
                "x": 0 + 86 + 91 + 89 + 88 + 87,
                "y": 0,
            },
        },
        # x 27
        # y 520
        "raub": {
            "1": {
                "x": 27,
                "y": 520,
            },
            # x 248
            "2": {
                "x": 27 + 248,
                "y": 520,
            },
            # x 263
            "3": {
                "x": 27 + 248 + 263,
                "y": 520,
            },
            # x 250
            "4": {
                "x": 27 + 248 + 263 + 250,
                "y": 520,
            },
        },
    },
}


def create_coord(coordinat, x_offset, y_offset):
    import copy

    # Create a deep copy of the original coordinates
    updated_coord = copy.deepcopy(coordinat)

    # Function to recursively update coordinates
    def update(obj):
        for key, value in obj.items():
            if isinstance(value, dict):
                if "x" in value and "y" in value:
                    value["x"] += x_offset
                    value["y"] += y_offset
                else:
                    update(value)

    update(updated_coord)

    return updated_coord


# Offsets
anpass_coord = {
    "3_bild": {"x": 4347, "y": 354},
    "1_bild": {"x": 1056, "y": 336},
    "x_bild": {"x": 1046, "y": 418},
}
# pass_coord = anpass_coord["x_bild"]
# new_coords = create_coord(coordinat["vorlage"], pass_coord["x"], pass_coord["y"])


# Neue Koordinaten erzeugen
def load_coordinates_from_file(filename="position.json"):
    try:
        with open(filename, "r") as file:
            new_coords = json.load(file)
            print("Koordinaten erfolgreich geladen.")
            return new_coords
    except FileNotFoundError:
        print(f"Die Datei {filename} wurde nicht gefunden.")
        return {}


vorlagen_coords = load_coordinates_from_file()
new_coords = vorlagen_coords["1_bild"]
# new_coords = vorlagen_coords["3_bild"]

# >> Truppen anzahl
p = 598
r = 48
a = 0
l = 672
s = 0
pl = 1
add_trup(p, r, a, l, s, pl)

print_resurce("t")


# !!! Thread Test


def ESC_break(func, *args):
    """
    Führt eine Funktion in einem separaten Prozess aus und beendet den Prozess,
    wenn die ESC-Taste gedrückt wird.

    Parameters:
        func: Die auszuführende Funktion.
        *args: Argumente für die Funktion.
    """
    if __name__ == "__main__":
        # Prozess erstellen und starten
        process = multiprocessing.Process(target=func, args=args)
        process.start()

        print("Drücke ESC, um den Prozess zu beenden.")
        while process.is_alive():
            if keyboard.is_pressed("esc"):
                print("ESC wurde gedrückt. Beende den Prozess...")
                process.terminate()  # Prozess beenden
                process.join()  # Warten, bis der Prozess beendet ist
                break

        print("Prozess erfolgreich beendet.")


ESC_break(send_all_trup, new_coords)


# send_all_trup(new_coords)


# !!! Time test


# print_time(100)
# print_time(200)
# print_time(300)
# print_time(400)
# print_time(500)
# print_time(600)
# print_time(700)
# print_time(800)
# print_time(900)
# print_time(1000)
# print_time(1100)
# print_time(8000)
# print_time(1500)
# print_time(15000)


# resurce_h(100)
# resurce_h(200)
# resurce_h(300)
# resurce_h(400)
# resurce_h(500)
# resurce_h(600)
# resurce_h(700)
# resurce_h(800)
# resurce_h(900)
# resurce_h(1000)
# resurce_h(1100)
# resurce_h(1500)
# resurce_h(15000)


# >>> !>S main
