from selenium import webdriver
import time
from datetime import date
# import sys

def certificateautomation(sname, semail, scourse, sduration, scompletion, sscore):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    web = webdriver.Chrome(options=options) # should have chromedriver.exe file in the same folder
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSf9kz59-k87gT3ImgsS9KU1S1muNOfDipoercMGM4T0Bqx87A/viewform')
    # web.maximize_window()
    time.sleep(3)

    name = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(sname)

    email = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email.send_keys(semail)

    course = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    course.send_keys(scourse)

    duration = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    duration.send_keys(sduration)

    completion = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    completion.send_keys(scompletion)

    score = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    score.send_keys(sscore)

    submit = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

sname = 'Christopher Chanobel' # sys.argv[0]
semail = 'example@gmail.com' # sys.argv[1]
scourse = 'Web Development' # sys.argv[2]
sduration = '14hrs' # sys.argv[3]
sscore = '80' # sys.argv[4]
scompletion = str(date.today())

certificateautomation(sname, semail, scourse, sduration, scompletion, sscore)
