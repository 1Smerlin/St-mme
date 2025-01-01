from PIL import Image
import pytesseract

# Load the image to extract text
image_path = "./rang29-12-24new.png"
image = Image.open(image_path)

# Extract text from image using Tesseract OCR
extracted_text = pytesseract.image_to_string(image, lang="deu")
print(extracted_text)


player = {
    "Vergangenheit": {"18.12.24": 321, "29.12.24": 4674},
    "Böser78": {"18.12.24": 597, "29.12.24": 2586},
    "XxGodEaterXx": {"18.12.24": 776, "29.12.24": 2100},
    "BlackOperator": {"18.12.24": 741, "29.12.24": 2096},
    "Merlok": {"18.12.24": 735, "29.12.24": 1877},
    "xXNadjeschdaXx": {"18.12.24": 639, "29.12.24": 1743},
    "Rifkyman": {"18.12.24": 732, "29.12.24": 1614},
    "erhama99": {"18.12.24": 544, "29.12.24": 1584},
    "kennykeks": {"18.12.24": 0, "29.12.24": 1553},  # !!! neu
    "Aulendil01": {"18.12.24": 450, "29.12.24": 1379},
    "falco48": {"18.12.24": 673, "29.12.24": 1271},
    "leo.pard": {"18.12.24": 399, "29.12.24": 1152},
    "RaPo": {"18.12.24": 261, "29.12.24": 1150},
    "Jokelan": {"18.12.24": 434, "29.12.24": 1077},
    "Rouven": {"18.12.24": 388, "29.12.24": 762},
    "Klepiiiii": {"18.12.24": 253, "29.12.24": 559},
    "Firepueppi112": {"18.12.24": 0, "29.12.24": 512},  # !!! neu
    "Wilhelm.der.69": {"18.12.24": 0, "29.12.24": 413},  # !!! neu
    "Salvatrucha7": {"18.12.24": 0, "29.12.24": 404},  # !!! neu
    "Dominican": {"18.12.24": 204, "29.12.24": 299},
}
