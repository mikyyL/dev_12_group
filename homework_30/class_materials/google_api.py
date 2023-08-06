import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
    "q": "Hello, world!",
    "target": "es",
    "source": "en"
}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "46a60ddcfamsh735cfd849f48005p1f6015jsn9acf1c534c5d",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
