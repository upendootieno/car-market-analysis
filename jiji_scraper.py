import requests
from bs4 import BeautifulSoup
import json
from utils import save_to_json, parse_adverts, get_last_scraped_url
import time

# Headers to simulate a browser visit (optional, adjust as necessary)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

def query_jiji_api(url, filename):
    next_url = url

    while next_url:
        print(f"Scraping {next_url}")

        response = requests.get(next_url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()

            adverts_list = data.get("adverts_list", {}).get("adverts", {})
            next_url = data.get("next_url")
            save_to_json(adverts_list, filename)

        # Sleep to avoid being rate flagged by Jiji Servers
        time.sleep(3) # Sleep for 3 seconds

    return data


def main():
    output_file = "vehicles_catalog.json"

    last_scraped_url = get_last_scraped_url("last_scraped_vehicles.txt", "vehicles")

    adverts = query_jiji_api(last_scraped_url, output_file)

if __name__ == "__main__":
    main()
