from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os

def fetch_autos_data(page):
    URL = f"https://www.12gebrauchtwagen.de/suchen?page={page}&s%5Bdoors%5D%5B%5D=4-5&s%5Bfuel%5D%5B%5D=7&s%5Bfuel%5D%5B%5D=6&s%5Bt%5D=3"
    response = requests.get(URL, headers={"Accept-Language": "de-DE"})
    soup = BeautifulSoup(response.content, 'html.parser')
    autos = soup.select('a[class*="car-make-"]')
    return autos

def extract_auto_data(item):
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
    return data

def save_to_csv(df):
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)
    current_datetime = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f'autos_hybrid_electro_price_Stand_{current_datetime}.csv'
    csv_filepath = os.path.join(data_folder, csv_filename)
    df.to_csv(csv_filepath, index=False)
    
def main():
    start_page = 1
    autos_list = []

    while True:
        autos = fetch_autos_data(start_page)
        
        if not autos:
            break
        
        for item in autos:
            data = extract_auto_data(item)
            autos_list.append(data)
        
        start_page += 1

    df = pd.DataFrame(autos_list)
    save_to_csv(df)

if __name__ == "__main__":
    main()
