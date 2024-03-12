# import modules
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# get URL from the User
url = input("Enter your URL here:")

# checked validity of the URL
try:
    # Example: url = "https://www.python.org/"
    resp = urlopen(url)
    print("status code: " + str(resp.status))
    print("Message Reason: " + resp.reason)
    print("Message Headers: " + str(resp.headers))

except HTTPError as err:
    # Example: url = "http://httpbin.org/status/404"

    # Display messages
    print("status code for HTTPError : " + str(err.code))
    print("Message for HTTPError: " + err.reason) 

except URLError as e:
    # Example: url= "https://www.python.o"

    # Retrieve the first element of the List and replace "[" with an empty space
    print("status code for URLError: " + str(e.reason).split(']')[0].replace('[',''))

    # Retrieve the second element of the List
    print("Message for URLError : " + str(e.reason).split(']')[1])