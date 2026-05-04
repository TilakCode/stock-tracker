import requests
from bs4 import BeautifulSoup

BOT_TOKEN = 8554974692:AAGz-pXsteyvcmbz1MVOxD8t3vLJmyr265k
CHAT_ID = 886705625
URL = "https://amzn.in/d/0hiMRvHi"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(URL, headers=headers)

if "Currently unavailable" not in res.text:
    send("🔥 Diet Coke is IN STOCK! Buy fast!")
