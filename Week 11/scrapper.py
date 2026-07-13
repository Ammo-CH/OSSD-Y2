import requests
from bs4 import BeautifulSoup
import csv


def get_cars_data(car):
    
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    cars = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        if not tables:
            print("No tables found on the webpage.")

        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cols = row.find_all('td')

                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)

                    cars.append({'name': name, 'price': price})

    else:
        print("Failed to retrieve the webpage.")

    return cars


def scrapper():
    car = input("Enter car name (e.g. toyota-corolla): ")
    data = get_cars_data(car)

    if not data:
        print("No data found.")
        return

    print(f"\nFound {len(data)} records:\n")

    for item in data:
        print(item['name'], "=>", item['price'])

    save_to_file(data, f"{car}.csv")



def save_to_file(data, filename):

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["Car Name", "Price"])

        for item in data:
            writer.writerow([item["name"], item["price"]])

    print(f"\nData saved to {filename}")


scrapper()