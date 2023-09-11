from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime


start_page = 1
end_page = 120
auto_list = []

for page in range (start_page, end_page+ 1):
    # 2 Kraftstoffe (Hybrid, Elektro), Türen 4/5, Limousine
    URL = f"https://www.12gebrauchtwagen.de/suchen?page={page}&s%5Bdoors%5D%5B%5D=4-5&s%5Bfuel%5D%5B%5D=7&s%5Bfuel%5D%5B%5D=6&s%5Bt%5D=3"
    response = requests.get(URL, headers={"Accept-Language": "de-DE"})
    soup = BeautifulSoup(response.content, 'lxml')

    autos = soup.select('a[class*="car-make-"]')


    for item in autos:
        title_elem = item.find('h3')
        price_elem = item.find('span', class_="ad-price")
        registration_elem = item.find('span', class_="ad-registration-date")
        location_elem = item.find('div', class_="small-8 medium-3 columns float-left")
        benzin_elem = item.find('div', class_="small-8 columns float-left")
        mileage_elem = item.find('span', class_="ad-mileage")
        power_elem = item.find('span', class_="ad-power truncate")
        gefunden_elem = item.find('span', class_="small-ad-extra-info")

        data = {
            "title": title_elem.text if title_elem else None,
            "price": price_elem.text if price_elem else None,
            "registration": registration_elem.text if registration_elem else None,
            "location": location_elem.text if location_elem else None,
            "benzin": benzin_elem.text if benzin_elem else None,
            "mileage": mileage_elem.text if mileage_elem else None,
            "power": power_elem.text if power_elem else None,
            "gefunden": gefunden_elem.text if gefunden_elem else None
        }

        auto_list.append(data)

# Create a DataFrame from the collected data
df = pd.DataFrame(auto_list)
current_datetime = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f'autos_hybrid_electro_price_Stand_{current_datetime}.csv')
