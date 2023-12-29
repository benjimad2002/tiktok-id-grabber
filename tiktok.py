import requests

# Set the search term and the number of results to retrieve
search_term = "your search term"
num_results = 100

# Set the API endpoint and the headers
api_endpoint = "https://api.tiktok.com/v1/search"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

# Set the search parameters
params = {
    "q": search_term,
    "count": num_results
}

# Make the API request
response = requests.get(api_endpoint, headers=headers, params=params)

# Extract the user IDs from the response
user_ids = []
for result in response.json()["data"]:
    user_ids.append(result["user"]["id"])

# Print the user IDs
print(user_ids)
