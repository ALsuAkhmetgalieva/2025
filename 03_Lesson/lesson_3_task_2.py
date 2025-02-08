from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S11", "+79877456562"),
    Smartphone("Iphone", "14 Pro Max", "+79873265256"),
    Smartphone("Honor", "200", "+78965222141"),
    Smartphone("Samsung", "Galaxy", "+79856325412"),
    Smartphone("Xiaomi", "gt2023", "+79562145698")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} - {smartphone.number}")