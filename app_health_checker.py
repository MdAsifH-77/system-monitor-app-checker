# Import requests for HTTP requests
import requests

# URL of the application/website to check
URL = "https://www.google.com"  # Replace with your target app URL if needed

def check_app_health():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"✅ Application is UP (Status Code: {response.status_code})")
        else:
            print(f"⚠️ Application returned Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Application is DOWN. Error: {e}")

if __name__ == "__main__":
    check_app_health()
