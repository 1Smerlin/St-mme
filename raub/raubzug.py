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


# result = 1 / 0.375
# result = 1 / 0.6

# result = (1 / 1.2) * 30

# print(result)


# >> Gesammt
p = 188
r = 175
a = 0
l = 127
s = 0
pl = 1


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
    "1": 1,
    "2": 2.5,
    "3": 5,
    "4": 7.5,
}


#  : Raub. : p       :  r  : a      : l      : s      : pl
roh_stärke = 0
roh_stärke = (p / trup["p"]["pro_Roh"]) + (r / trup["r"]["pro_Roh"]) + (a / trup["a"]["pro_Roh"]) + (l / trup["l"]["pro_Roh"]) + (s / trup["s"]["pro_Roh"]) + (pl / trup["pl"]["pro_Roh"])

print(roh_stärke)

print(roh_stärke)

# > Größe
#  : Rohst. : a : r : p   : s   : l     : pl
# 1: 1      : 3 : 2 : 1.2 : 0.6 : 0.375 : 0.3
