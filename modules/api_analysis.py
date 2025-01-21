import requests

def run(url):
    print("\n[API Analysis Module]")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("API appears accessible. Checking response data...")
            print(f"Response: {response.text[:200]}...")
        else:
            print("API endpoint appears secure.")
    except Exception as e:
        print(f"Error during API analysis: {e}")
