from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# BMW, 3er, Benzin, EZ von 2016, von 74 kW (101 PS), bis 110 kW (150 PS), Türen 4/5, Manuell, Limousine
URL = "https://www.12gebrauchtwagen.de/suchen?utf8=%E2%9C%93&s%5Bsort%5D=6&s%5Bmk%5D=11&s%5Bmd%5D=108&s%5By_min%5D=2016&s%5By_max%5D=&s%5Bm_min%5D=&s%5Bm_max%5D=&s%5Bprice_or_rate%5D=price&s%5Bpr_min%5D=&s%5Bpr_max%5D=&s%5Brate_from%5D=&s%5Brate_to%5D=&s%5Bzip%5D=&s%5Bt%5D=3&s%5Bfuel%5D%5B%5D=2&s%5Bg%5D=m&s%5Bpw_min%5D=74&s%5Bpw_max%5D=110&s%5Bsince%5D=&s%5Bprovider_id%5D%5B%5D=4&s%5Bprovider_id%5D%5B%5D=68&s%5Bprovider_id%5D%5B%5D=26&s%5Bprovider_id%5D%5B%5D=16&s%5Bprovider_id%5D%5B%5D=34&s%5Bprovider_id%5D%5B%5D=35&s%5Bprovider_id%5D%5B%5D=28&s%5Bprovider_id%5D%5B%5D=27&s%5Bprovider_id%5D%5B%5D=2&s%5Bdoors%5D%5B%5D=4-5&s%5Bcu%5D="

response = requests.get(URL, headers={"Accept-Language": "de-DE"})
soup = BeautifulSoup(response.content, 'lxml')

articles = soup.select('a[class*="car-make-bmw"]')

articlelist_11 = []
for item in articles:
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

    articlelist_11.append(data)

# Create a DataFrame from the collected data
df = pd.DataFrame(articlelist_11)
current_datetime = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f'bmw_aktuell_price_Stand_{current_datetime}.csv')
