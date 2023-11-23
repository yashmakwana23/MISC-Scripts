from multiprocessing.connection import wait
from operator import truediv
from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from http import client
from sqlite3 import Row
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.chrome.options import Options
import json

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
Option = Options()
Option.headless = True
driver= webdriver.Chrome(executable_path="C:/chromedriver.exe",options=Option)

creds= ServiceAccountCredentials.from_json_keyfile_name("credts.json",scope)
client= gspread.authorize(creds)
b=0
gtv= open('gametv/gtvt.json',"r+")
data= json.load(gtv)
token=data["token_uri"]
sheet= client.open("Halero Approval Sheet").sheet1
col= sheet.col_values(1)
for a in col:
    b=b+1
    driver.get(f"{a}?token={token}&user_id=")
    time.sleep(5)
    try:
        folder=driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[2]/span/div/span')
        sheet.append_row(values=[folder.text],table_range=f'B{b}')
    except:
        print("excepted")