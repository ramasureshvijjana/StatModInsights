import pandas as pd
from util import Util

class  MeticulousStatsReporter:
    def __init__(self, github_raw_url):
        util_obj = Util()
        #self.github_raw_url = github_raw_url
        data_json = util_obj.download_data_config(github_raw_url)
        print(f"Downloding data configuration succeeded")
        pass
        