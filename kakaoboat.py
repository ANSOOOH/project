from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
from pyvirtualdisplay import Display
import django
import os

#display = Display(visible=0, size=(800,600))
#display.start()

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#driver.implicitly_wait(3)
#driver.get("https://kauth.kakao.com/oauth/authorize?client_id=aaf10ece6c3c39b8c4a845f1ec802e16&redirect_uri=http://itm.seoultech.ac.kr/bachelor_of_information/notice&response_type=code&scope=talk_message")

#driver.find_element_by_id('loginEmail').send_keys("0308su@naver.com")
#driver.find_element_by_id('loginPw').send_keys("a030s080o!")
#driver.find_elements_by_class_name('btn_login')[0].click()
#print("test")

def sendText(accessToken, all_divs) :
    print("b")
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    payloadDict = dict({
            "object_type" : "text",
            "text" : all_divs,
            "link" : {
                "web_url" : "http://iise.seoultech.ac.kr/notice/faculty_announcements_",
                "mobile_web_url" : "http://iise.seoultech.ac.kr/notice/faculty_announcements_"
             },
             "button_title":"바로확인"
            })

    payload = 'template_object=' + str(json.dumps(payloadDict))
    headers = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Cache-Control" : "no-cache",
        "Authorization" : "Bearer " + str(accessToken)
    }
    reponse = requests.request("POST",url,data=payload, headers=headers)
    access_token = json.loads(((reponse.text).encode('utf-8')))
    return access_token



def getAccessToken(clientId, code) :

    print("c")

    url = "https://kauth.kakao.com/oauth/token"

    payload = "grant_type=authorization_code"

    payload += "&client_id=" + clientId

    payload += "&code=" + code

    headers = {

        'Content-Type' : "application/x-www-form-urlencoded",

        'Cache-Control' : "no-cache",

    }

    reponse = requests.request("POST",url,data=payload, headers=headers)

    access_token = json.loads(((reponse.text).encode('utf-8')))

    return access_token


try:
   # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wrap")))
    #print(driver.current_url)
    client_id = "aaf10ece6c3c39b8c4a845f1ec802e16"
    code = "ISIujbZ1-l67Meaoc33l2fHXYYofk4f-wAFrAgVr_FSEv0v6l_rMv4ESkp7heFscREzPUAo8BZUAAAFob09pzg"

    token = getAccessToken(client_id, code)

    #access_token = "4pksUn1J44D9zri-vrx3v47sCfJBPnzYVZX6dQoqAucAAAFobzvkQw"
    result = sendText(token['access_token'], "hello")
    print(result)
    #print(token)
finally:
    print("end")
    #driver.quit()

