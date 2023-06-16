import requests


token = '6266737620:AAFv6ykgL0a0fbzUWeZPqU2fDJCC_eXBYEA'
chat_id = '-884117797'
text = 'Текст_2'


def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text,
    })


sendTelegram()