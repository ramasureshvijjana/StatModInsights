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
        logging.info(f"""The dataframe columns are classified successfully based on dtypes.
                     The classified datatype columns are {self.datatype_classified_clms}""")
        
        # Creating statistics datafrmes to showcase stat reports.
        self.statistics_dfs_dict = dict()
        self.create_statistics_dfs()
        # Updating datatype stats
        self.update_datatype_stats()

        print(df for df in self.statistics_dfs_dict)

    def create_statistics_dfs(self):
        for key, clm_list in self.datatype_classified_clms.items():
            if len(clm_list) > 0:
                self.statistics_dfs_dict[key] = pd.DataFrame(index=clm_list ,
                                                             columns=['Data_Types', 'mean', 'median', 'mode'])

    def update_datatype_stats(self):
        for key in self.statistics_dfs_dict:
            clm_datatype_dict = self.data[self.datatype_classified_clms[key]].dtypes
            self.statistics_dfs_dict[key]['Data_Types'] = self.statistics_dfs_dict[key].index.map(clm_datatype_dict)

    def update_mean_median_mode(self):
        if 'numeric_columns' in self.statistics_dfs_dict:
            clms_mean_values = {numaric_clm: self.data['numaric_clm'].mean() for numaric_clm in self.datatype_classified_clms['numeric_columns']}
        self.statistics_dfs_dict['numeric_columns']['mean'] = self.statistics_dfs_dict['numeric_columns'].index.map(clms_mean_values)