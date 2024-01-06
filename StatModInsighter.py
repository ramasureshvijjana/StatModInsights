import os
from MeticulousStatsReporter import MeticulousStatsReporter as msr
import logging
logging.basicConfig(format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if __name__ == "__main__":
    logging.info("Pipeline running started.")
    # Extracting the environment variables from yml
    github_raw_url = os.getenv("feed_json")
    data_file_path = os.getenv("data_file_path")

    # Creating object for MeticulousStatsReporter class, this is the starting point of pipeline process
    # Means pipeline start the running by creating MeticulousStatsReporter obj
    smi_obj = msr(github_raw_url, data_file_path)
    logging.info("Pipeline running succeeded.")
    pass

# logging setup