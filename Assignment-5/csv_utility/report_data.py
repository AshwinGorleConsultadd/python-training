import csv

def save_to_csv(data, filename):
    if not data:
        return
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
