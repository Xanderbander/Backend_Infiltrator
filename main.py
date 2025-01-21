import argparse
from modules import (
    reconnaissance,
    injection_testing,
    authentication_testing,
    file_upload_testing,
    api_analysis,
    logic_testing,
)
from core import report_generator

def main():
    print("BackEnd Infiltrator v1.0 - Penetration Testing Tool")
    print("---------------------------------------------------")
    parser = argparse.ArgumentParser(description="Run penetration tests on a target URL.")
    parser.add_argument("--url", type=str, required=True, help="Target URL to test.")
    parser.add_argument("--module", type=str, choices=[
        "recon", "injection", "auth", "upload", "api", "logic", "all"
    ], default="all", help="Module to run. Default: all")

    args = parser.parse_args()

    url = args.url
    module = args.module

    print(f"Target URL: {url}")
    print(f"Running module: {module}")

    # Module execution logic
    if module == "recon" or module == "all":
        reconnaissance.run(url)
    if module == "injection" or module == "all":
        injection_testing.run(url)
    if module == "auth" or module == "all":
        authentication_testing.run(url)
    if module == "upload" or module == "all":
        file_upload_testing.run(url)
    if module == "api" or module == "all":
        api_analysis.run(url)
    if module == "logic" or module == "all":
        logic_testing.run(url)

    # Generate consolidated report
    report_generator.generate(url)
    print("Testing complete. Report saved to 'reports/' directory.")

if __name__ == "__main__":
    main()
