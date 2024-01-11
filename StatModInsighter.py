import os
from MeticulousStatsReporter import MeticulousStatsReporter as msr
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if __name__ == "__main__":

    """
    This main function is triggered automatically by CICD pipeline yml.
        1. It collects the environment variables from CICD yml.
        2. Next, it will start the pipeline running by creating the obj to MeticulousStatsReporter class.
    
    Parameters:
        No Parameters
    
    Return Values:
        No return values
    """

    logging.debug("Pipeline running started.")
    
    # Collecting the environment variables from CICD yml.
    github_raw_url = os.getenv("feed_json")
    data_file_path = os.getenv("data_file_path")

    # Creating object of 'MeticulousStatsReporter' class, this is the starting point of pipeline process.
    # Means pipeline running starts by creating the obj to 'MeticulousStatsReporter' class
    smi_obj = msr(github_raw_url, data_file_path)
    logging.debug("Pipeline running succeeded.")