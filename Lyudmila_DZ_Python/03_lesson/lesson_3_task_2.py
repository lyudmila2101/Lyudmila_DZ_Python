from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "16 Pro", "+79993456789"),
    Smartphone("Samsung", "Galaxy S3", "+79993456987"),
    Smartphone("Samsung", "Galaxy A7", "+79993454444"),
    Smartphone("Samsung", "Galaxy", "+79993453333"),
    Smartphone("Iphone", "17 Pro", "+79993411111"),
    Smartphone("Iphone", "14 Pro", "+79993422222")
]
for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.number}")




  