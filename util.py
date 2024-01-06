import requests
import json
import pandas as pd

class Util:
    def __init__(self):
        pass
    def download_data_config(self, github_raw_url):

        # Specify the local path where you want to save the downloaded file
        local_json_file_path = github_raw_url.split('/')[-1]
        print(f"the local_file_path is {local_json_file_path}")

        # Download the file
        response = requests.get(github_raw_url)
        with open(local_json_file_path, 'w') as local_file:
            local_file.write(response.text)

        # Now, open the local file 
        with open(local_json_file_path, 'r') as json_file:
            data_json = json.load(json_file)

        print(f"MeticulousStatsReporter  {data_json}")
        return data_json
    def load_input_data(self, data_file_path, required_columns):
        data = pd.read_csv(data_file_path,
                           usecols= required_columns)
        return data
    
    def classifying_numaric_and_obj_clms(self, meticulous_stats_reporter_obj):
        if 'numaric_columns' in meticulous_stats_reporter_obj.data_json:
            numaric_columns = meticulous_stats_reporter_obj.data_json['numaric_columns']
        else:
            datatype_dict = dict(meticulous_stats_reporter_obj.data.dtypes)
            print("Data type of all columns is {datatype_dict}")