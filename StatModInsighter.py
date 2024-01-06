import os
from MeticulousStatsReporter import MeticulousStatsReporter as msr

if __name__ == "__main__":
    print("Pipeline running started.")
    github_raw_url = os.getenv("feed_json")
    smi_obj = msr(github_raw_url)
    print("Pipeline running succeeded.")
    pass

# oops setup