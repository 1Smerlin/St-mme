import pyautogui
import time


def klick_und_eingabe(x, y, zahl):
    """
    Bewegt die Maus zu den Koordinaten (x, y), klickt und gibt die Zahl ein.

    :param x: x-Koordinate auf dem Bildschirm
    :param y: y-Koordinate auf dem Bildschirm
    :param zahl: Zahl, die eingegeben werden soll
    """
    # Maus zur angegebenen Position bewegen und klicken
    pyautogui.moveTo(x, y, duration=0.5)  # Optional: duration für sanfte Bewegung
    pyautogui.click()

    # Kurze Verzögerung, um sicherzustellen, dass das Eingabefeld fokussiert ist
    time.sleep(0.2)

    # Zahl eingeben
    pyautogui.typewrite(str(zahl), interval=0.1)  # Optional: interval für Tippen-Verzögerung


# Beispielaufruf
if __name__ == "__main__":
    zahl = 12345  # Beispiel Zahl
    klick_und_eingabe(4111, 330, zahl)
