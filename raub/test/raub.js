let button = document.querySelectorAll("a.btn.btn-default.free_send_button");

let allInput = {
  p: document.querySelector("input[name=spear]"),
  r: document.querySelector("input[name=sword]"),
  a: document.querySelector("input[name=axe]"),
  l: document.querySelector("input[name=light]"),
  s: document.querySelector("input[name=heavy]"),
  pl: document.querySelector("input[name=knight]"),
};

function simulateInputSequence(inputFeld, zahl) {
  // Setze den Fokus auf das Input-Feld
  inputFeld.focus();

  // Teile die Zahl in einzelne Ziffern auf
  const ziffern = zahl.toString().split("");

  // Simuliere die Eingabe jeder Ziffer
  ziffern.forEach((ziffer, index) => {
    setTimeout(() => {
      // Simuliere einen Tastendruck
      const event = new KeyboardEvent("keydown", {
        key: ziffer, // Der eingegebene Schlüssel (z. B. "1")
        code: `Digit${ziffer}`, // Der physische Tasten-Code (z. B. "Digit1")
        charCode: ziffer.charCodeAt(0),
        keyCode: ziffer.charCodeAt(0),
        bubbles: true, // Event sollte blubbern
        cancelable: true, // Event sollte abbrechbar sein
      });

      // Löst das Event aus
      inputFeld.dispatchEvent(event);

      // Füge die Ziffer ins Feld ein
      inputFeld.value += ziffer;
    }, index * 200); // Zeitversatz für jede Ziffer (200 ms)
  });
}

add_list = {
  1: { sum: 337.8333333333333, skal: 1, trup: { p: 111, r: 100, a: 0, l: 72, s: 0, pl: 1 } },
  2: { sum: 338.75, skal: 2.5, trup: { p: 42, r: 41, a: 0, l: 30, s: 0, pl: 0 } },
  3: { sum: 337.5, skal: 5, trup: { p: 21, r: 20, a: 0, l: 15, s: 0, pl: 0 } },
  4: { sum: 340.0, skal: 7.5, trup: { p: 14, r: 14, a: 0, l: 10, s: 0, pl: 0 } },
};

for (const [key, value] of Object.entries(add_list["1"]["trup"])) {
  console.log(key); // Gibt die Keys aus: a, b, c
  console.log(value); // Gibt die Werte aus: 1, 2, 3
  simulateInputSequence(allInput[key], value);
}
