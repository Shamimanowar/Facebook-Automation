import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from pynput.keyboard import Key, Controller
from pynput import keyboard as board, mouse as ms

# username = input('Enter facebook username, email or phone number : ')

username = ''
password = ''

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path='G:\WebDriverSel/chromedriver.exe')
driver = webdriver.Chrome()

driver.get('https://www.facebook.com')

txt_username = driver.find_element(By.ID, 'email')
txt_username.send_keys(username)

txt_password = driver.find_element(By.ID, 'pass')
txt_password.send_keys(password)
time.sleep(1)
btn_login = driver.find_element(By.NAME, 'login')
time.sleep(1)
btn_login.click()
time.sleep(2)

page_links = ['Python-BOT-104540468791798',
              # 'javascriptJS',
              # 'computerprogrammingbook',
              'web.dev.and.prog/',
              'amazonwebservices/'
              ]
keyboard = board.Controller()
mouse = ms.Controller()

for link in page_links:
    time.sleep(2)

    driver.get('https://www.facebook.com/' + link)
    for i in range(2):
        time.sleep(1)
        keyboard.press('j')
        keyboard.release('j')
        time.sleep(1)

        # This part is for just like
        keyboard.press('l')
        keyboard.release('l')
        time.sleep(1)
        keyboard.press(board.Key.enter)
        keyboard.release(board.Key.enter)

        keyboard.press('c')
        keyboard.release('c')
        time.sleep(1)

        keyboard.type('Hello, this is an automatic comment by python script !')
        time.sleep(1)
        keyboard.press(board.Key.enter)
        keyboard.release(board.Key.enter)

        # the mouse not to focus comment box
        mouse.press(ms.Button.left)
        # mouse.release(ms.Button.left)
        time.sleep(1)


time.sleep(5)
print('Program has been terminated !')
