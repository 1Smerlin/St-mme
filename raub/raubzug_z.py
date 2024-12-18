class Raub_Default:
    def __init__(self):
        self.round = 1
        self.add_round = 1
        self.p = 0
        self.r = 0
        self.l = 0
        self.m = 0
        self.z = 0

    def add_raub(self, p, r, l, m, z):
        self.p += p
        self.r += r
        self.l += l
        self.m += m
        if self.z < z:
            self.z = z
        # print("add: ", self.add_round)
        # print("p: ", self.p)
        # print("r: ", self.r)
        # print("l: ", self.l)
        # self.add_round += 1

    def gewinn(self):
        result = self.m / self.z * 60
        print(f"Runde.{self.round} -------!!!")
        self.round += 1
        print("pro Stunde: ", result)
        leicht = self.l
        männer = self.p + self.r + (leicht * 4) + 1
        pro_mann = self.m / männer
        print("pro Mann: ", pro_mann)
        print("p: ", self.p)
        print("r: ", self.r)
        print("l: ", self.l)
        self.p = 0
        self.r = 0
        self.l = 0
        self.m = 0
        self.z = 0


raub_val = Raub_Default()


# >> New
# > 1
p = 147
r = 175
l = 33
z = 60 + 29
m = 298
raub_val.add_raub(p, r, l, m, z)


# > 2
p = 0
r = 0
l = 48
z = 60 + 35
m = 328
raub_val.add_raub(p, r, l, m, z)


# > 3
p = 0
r = 0
l = 24
z = 60 + 33
m = 320
raub_val.add_raub(p, r, l, m, z)


# > 4
p = 0
r = 0
l = 16
z = 60 + 33
m = 320
raub_val.add_raub(p, r, l, m, z)

raub_val.gewinn()


# >> Rest
p = 147
r = 175
l = 110

# >> Gesammt
p = 147
r = 175
l = 121
n = 0


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

result = (1 / 1.2) * 30

print(result)


truppen = {
    "p": {
        "Spitz_name": "picke",
        "name": "Speerträger",
        "pro_Roh": 1.2,
        "pro_man": 1 / 1.2,
    },
    "r": {
        "Spitz_name": "Ritter",
        "name": "Schwertkämpfer",
        "pro_Roh": 2,
        "pro_man": 1 / 2,
    },
    "a": {
        "Spitz_name": "Axt",
        "name": "Axtkämpfer",
        "pro_Roh": 3,
        "pro_man": 1 / 3,
    },
    "l": {
        "Spitz_name": "leicht",
        "name": "leichte Kavallerie",
        "pro_Roh": 0.375,
        "pro_man": 1 / 0.375,
    },
    "s": {
        "Spitz_name": "schwer",
        "name": "schwere Kavallerie",
        "pro_Roh": 0.6,
        "pro_man": 1 / 0.6,
    },
    "pl": {
        "Spitz_name": "Paladin",
        "name": "Paladin",
        "pro_Roh": 0.3,
        "pro_man": 1 / 0.3,
    },
}

# 1: 1      : 1.2 : 2 : 3 : 0.375 : 0.6 : 0.3
