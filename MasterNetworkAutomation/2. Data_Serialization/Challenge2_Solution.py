###################
# Coding Challenge Solution
###################
 
import json
import requests
import csv
 
# getting the json data from the server
response = requests.get("https://jsonplaceholder.typicode.com/users")
 
# loading the json encoded string into a Python Object
# users it's a list of dictionaries
users = json.loads(response.text)
 
# opening the csv file for writing
with open('users.csv', 'w') as f:
    writer = csv.writer(f)
 
    # write a header to file
    writer.writerow(("Name", "City", "GPS", "Company"))
 
    # iterating over the users list
    for user in users:
        # getting the data from the dictionary
        name = user['name']
        city = user['address']['city']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        # constructing the GPS coordinates in form of (lat, lng)
        geo = f'({lat},{lng})'
        company_name = user['company']['name']
 
        # writing to csv file
        csv_data = (name, city, geo, company_name)
        writer.writerow(csv_data)
 
### The resulting CSV File (users.csv):
# Leanne Graham,Gwenborough,"(-37.3159,-37.3159)",Romaguera-Crona
# Ervin Howell,Wisokyburgh,"(-43.9509,-43.9509)",Deckow-Crist
# Clementine Bauch,McKenziehaven,"(-68.6102,-68.6102)",Romaguera-Jacobson
# Patricia Lebsack,South Elvis,"(29.4572,29.4572)",Robel-Corkery
# Chelsey Dietrich,Roscoeview,"(-31.8129,-31.8129)",Keebler LLC
# Mrs. Dennis Schulist,South Christy,"(-71.4197,-71.4197)",Considine-Lockman
# Kurtis Weissnat,Howemouth,"(24.8918,24.8918)",Johns Group
# Nicholas Runolfsdottir V,Aliyaview,"(-14.3990,-14.3990)",Abernathy Group
# Glenna Reichert,Bartholomebury,"(24.6463,24.6463)",Yost and Sons
# Clementina DuBuque,Lebsackbury,"(-38.2386,-38.2386)",Hoeger LLC
