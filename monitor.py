import requests


def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)

        response_time = response.elapsed.total_seconds()

        print("URL:", url)
        print("Status code:", response.status_code)
        print("Response time:", round(response_time, 3), "seconds")

    except requests.RequestException as error:
        print("URL:", url)
        print("Hata:", error)


websites = []
with open("websites.txt", "r", encoding="utf-8") as file:
    for line in file:
        url = line.strip()

        if url:
            websites.append(url)

for website in websites:
    check_website_status(website)
    print("-" * 40)