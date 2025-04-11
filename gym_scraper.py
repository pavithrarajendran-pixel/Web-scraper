import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml
import random

# Load config from config.yaml
def load_config(file_path="config.yaml"):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def scrape_with_config():
    config = load_config()
    url = config["url"]
    selectors = config["selectors"]

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    class_elements = soup.select(selectors["class_name"])

    for element in class_elements:
        class_name = element.get_text(strip=True)
        schedule_el = element.select_one(selectors["schedule"])
        fee_el = element.select_one(selectors["fee"])

        data.append({
            "Class Name": class_name,
            "Schedule": schedule_el.get_text(strip=True) if schedule_el else "N/A",
            "Fee": fee_el.get_text(strip=True) if fee_el else "N/A"
        })

    return pd.DataFrame(data)

def simulate_gym_data():
    class_names = [
        "Yoga Flow", "HIIT Blast", "Zumba Dance", "Spinning", "Pilates Core",
        "Strength Training", "Cardio Kickboxing", "Bootcamp", "CrossFit", "Aqua Aerobics"
    ]
    schedules = [
        "Mon/Wed/Fri - 7:00 AM", "Tue/Thu - 6:00 PM", "Sat - 9:00 AM",
        "Daily - 5:30 PM", "Mon-Fri - 8:00 AM", "Sun - 10:30 AM"
    ]
    fees = ["Included in Membership", "$5/class", "$10 drop-in", "Free Trial Available"]

    data = []
    for _ in range(10):
        data.append({
            "Class Name": random.choice(class_names),
            "Schedule": random.choice(schedules),
            "Fee": random.choice(fees),
            "Trainer": random.choice(["Alex", "Jordan", "Taylor", "Sam", "Riley"]),
            "Intensity": random.choice(["Beginner", "Intermediate", "Advanced"])
        })

    return pd.DataFrame(data)
