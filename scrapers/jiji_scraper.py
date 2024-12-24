import requests
from bs4 import BeautifulSoup
import json
from utils import save_to_json, get_last_scraped_url
import time

# Headers to simulate a browser visit (optional, adjust as necessary)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

def query_jiji_api(last_scraped_url_filename, slug, output_filename):
    url = get_last_scraped_url(last_scraped_url_filename, slug)

    while url:
        print(f"Scraping {url}")

        response = requests.get(url, headers=HEADERS)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()

            adverts_list = data.get("adverts_list", {}).get("adverts", {})
            url = data.get("next_url")
            save_to_json(adverts_list, output_filename)

        # Update the last scraped url
        if url:
            with open(last_scraped_url_filename, "w") as fw:
                fw.write(url)

        # Sleep to avoid being rate flagged by Jiji Servers
        time.sleep(2) # Sleep for 2 seconds

    return data


def main():
    output_file = "property_catalog.json" # vehicles_catalog.json property_catalog.json
    real_estate = "real_estate"
    last_scraped_url_filename = "last_scraped_property_url"

    # Property -> last_scraped_property_url real-estate
    # Vehicles -> last_scraped_vehicles_url vehicles

    adverts = query_jiji_api(last_scraped_url_filename, real_estate, output_file)

if __name__ == "__main__":
    main()
