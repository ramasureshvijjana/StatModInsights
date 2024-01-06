import pandas as pd
from util import Util

class  MeticulousStatsReporter:
    def __init__(self, github_raw_url, data_file_path):
        util_obj = Util()
        #self.github_raw_url = github_raw_url
        self.data_json = util_obj.download_data_config(github_raw_url)
        print(f"Downloding data configuration succeeded")

        required_columns = self.data_json['required_columns'] if 'required_columns' in self.data_json else None
        self.data = util_obj.load_input_data(data_file_path, required_columns)
        util_obj.classifying_numaric_and_obj_clms(self)
        self.data.head()
    

        