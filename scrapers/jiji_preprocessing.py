def parse_car_details(cars):
    return
    """Parse car details from the given HTML."""
    soup = BeautifulSoup(html, "html.parser")
    
    car_data = []
    cars = soup.find_all("a", class_="b-list-advert-base")
    
    for car in cars:
        try:
            # Scrape the title
            title = car.find("div", class_="b-advert-title-inner").text.strip()
            
            # Scrape the price
            price = car.find("div", class_="qa-advert-price").text.strip()
            
            # Scrape the description
            description = car.find("div", class_="b-list-advert-base__description-text").text.strip()
            
            # Scrape the location
            location = car.find("span", class_="b-list-advert__region__text").text.strip()
            
            # Scrape the attributes (e.g., usage, transmission)
            attributes = car.find_all("div", class_="b-list-advert-base__item-attr")
            usage = attributes[0].text.strip() if len(attributes) > 0 else None
            transmission = attributes[1].text.strip() if len(attributes) > 1 else None
            
            # Scrape the image URL
            image_tag = car.find("img")
            image_url = image_tag["src"] if image_tag else None
            
            # Add the scraped data to the list
            car_data.append({
                "Title": title,
                "Price": price,
                "Description": description,
                "Location": location,
                "Usage": usage,
                "Transmission": transmission,
                "Image URL": image_url,
            })
        
        except AttributeError:
            # Skip any cars with missing data
            continue
    
    return car_data