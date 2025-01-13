import requests
from datetime import datetime
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
def send_msg(**kwargs):
    token = "TOKEN"  # bot token

    user_id = "Telegram_id"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S  {kwargs} </b> ')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
