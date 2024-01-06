import os
from MeticulousStatsReporter import MeticulousStatsReporter as msr

def stat_mod_insighter_start():
    print("Pipeline running started.")
    github_raw_url = os.getenv("feed_json")
    smi_obj = msr(github_raw_url)
    print("Pipeline running succeeded.")
    pass


# oops setup