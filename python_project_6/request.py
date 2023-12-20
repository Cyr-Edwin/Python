# import module
import requests

# Githbub repo owner's name
# owner = Kubernetes
owner = input("Enter the owner's name:")

# repo name
# repo = Kubernetes 
repo = input("Enter your repo name:")

# url to fetch pull request 
url = "https://api.github.com/repos/"+ owner + "/"+ repo + "/pulls"

# make a Get request to fetch pull request from GitHub API
response = requests.get(url)

# only for successful request
if response.status_code == 200:
    # convert json format to dictionary
    data = response.json()
   
    # create empty users dictionary
    users = {}
    
    # iterate through each data to retrieve the user'id
    for user_id in data:
        id = user_id['user']['id']
        if id in users:
            users[id] +=1
        else:
             users[id] = 1
        
    # Display ID and counts
    for id , count in users.items():
        print(f"ID: {id}\n")
        print(f"Count(s): {count}\n")
        print("##########")

        
          




