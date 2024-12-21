import json
import os
import pandas as pd


def get_last_scraped_url(filename, slug):
    if os.path.exists(filename):
        with open(filename, "r") as fo:
            last_scraped_url = fo.read()
    else:
        last_scraped_url = f"https://jiji.co.ke/api_web/v1/listing?slug={slug}"

    return last_scraped_url


def parse_adverts(filename):
    df = pd.read_json(filename)
    df.head
    df.describe
    return
    # advert_attributes = []
    # with open(filename, "r", encoding="utf-8") as f:
    #     # adverts = json.load(f)
    #     df.read_json(f)

    #     for advert in adverts:
    #         advert_attributes.append(advert.keys())

    # print(advert_attributes)
    # print(len(advert_attributes))

    # return advert_attributes


def save_to_json(data, filename):
    """Save or append the data to a JSON file."""
    # Check if the file already exists
    if os.path.exists(filename):
        # Load existing data
        with open(filename, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
        
        # Append new data
        if isinstance(existing_data, list):
            existing_data.extend(data)
        else:
            raise ValueError(f"The file {filename} does not contain a JSON list.")
    else:
        # Start with new data if file doesn't exist
        existing_data = data

    # Write updated data back to the file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    print(f"Data successfully saved to {filename}")

