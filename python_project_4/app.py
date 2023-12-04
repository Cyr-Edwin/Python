# Import Modules
import json
import csv

# Load  JSON file
with open("json_file.json") as json_file:
    # json_file store as dictionary 
    json_data = json.load(json_file)
    # Display data
    #print(json_data)

# Create a list of content
content = json_data['content']['items']
#print(content)

# Open a new file in writing mode
file = open('json_to_csv.csv', 'w')

# Create an object for writing into it
csv_file = csv.writer(file)

# Counter used as header
count = 0

for item in content:
    if count == 0:
        # Writting csv headers
        header = item.keys()
        #print(header)
        csv_file.writerow(header)
        count=+1
    # Writting data into CSV file
    csv_file.writerow(item.values())
    
file.close()