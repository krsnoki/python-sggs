from bs4 import BeautifulSoup
import requests

url = 'https://www.technik-consulting.eu/en/optimizing/drone_PID-optimizing.html'
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')

    for link in soup.find_all('a'):
        print(link.get('href'))

except requests.exceptions.RequestException as e:
    print("Request error:", e)
except Exception as e:
    print("An error occurred:", e)
