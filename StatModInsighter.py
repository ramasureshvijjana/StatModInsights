import os
from MeticulousStatsReporter import MeticulousStatsReporter as msr

if __name__ == "__main__":
    print("Pipeline running started.")
    # Extracting the environment variables from yml
    github_raw_url = os.getenv("feed_json")
    data_file_path = os.getenv("data_file_path")

    # Creating object for MeticulousStatsReporter class, this is the starting point of pipeline process
    smi_obj = msr(github_raw_url, data_file_path)
    print("Pipeline running succeeded.")
    pass

# read data