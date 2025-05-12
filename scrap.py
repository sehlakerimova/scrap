import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


wb = Workbook()
ws = wb.active
ws.title = "Mini Cooper"
ws.append(["Model və İli", "Qiymət"])

headers = {"User-Agent": "Mozilla/5.0"}


url = "https://turbo.az/autos?marka%5B%5D=42"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

cars = soup.find_all("div", class_="products-i")

print(f"Tapılan Mini Cooper sayı: {len(cars)}")

for car in cars:
    try:
        name_tag = car.find("div", class_="products-i__name")
        title = name_tag.text.strip() if name_tag else "Model yoxdur"

        price_tag = car.find("div", class_="products-i__price")
        price = price_tag.text.strip() if price_tag else "Qiymət yoxdur"

        ws.append([title, price])
    except Exception as e:
        print("Xəta:", e)
        continue


wb.save("turbo_mini_cooper.xlsx")
print("Fayl yaradıldı: turbo_mini_cooper.xlsx")
