import os
from . import MeticulousStatsReporter as msr

def stat_mod_insighter_start():
    github_raw_url = os.getenv("feed_json")
    smi_obj = msr.MeticulousStatsReporter(github_raw_url)
    pass
