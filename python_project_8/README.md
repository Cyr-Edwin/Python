# Create , Update and List automatically Repositories from Github using Python and Requests module.

<h6>Modules used</h6>

**1 - requests**
> The **requests** module allows to send HTTP requests using Python.

<h5> Example:</h5>

```
import requests

# store the the object in response
response  = requests.get = ("http://example.com")

# display HTML text
print(response.text)
```

**2 - json**
> The **json** module allows to convert object to dictionary in  Python.

<h5> Example:</h5>

```
import json

# Initialize the json string
country_json = '{"Country": "USA","States": [, "Texas","California"],"Lakes_Available":"Yes"}'

# Using json.loads()
# Converting json to dictionary
country_dict = json.loads(country_json)
print(country_dict)
```
