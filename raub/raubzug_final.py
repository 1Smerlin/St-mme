import pyautogui
import time

trup = {
    "p": {
        "Spitz_name": "picke",
        "name": "Speerträger",
        "pro_Roh": 1.2,
        "x": 4111,
        "y": 330,
    },
    "r": {
        "Spitz_name": "Ritter",
        "name": "Schwertkämpfer",
        "pro_Roh": 2,
        "x": 4202,
        "y": 330,
    },
    "a": {
        "Spitz_name": "Axt",
        "name": "Axtkämpfer",
        "pro_Roh": 3,
        "x": 4288,
        "y": 330,
    },
    "l": {
        "Spitz_name": "leicht",
        "name": "leichte Kavallerie",
        "pro_Roh": 0.375,
        "x": 4377,
        "y": 330,
    },
    "s": {
        "Spitz_name": "schwer",
        "name": "schwere Kavallerie",
        "pro_Roh": 0.6,
        "x": 4464,
        "y": 330,
    },
    "pl": {
        "Spitz_name": "Paladin",
        "name": "Paladin",
        "pro_Roh": 0.3,
        "x": 4557,
        "y": 330,
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
        "button": {
            "x": 4137,
            "y": 852,
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
        "button": {
            "x": 4390,
            "y": 852,
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
        "button": {
            "x": 4651,
            "y": 852,
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
        "button": {
            "x": 4898,
            "y": 852,
        },
    },
}


# >> Time
def convert_s(zeit_obj):
    seconds = zeit_obj["h"] * 3600 + zeit_obj["m"] * 60 + zeit_obj["s"]
    return seconds


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


# > Größe
#  : Rohst. : a : r : p   : s   : l     : pl
# 1: 1      : 3 : 2 : 1.2 : 0.6 : 0.375 : 0.3
# Kosten
#           :130:130: 90  : 950 : 475   : 80


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
    for raub_key in raub:
        resurce = raub[raub_key]["sum"]
        print("Raub: ", raub_key)
        print("sum: ", resurce)
        gesammt += resurce
        print("gesammt: ", gesammt)
        if more:
            for trup_key in raub[raub_key]["trup"]:
                print(f"{trup_key}: ", raub[raub_key]["trup"][trup_key])
    print(f"Gesammt Summe: ", gesammt)
    print(f"Time: ", t)
    print(f"Time Second: ", convert_s(t))
    print(f"pro Stunde: ", gesammt / convert_s(t) * 3600)


# >> Truppen anzahl
p = 239
r = 175
a = 0
l = 164
s = 0
pl = 1
t = {"h": 1, "m": 49, "s": 20}

add_trup(p, r, a, l, s, pl)

# print_resurce("t")
print_resurce()


# >>> Bot


def klick_und_eingabe(x, y, zahl):
    # Maus zur angegebenen Position bewegen und klicken
    pyautogui.moveTo(x, y, duration=0.5)  # Optional: duration für sanfte Bewegung
    pyautogui.click()

    # Kurze Verzögerung, um sicherzustellen, dass das Eingabefeld fokussiert ist
    time.sleep(0.2)

    # Zahl eingeben
    pyautogui.typewrite(str(zahl), interval=0.1)  # Optional: interval für Tippen-Verzögerung


def send_trup(raub_key):
    pyautogui.moveTo(raub[raub_key]["button"]["x"], raub[raub_key]["button"]["y"], duration=0.5)  # Optional: duration für sanfte Bewegung
    pyautogui.click()


def send_all_trup():
    for raub_key in raub:
        for trup_key in raub[raub_key]["trup"]:
            if raub[raub_key]["trup"][trup_key] > 0:
                klick_und_eingabe(trup[trup_key]["x"], trup[trup_key]["y"], raub[raub_key]["trup"][trup_key])

        send_trup(raub_key)


send_all_trup()
