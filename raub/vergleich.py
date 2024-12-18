# > Größe
#  : Rohst. : a : r : p   : s   : l     : pl
# 1: 1      : 3 : 2 : 1.2 : 0.6 : 0.375 : 0.3
# Kosten
#           :130:130: 90  : 950 : 475   : 80

# print("a pro stoff: ", 130 / (1 / 3))
# print("r pro stoff: ", 130 / (1 / 2))
# print("p pro stoff: ", 90 / (1 / 1.2))
# print("s pro stoff: ", 950 / (1 / 0.6))
# print("l pro stoff: ", 475 / (1 / 0.375))
# print("pl pro stoff: ", 80 / (1 / 0.3))

# print("a pro stoff/h: ", 130 / ((1 / 3) / (60 + 30) * 60))
# print("r pro stoff/h: ", 130 / ((1 / 2) / (60 + 30) * 60))
# print("p pro stoff/h: ", 90 / ((1 / 1.2) / (60 + 30) * 60))
# print("s pro stoff/h: ", 950 / ((1 / 0.6) / (60 + 30) * 60))
# print("l pro stoff/h: ", 475 / ((1 / 0.375) / (60 + 30) * 60))
# print("pl pro stoff/h: ", 80 / ((1 / 0.3) / (60 + 30) * 60))


# >>> Build Kosten berechner
def build_kost(holz, lehm, eisen, pro_n, pro_v):
    kosten = (holz + lehm + eisen) / (pro_n - pro_v)
    print(kosten)


holz = 1.137
lehm = 1.800
eisen = 860

pro_v = 214
pro_n = 249


build_kost(holz, lehm, eisen, pro_n, pro_v)


# >>> Zeit

zeit_stoff = {
    "100": {"h": 0, "m": 52, "s": 27},
    "200": {"h": 1, "m": 11, "s": 54},
    "300": {"h": 1, "m": 30, "s": 21},
    "400": {"h": 1, "m": 48, "s": 11},
    "500": {"h": 2, "m": 5, "s": 34},
    "600": {"h": 2, "m": 22, "s": 37},
}


def read_s(stoff_name):
    zeit_obj = zeit_stoff[stoff_name]
    seconds = (((zeit_obj["h"] * 60) + zeit_obj["m"]) * 60) + zeit_obj["s"]
    return seconds


def print_s(stoff_name):
    seconds = read_s(stoff_name)
    print(f"{stoff_name}: ", seconds)


def compare_s(stoff_name1, stoff_name2):
    seconds1 = read_s(stoff_name1)
    seconds2 = read_s(stoff_name2)
    if seconds1 < seconds2:
        compare_result = seconds2 - seconds1
        print(f"{stoff_name1}-{stoff_name2}: ", compare_result)
    else:
        compare_result = seconds1 - seconds2
        print(f"{stoff_name2}-{stoff_name1}: ", compare_result)


print_s("100")
print_s("200")
compare_s("100", "200")
print_s("300")
compare_s("200", "300")
print_s("400")
compare_s("300", "400")
