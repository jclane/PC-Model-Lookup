import csv

from dell_handler import get_dell_model
from hp_handler import get_hp_model

    
def get_model(serial, brand, model=""):
    brand = brand.lower().strip()
    if brand == "hp":
        return get_hp_model(serial, model)
    elif brand == "dell":
        return get_dell_model(serial)
    else:
        return "unable to locate model info"

def write_output(output):
    with open("hp_lookedup.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerows(output)
        