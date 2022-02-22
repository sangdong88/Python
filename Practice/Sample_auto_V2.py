import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import win32com.client
import getpass

try:
    start0 = time.time()

    # for num_py in range(1,10):
    start = time.time()
    # print(num_py)

    # 크롬 실행, 템포 주소 입력, 최대화
    driver = webdriver.Chrome('Chromedriver')
    driver.maximize_window()
    driver.get('https://tempo.app.corp/TEMPO_P6_PROD/')

    # Tempo login
    WebDriverWait(driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div/div')))
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div/div').click()

    pyautogui.write("parkj001")
    pyautogui.hotkey('tab')
    pyautogui.write("Pjh0147143@13")
    pyautogui.hotkey('enter')

    # LTI Management 진입 및 대기
    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.ID, "cga418")))
    driver.find_element(By.ID, 'cga418').click()
    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.ID, "object381028")))

    # LTI 정보, 이름, 요청 부서 재입력
    driver.find_element(By.ID, 'object485710').send_keys(
        Keys.CONTROL, 'a', Keys.BACKSPACE)
    time.sleep(0.5)
    driver.find_element(By.ID, 'object485710').send_keys(Keys.ENTER)
    time.sleep(5)

    driver.find_element(By.ID, 'object485710').send_keys('AFO_JANGAN')
    time.sleep(0.5)
    driver.find_element(By.ID, 'object485710').send_keys(Keys.ENTER)
    time.sleep(5)
    # WebDriverWait(driver, 100).until(expected_conditions.invisibility_of_element_located((By.ID, "Freezer")))

    driver.find_element(By.ID, 'object381028').send_keys(
        Keys.CONTROL, 'a', Keys.BACKSPACE, Keys.ENTER)
    time.sleep(5)
    #WebDriverWait(driver, 100).until(expected_conditions.invisibility_of_element_located((By.ID, "Freezer")))

    driver.find_element(By.ID, 'object381710').send_keys(
        Keys.CONTROL, 'a', Keys.BACKSPACE, Keys.ENTER)
    time.sleep(5)
    #WebDriverWait(driver, 100).until(expected_conditions.invisibility_of_element_located((By.ID, "Freezer")))

    if driver.find_element(By.XPATH, '//*[@id="string640002"]/tbody/tr/td/div').text != 'All LTI*':
        driver.find_element(By.ID, 'rw784016').click()
        WebDriverWait(driver, 100).until(
            expected_conditions.visibility_of_element_located((By.ID, "cga1484056")))
        driver.find_element(By.ID, 'cga1484056').click()
        time.sleep(7.5)

    driver.find_element(By.ID, 'rw128002').click()
    time.sleep(1)
    #WebDriverWait(driver, 100).until(expected_conditions.visibility_of_element_located((By.ID, "cga728730")))
    driver.find_element(By.ID, 'cga728730').click()
    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.ID, "object596412")))
    driver.find_element(By.ID, 'object596412').send_keys(Keys.ENTER)

    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.ID, "mouseline")))
    a = driver.find_element(By.ID, 'mouseline').text
    download_percent = int(a[-3:-1])
    print(download_percent)

    while download_percent < 94:
        if download_percent >= 94 or download_percent == 0:
            break
        time.sleep(1)
        download_percent = int(driver.find_element(
            By.ID, 'mouseline').text[-3:-1])
        print(download_percent)

    print("Wait next step")
    time.sleep(15)
    driver.quit()
    print('Quit browser')

    print("Start sample management section")
    username = getpass.getuser()
    folder_path = 'C:\\Users\\'+username+'\\Downloads\\'
    each_file_path_and_gen_time = []
    for each_file_name in os.listdir(folder_path):
        each_file_path = folder_path + each_file_name
        each_file_gen_time = os.path.getctime(each_file_path)
        each_file_path_and_gen_time.append(
            (each_file_path, each_file_gen_time))
        most_recent_file = max(
            each_file_path_and_gen_time, key=lambda x: x[1])[0]
    print(most_recent_file)

    driver = webdriver.Chrome("Chromedriver")
    driver.get('http://10.162.2.46:8080/')

    WebDriverWait(driver, 100).until(
        expected_conditions.visibility_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, 'username').send_keys('jin-ho.park')
    driver.find_element(By.NAME, 'password').send_keys('jin-ho.park')
    driver.find_element(
        By.CSS_SELECTOR, '#user-login-5 > div > div.col-md-6.login-container.bs-reset > div.login-content > form > div:nth-child(3) > div.col-sm-4 > div > div > select > option:nth-child(2)').click()
    driver.find_element(By.ID, 'btn-user-login').click()
    print('Login done')

    driver.maximize_window()
    WebDriverWait(driver, 600).until(
        expected_conditions.visibility_of_element_located((By.ID, "menuitem-1081-iconEl")))
    driver.find_element(By.ID, 'menuitem-1081-iconEl').click()
    print('first step')
    WebDriverWait(driver, 600).until(
        expected_conditions.visibility_of_element_located((By.ID, "button-1161")))
    driver.find_element(By.ID, 'button-1161').click()
    print('second step')
    WebDriverWait(driver, 600).until(
        expected_conditions.visibility_of_element_located((By.ID, "uploadFileBtn")))
    driver.find_element(By.ID, 'uploadFileBtn').send_keys(most_recent_file)
    print('Insert file done')
    time.sleep(1)
    UPLOAD_FILE = driver.find_element(
        By.LINK_TEXT, 'Upload File').get_attribute('id')
    driver.find_element(By.ID, UPLOAD_FILE).click()
    print('upload click')
    start2 = time.time()
    WebDriverWait(driver, 3600).until(
        expected_conditions.visibility_of_element_located((By.ID, "button-1014-btnEl")))
    driver.find_element(By.ID, 'button-1014-btnEl').click()
    print('Done')
    print("total time : ", time.time()-start)
    print("time : ", time.time()-start2)
    driver.quit()
    print('Quit browser')

    ex_time = time.time()-start0\

    # Send success mail.
    mail_subject = "Beta tester - [Sample management system]LTI Update Automatic Notification"
    mail_body = """[Sample management system]LTI Update Automatic Notification"""
    mail_To = "AHN Sang-Hyuk <sang-hyuk.ahn@faurecia.com>; JUNG Chang-Yeon <chang-yeon.jung@faurecia.com>; JANG Kwang-Soon <kwang-soon.jang@faurecia.com>; KIM Dong-Wok <dong-wok.kim@faurecia.com>; LEE Sang-Deok <sang-duk.lee@faurecia.com>; LEE Sang-Dong <sang-dong.lee@faurecia.com>; LEE Tae-Young <tae-young.lee@faurecia.com>; PARK Jin-Ho <jin-ho.park@faurecia.com>; PARK Seong-Han <seong-han.park@faurecia.com>; SEO Jung-Min <jung-min.seo@faurecia.com>; SHIN Byeong-Uk <byeong-uk.shin@faurecia.com>"
    mail_CC = ""

    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    new_mail = obj.CreateItem(olMailItem)

    new_mail.Subject = mail_subject
    new_mail.HTMLBody = mail_body
    new_mail.To = mail_To
    new_mail.CC = mail_CC

    new_mail.Send()

except:
    print("error")
    # Send error mail.
    mail_subject = "Beta tester - [Sample management system]Automatic error"
    mail_body = """Automatic error was occurred. Please check the system."""
    mail_To = "sang-hyuk.ahn@faurecia.com"
    mail_CC = ""

    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    new_mail = obj.CreateItem(olMailItem)

    new_mail.Subject = mail_subject
    new_mail.HTMLBody = mail_body
    new_mail.To = mail_To
    new_mail.CC = mail_CC

    new_mail.Send()
