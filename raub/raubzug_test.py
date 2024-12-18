import numpy as np


zeit_stoff = {
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


def read_s(stoff_menge):
    zeit_obj = zeit_stoff[stoff_menge]
    seconds = convert_s(zeit_obj)
    return seconds


def convert_s(zeit_obj):
    seconds = zeit_obj["h"] * 3600 + zeit_obj["m"] * 60 + zeit_obj["s"]
    return seconds


rohstoffe = np.array([stoff_key for stoff_key in zeit_stoff])  # Rohstoffmengen

zeiten = np.array([read_s(stoff_key) for stoff_key in zeit_stoff])


# Polynomiale Regression 2. Grades (quadratische Funktion)
koeffizienten = np.polyfit(rohstoffe, zeiten, 10)  # a, b, c für ax^2 + bx + c
funktion = np.poly1d(koeffizienten)


# Funktion testen
def berechne_zeit(rohstoffe, funktion):
    sekunden = funktion(rohstoffe)
    h = int(sekunden // 3600)
    m = int((sekunden % 3600) // 60)
    s = int(sekunden % 60)
    return {"h": h, "m": m, "s": s}


def print_zeit(stoff_menge):
    zeit_test = berechne_zeit(stoff_menge, funktion)

    print(f"Zeit für {stoff_menge} Rohstoffe: {zeit_test['h']} Stunden, {zeit_test['m']} Minuten, {zeit_test['s']} Sekunden")
    if stoff_menge in zeit_stoff:
        new_seconds = convert_s(zeit_test)
        old_seconds = read_s(stoff_menge)
        if new_seconds > old_seconds:
            deferent = new_seconds - old_seconds
            print(f"new_seconds ist {deferent} Größer")
        elif new_seconds < old_seconds:
            deferent = old_seconds - new_seconds
            print(f"old_seconds ist {deferent} Größer")
        else:
            print(f"new_seconds und old_seconds sind gleich Größ")


# print_zeit(100)
# print_zeit(200)
# print_zeit(300)
# print_zeit(400)
# print_zeit(500)
# print_zeit(600)
# print_zeit(700)
# print_zeit(800)
# print_zeit(900)
# print_zeit(1000)
# print_zeit(1100)
# print_zeit(8000)
# print_zeit(1500)
# print_zeit(15000)


def read_pro_stoff(stoff_menge):
    seconds = read_s(stoff_menge)
    pro_stoff = stoff_menge / seconds * 3600
    print(f"Bei {stoff_menge} ist umsatz {pro_stoff} pro Stunde")


read_pro_stoff(100)
read_pro_stoff(200)
read_pro_stoff(300)
read_pro_stoff(400)
read_pro_stoff(500)
read_pro_stoff(600)
read_pro_stoff(700)
read_pro_stoff(800)
read_pro_stoff(900)
read_pro_stoff(1000)
read_pro_stoff(1100)
read_pro_stoff(1500)
read_pro_stoff(15000)


# seconds = read_s(400)
# pro_stoff = 1600 / seconds * 3600

# print("seconds: ", seconds)
# print("pro_stoff: ", pro_stoff)
