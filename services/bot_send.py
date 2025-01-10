import requests
from datetime import datetime
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
def send_msg(**kwargs):
    token = "6754543518:AAEKV335o7NiQ-i-Ze_IWXypIBWCwJ0jTLw"  # bot token

    user_id = "5445752576"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S  {kwargs} </b> ')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())