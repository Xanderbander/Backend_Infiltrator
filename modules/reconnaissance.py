import requests
from bs4 import BeautifulSoup

def run(url):
    print("\n[Reconnaissance Module]")
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")

        # Parsing HTML for forms and links
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all("form")
        print(f"Found {len(forms)} forms on the page.")

        with open(f"reports/recon_report.txt", "w") as file:
            file.write(f"Target URL: {url}\n")
            file.write(f"Status Code: {response.status_code}\n")
            file.write(f"Headers: {response.headers}\n")
            file.write(f"Found {len(forms)} forms.\n")
    except Exception as e:
        print(f"Error during reconnaissance: {e}")
