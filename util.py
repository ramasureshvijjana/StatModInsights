import requests
import json
import pandas as pd
import logging
logging.basicConfig(format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class Util:
    def __init__(self):
        pass
    def download_data_config(self, github_raw_url):

        # Specify the local path where you want to save the downloaded file
        local_json_file_path = github_raw_url.split('/')[-1]
        logging.debug(f"the local_file_path is {local_json_file_path}")

        # Download the file
        response = requests.get(github_raw_url)
        with open(local_json_file_path, 'w') as local_file:
            local_file.write(response.text)

        # Now, open the local file 
        with open(local_json_file_path, 'r') as json_file:
            data_json = json.load(json_file)

        logging.debug(f"MeticulousStatsReporter  {data_json}")
        return data_json
    def load_input_data(self, data_file_path, required_columns):
        data = pd.read_csv(data_file_path,
                           usecols= required_columns)
        return data
    
    def classifying_numeric_and_obj_clms(self, msr_obj):

        dtype_clm_keys = ['numeric_columns', "string_columns"]
        datatype_unkown_columns = list(msr_obj.data.columns)
        
        # Classifing the columns
        for key in dtype_clm_keys:
            if key in msr_obj.data_json:
                msr_obj.datatype_classified_clms[key] = msr_obj.data_json[key]
            else:
                msr_obj.datatype_classified_clms[key] = [col for col in datatype_unkown_columns if pd.api.types.is_numeric_dtype(msr_obj.data[col])]
            datatype_unkown_columns = [clm for clm in datatype_unkown_columns if clm not in msr_obj.datatype_classified_clms[key]]
            logging.debug(f"The Datatypes classified columns after filter the Numaric columns are {msr_obj.datatype_classified_clms}")
        
        msr_obj.datatype_classified_clms['datatype_unkown_columns'] = datatype_unkown_columns
        