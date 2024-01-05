import pandas as pd
import requests
import json
import os


github_raw_url = os.getenv("feed_json")
# json_path = "https://github.com/ramasureshvijjana/StatModInsights_JSON/blob/master/feed_config.json"
# print(f"MeticulousStatsReporter  {json_path}")

# with open(json_path, 'r') as json_file:
#     data = json.load(json_file)

# URL of the raw JSON file on GitHub
#github_raw_url = 'https://raw.githubusercontent.com/ramasureshvijjana/StatModInsights_JSON/master/feed_config.json'

# Specify the local path where you want to save the downloaded file
local_file_path = 'feed_config.json'

# Download the file
response = requests.get(github_raw_url)
with open(local_file_path, 'w') as local_file:
    local_file.write(response.text)

# Now, open the local file
with open(local_file_path, 'r') as json_file:
    data = json.load(json_file)

print(f"MeticulousStatsReporter  {data}")