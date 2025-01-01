import json
import os
from pynput import mouse


# Funktion, die die Mausposition aufnimmt und in das Dictionary einträgt
def update_coordinates(coordinat):
    # Temporäre Variablen zur Speicherung der Koordinaten
    temp_coordinates = {"x": None, "y": None}

    def on_click(x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            print(f"Mausposition: ({x}, {y})")
            temp_coordinates["x"] = x
            temp_coordinates["y"] = y
            listener.stop()

    # Iteriere durch die Kategorien 'trup' und 'raub'
    for category, items in coordinat.items():
        for key, obj in items.items():
            print(f"Klicke, um die Position für {category}[{key}] festzulegen.")

            # Listener starten und Mausposition aufnehmen
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()

            # Speichere die Mauskoordinaten im Dictionary
            obj["x"] = temp_coordinates["x"]
            obj["y"] = temp_coordinates["y"]

    return coordinat


# Koordinaten speichern in position.json
def save_coordinates_to_file(coordinat, filename="position.json"):
    with open(filename, "w") as file:
        json.dump(coordinat, file, indent=4)


# Funktion, die das Dictionary aus einer Datei lädt und in einer Variable speichert
def load_coordinates_from_file(filename="position.json"):
    try:
        with open(filename, "r") as file:
            new_coords = json.load(file)
            print("Koordinaten erfolgreich geladen.")
            return new_coords
    except FileNotFoundError:
        print(f"Die Datei {filename} wurde nicht gefunden.")
        return {}


# Hauptfunktion
def write_position(position_name):
    if os.path.exists("position.json"):
        new_coords = load_coordinates_from_file()
    else:
        new_coords = {}

    coordinat = {
        "trup": {
            "p": {"x": 0, "y": 0},
            "r": {"x": 0, "y": 0},
            "a": {"x": 0, "y": 0},
            "l": {"x": 0, "y": 0},
            "s": {"x": 0, "y": 0},
            "pl": {"x": 0, "y": 0},
        },
        "raub": {
            "1": {"x": 0, "y": 0},
            "2": {"x": 0, "y": 0},
            "3": {"x": 0, "y": 0},
            "4": {"x": 0, "y": 0},
        },
    }
    updated_coordinates = update_coordinates(coordinat)
    new_coords[position_name] = updated_coordinates
    save_coordinates_to_file(new_coords)
    print("Koordinaten erfolgreich gespeichert in position.json")


if __name__ == "__main__":
    # write_position("1_bild")
    write_position("3_bild")
