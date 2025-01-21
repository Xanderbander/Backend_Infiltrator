import os

def ensure_report_dir():
    if not os.path.exists("reports"):
        os.makedirs("reports")
