def generate(url):
    print("\n[Report Generator]")
    with open("reports/final_report.txt", "w") as report:
        report.write(f"Report for {url}\n")
        report.write("------------------------------------------------\n")
        report.write("Reconnaissance, injection testing, and more completed.\n")
    print("Report generated at 'reports/final_report.txt'.")
