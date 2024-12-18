def finde_geringsten_raub(raub):
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


# Beispielobjekt
raub = {
    "1": {
        "sum": 10,
        "skal": 1,
        "trup": {"p": 0, "r": 0, "a": 0, "l": 0, "s": 0, "pl": 0},
    },
    "2": {
        "sum": 5,
        "skal": 2.5,
        "trup": {"p": 0, "r": 0, "a": 0, "l": 0, "s": 0, "pl": 0},
    },
    "3": {
        "sum": 5,
        "skal": 5,
        "trup": {"p": 0, "r": 0, "a": 0, "l": 0, "s": 0, "pl": 0},
    },
    "4": {
        "sum": 8,
        "skal": 7.5,
        "trup": {"p": 0, "r": 0, "a": 0, "l": 0, "s": 0, "pl": 0},
    },
}

# Funktion aufrufen
geringster = finde_geringsten_raub(raub)
print(f"Der Raubzug mit der geringsten Summe ist: Raub {geringster}")
