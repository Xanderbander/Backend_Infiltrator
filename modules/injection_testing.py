import subprocess

def run(url):
    print("\n[Injection Testing Module]")
    try:
        print("Running SQLMap for SQL Injection tests...")
        command = f"sqlmap -u {url} --batch --output-dir=reports/sqlmap"
        subprocess.run(command, shell=True)
        print("SQLMap testing complete. Check 'reports/sqlmap' for details.")
    except Exception as e:
        print(f"Error during injection testing: {e}")
