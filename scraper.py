import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch the webpage
url = "https://world-camps.org/camp/global-enrichment-programme/"  # Replace with your selected URL
response = requests.get(url)

if response.status_code != 200:
    print(f"Failed to retrieve the webpage: {response.status_code}")
    exit()

# Step 2: Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Extract the required information
data = {}

# Highlights - Extract all highlights from the list
highlights_tags = soup.select(".elementor-icon-list-items .elementor-icon-list-text")
data["highlights"] = [tag.text.strip() for tag in highlights_tags] if highlights_tags else ["Highlights not found"]

# Overview - Extract the overview text
overview_tag = soup.select_one(".jet-listing-dynamic-field__content p")
data["overview"] = overview_tag.text.strip() if overview_tag else "Overview not found"

# Age Range - Extract the age range from the overview

age_range = "10-17" if "students aged 10-17" in data["overview"] else "Age range not found"
data["age_range"] = age_range

# Availability - Placeholder for now (not explicitly mentioned in the HTML)
availability_tag = soup.select_one(".availability-class")  # Replace with correct class if available
data["availability"] = availability_tag.text.strip() if availability_tag else "Details not available"

# Minimum Stay - Placeholder for now (not explicitly mentioned in the HTML)
minimum_stay_tag = soup.select_one(".minimum-stay-class")  # Replace with correct class if available
data["minimum_stay"] = minimum_stay_tag.text.strip() if minimum_stay_tag else "Details not available"

# Price - Placeholder for now (not explicitly mentioned in the HTML)
price_tag = soup.select_one(".price-class")  # Replace with correct class if available
data["price"] = price_tag.text.strip() if price_tag else "Details not available"

# Main Language - Extracted from the overview
main_language = "English" if "English" in data["overview"] else "Language not found"
data["main_language"] = main_language

# Number of Campers - Placeholder for now (not explicitly mentioned in the HTML)
nr_of_campers_tag = soup.select_one(".number-of-campers-class")  # Replace with correct class if available
data["nr_of_campers"] = nr_of_campers_tag.text.strip() if nr_of_campers_tag else "Details not available"

# Gender - Placeholder for now (not explicitly mentioned in the HTML)
gender_tag = soup.select_one(".gender-class")  # Replace with correct class if available
data["gender"] = gender_tag.text.strip() if gender_tag else "Details not available"

# Bedrooms - Placeholder for now (not explicitly mentioned in the HTML)
bedrooms_tag = soup.select_one(".bedrooms-class")  # Replace with correct class if available
data["bedrooms"] = bedrooms_tag.text.strip() if bedrooms_tag else "Details not available"

# Activities - Extract the list of activities dynamically
activities_tags = soup.select(".jet-listing-grid__item")
data["activities"] = [activity.text.strip() for activity in activities_tags if activity.text.strip()]

# Language Lessons - Extract language-related details dynamically
language_lessons_cost_tag = soup.select_one(".language-cost-class")  # Replace with correct class if available
language_lessons_schedule_tag = soup.select_one(".language-schedule-class")  # Replace with correct class if available
language_lessons_taught_by_tag = soup.select_one(".language-taught-by-class")  # Replace with correct class if available
language_lessons_certificate_tag = soup.select_one(".language-certificate-class")  # Replace with correct class if available

data["language_lessons"] = {
    "offered": ["English"],
    "cost": language_lessons_cost_tag.text.strip() if language_lessons_cost_tag else "Details not available",
    "schedule": language_lessons_schedule_tag.text.strip() if language_lessons_schedule_tag else "Details not available",
    "taught_by": language_lessons_taught_by_tag.text.strip() if language_lessons_taught_by_tag else "Details not available",
    "certificate": language_lessons_certificate_tag.text.strip() if language_lessons_certificate_tag else "Details not available"
}

# Accommodation & Facilities - Extract accommodation details dynamically
accommodation_buildings_tag = soup.select_one(".buildings-class")  # Replace with correct class if available
accommodation_capacity_tag = soup.select_one(".capacity-class")  # Replace with correct class if available
accommodation_amenities_tags = soup.select(".amenities-class")  # Replace with correct class if available

data["accommodation_facilities"] = {
    "buildings": accommodation_buildings_tag.text.strip() if accommodation_buildings_tag else "Details not available",
    "capacity": accommodation_capacity_tag.text.strip() if accommodation_capacity_tag else "Details not available",
    "amenities": [amenity.text.strip() for amenity in accommodation_amenities_tags] if accommodation_amenities_tags else []
}

# Images - Extract image URLs dynamically
# swiper-slide-image jet-popup-cursor-pointer
image_tags = soup.select("img.swiper-slide-image")
data["images"] = [img["src"] for img in image_tags if "src" in img.attrs]

# Step 4: Save data in JSON format
with open("camp_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been successfully scraped and saved in camp_data.json")