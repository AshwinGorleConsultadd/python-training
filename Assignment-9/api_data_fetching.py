import requests

# fetching gneeral information of dog from the free api I got!

url = "https://dogapi.dog/api/v2/breeds"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for breed in data["data"]:
        info = breed["attributes"]
        name = info["name"]
        description = info["description"]
        life = f"{info['life']['min']} - {info['life']['max']} years"
        weight = f"{info['male_weight']['min']} - {info['male_weight']['max']} kg"
        hypo = "Yes" if info["hypoallergenic"] else "No"

        print("Breed:", name)
        print(" Description:", description)
        print(" Lifespan:", life)
        print(" Male Weight:", weight)
        print(" Hypoallergenic:", hypo)
        print("-" * 50)
else:
    print("Failed to fetch data. Status code:", response.status_code)
