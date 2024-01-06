# import modules
import requests
import json

# Github API endpoint
url = 'https://api.github.com'


# defide header and token
headers = {'Authorization':'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', 'Accept':'application/vnd.github.v3+json'}
# get repo list
def get_repo_list(username):
    api_endpoint = f"{url}/users/{username}/repos"
    response = requests.get(api_endpoint , headers=headers)
    # convert object to dictionary
    github_repos = json.loads(response.content)
    # display the content
    print(github_repos)


# Create a new GitHub repository using the GitHub API
def create_github_repo(token, repo_name):
    headers = {
        'Authorization': f'token {token}',
    }

    data = {
        'name': repo_name,
        'private': False 
    }

    url_endpoint = f'{url}/user/repos'
    response = requests.post(url_endpoint, headers=headers, data=json.dumps(data))

    # check the response and diplay a message
    if response.status_code == 201:
        print(f"GitHub repository '{repo_name}' created successfully.")
    else:
        print(f"Error creating GitHub repository. Status code: {response.status_code}")


create_github_repo('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', "example3")
