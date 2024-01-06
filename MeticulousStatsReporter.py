import pandas as pd
from util import Util
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class  MeticulousStatsReporter:
    def __init__(self, github_raw_url, data_file_path):
        # Creating required internal objs.
        util_obj = Util()

        # Downloading data configuration json.
        self.data_json = util_obj.download_data_config(github_raw_url)
        logging.info(f"The data configuration json has been downloaded successfully.")

        # Loading input data file as pandas df.
        required_columns = self.data_json['required_columns'] if 'required_columns' in self.data_json else None
        self.data = util_obj.load_input_data(data_file_path, required_columns)
        self.data.head()
        logging.info(f"The input data loaded successfully.")

        # Classifying the dataframe columns based on dtypes.
        self.datatype_classified_clms = dict()
        util_obj.classifying_numeric_and_obj_clms(self)
        logging.info(f"The dataframe columns are classified successfully based on dtypes.\n\
              The classified datatype columns are {self.datatype_classified_clms}")
    

        