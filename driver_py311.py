import os
import random
import time

import urllib3
from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver

if __name__ == "__main__":
    print("input start and end:\n")
    a,b = (int(i) for i in (input().split()))
    urllib3.disable_warnings()
    login_url = ''
    data = {
        "username": "USER",
        "password": 
    }
    options = webdriver.ChromeOptions()
    options.binary_location = r"E:\chrome-win\chrome.exe"
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    url_root = ""
    driver.get(login_url)
    driver.refresh()
    driver.maximize_window()
    driver.find_element(by="name", value="user_name").send_keys(data.get("username"))
    driver.find_element(by="name", value="user_password").send_keys(data.get("password"))
    # driver.find_element_by_name("user_name").send_keys(data.get("username"))
    # driver.find_element_by_name("user_password").send_keys(data.get("password"))
    time.sleep(25)
    # url_list = soup.find_all('img', {'decoding': 'async'})
    post = a
    while(post<b):
        try:
            url = url_root + post.__str__()
            post+=1
            driver.get(url)
            print(url)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            url_list = soup.find_all('img', {'decoding': 'async'})
            if len(url_list) == 0:
                continue
            for j in range(0, len(url_list)):
                url_list[j] = url_list[j]['src']
            folders = re.findall('<title>(.*?)</title>', page_source)
            folders2 = re.findall('<source type="video/mp4" src="(.*?)">', page_source)
            if len(folders2) > 0:
                for ff in folders2:
                    url_list.append(ff[:-4])
            if len(url_list) == 1:
                print("jump")
                continue
            folder = random.randint(0, 100000).__str__()
            if len(folders) > 0:
                folder = folders[0].replace(' ', '')
                if not os.path.exists(folder):
                    os.mkdir(folder)
            else:
                os.mkdir(folder)
            length = url_list.__len__()-3
            if(length>2):
                post += length
            for url in url_list:
                print(url)
                response = requests.get(url,verify=False)
                filename = url.split('/')[-1]
                with open('./' + folder + '/' + '%s' % filename, "wb") as f:
                    f.write(response.content)
        except:
            continue
