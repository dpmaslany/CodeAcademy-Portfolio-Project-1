import csv
import random

fish_dict = {}

with open('/home/daniel/dev/learning/python/python_project_1/fish.csv') as fish_data_csv:
    fish_data = list(csv.DictReader(fish_data_csv))  # Convert to list first
    for idx, fish in enumerate(fish_data):
        fish_dict[idx] = fish  # Use numeric index as key

