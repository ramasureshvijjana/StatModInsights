import pandas as pd
import json
import os


json_path = os.getenv("feed_json")
print(f"MeticulousStatsReporter  {json_path}")

with open(json_path, 'r') as json_file:
    data = json.load(json_file)