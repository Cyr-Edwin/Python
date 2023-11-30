# Import Modules
import json
import xmltodict

# Read the XML file
with open('books.xml') as book_xml_file:

    # Convert xml file to Python Dictionary
    xml_dict =xmltodict.parse(book_xml_file.read()) 

    # Covert json object to string
    json_string = json.dumps(xml_dict)

# Write into a file
with open("data.json" , "w") as json_file:

    json_file.write(json_string)

    # close  file
    json_file.close()

 