# Import modules
import argparse
import pyqrcode
import png

# Create a Parser
parser = argparse.ArgumentParser()

# Get url from the user
# Example: url = https://www.python.org/
parser.add_argument('url' , type = str, help='URL')

# Get filename from the user  with .png extension
# Example: filename = "text.png"
parser.add_argument("filename" , type=str , help="filename")


# Display the arguments parser
args = parser.parse_args()

# Convert args Object to a Dictionary
dict = args.__dict__

# Retrieve the first element of the dict
element_0 = dict['url']

# Retrieve the second element of the dict
element_1 = dict['filename']

# Check if the filename ends with .png extension
if element_1.endswith(".png"):
    # Create the  QR Code
    qrcode = pyqrcode.create(element_0)

    # Create the png file
    qrcode.png(element_1 , scale=8)

    # Success message
    print("Your " + element_1 + " has been successfully created.")

else:
    print("Filename should end with .png extension. Thank you!")
    