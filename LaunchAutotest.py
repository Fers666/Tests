from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys

#Проверка на наличие элемента на странице
def check_exists_by_xpath(self,driver):
    try:
        driver.find_element_by_xpath(self)
    except NoSuchElementException:
        return self.assertTrue(False)
    return True

def check_exists_by_id(self,driver):
    try:
        driver.find_element_by_id(self)
    except NoSuchElementException:
        return False
    return True

#import str in int
def str_in_int (data) :
    list_num = []
    for i in data:
        try:
            num = int(i)
            list_num.append(num)
        except ValueError:
            continue
    return list_num

#User choice (Выбор пользователя)
def user_choice ():
    # input (Choice name of logins and passwords)
    f_data='Settings.txt'
    f = read_data(f_data)
    user = int(f[1])
    if user == 1:
        filename = 'Admin.txt'
    elif user == 2:
        filename = 'Logists.txt'
    elif user == 3:
        filename = 'TK.txt'
    elif user == 4:
        filename = 'SamMbTK.txt'
    else:
        filename = 'test.txt'
    return filename

#reading a file and converting to an array( конверктация строк файла в массив )
def read_data(filename):
    stops = []
    with open(filename,  'r') as fobj:
       for line in fobj:
           stops.append(line.strip())
    return stops

#authorization autotest (атотест авторизации на сайте)
def test_autorization(login,password):
    #shief window
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # initialize the Chrome driver
    driver = webdriver.Chrome("C:\\Users\\Евген\\Desktop\\Python\\work\\selenium\\chromedriver.exe")

    driver.get("https://10.32.0.22/")

    driver.minimize_window()
    #
    driver.find_element_by_id("details-button").click()
    driver.find_element_by_id("proceed-link").click()

    # Autorization
    driver.find_element_by_id("email").send_keys(login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name('MuiButton-label').click()
    time.sleep(3)
    if driver.current_url == "https://10.32.0.22/main/tc":
        result = ' testname : autorization; result : Success; '
        print(result)
    elif driver.current_url == "https://10.32.0.22/main/logist":
        result = ' testname : autorization; result : Success; '
        print(result)
    else :
        result = ' testname : autorization;  result : Login ERROR'
        print(result)
    return result

#writing to logfile (запись лог-файла)
def writing_file (result):
    now = datetime.now()
    date_time = now.strftime("date : %Y-%m-%d  %H:%M:%S ;")
    file = open('ErrorLogs.txt', 'a')
    file.write(date_time)
    file.write(result)
    file.write('\n')
    file.close()

#planing autotest
def test_planing (login,password):
    # shief window
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # initialize the Chrome driver
    driver = webdriver.Chrome("C:\\Users\\Евген\\Desktop\\Python\\work\\selenium\\chromedriver.exe")

    driver.get("https://10.32.0.22/")

    driver.maximize_window()
    driver.minimize_window()
    #
    driver.find_element_by_id("details-button").click()
    driver.find_element_by_id("proceed-link").click()

    # Autorization
    driver.find_element_by_id("email").send_keys(login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name('MuiButton-label').click()
    time.sleep(3)
    if driver.current_url == "https://10.32.0.22/main/tc":
        result = ' testname : autorization; result : Success; '
        print(result)
    elif driver.current_url == "https://10.32.0.22/main/logist":
        result = ' testname : autorization; result : Success; '
        print(result)
    else :
        result = ' testname : autorization;  result : Login ERROR'
        print(result)

    #planing autotest
    # planing autotest
    driver.refresh()
    time.sleep(1)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Планирование подачи ТС')]"))).click()
    time.sleep(1)

    #Проверка ранее поданых данных
    x_p = 'edit-btn'
    x_p_conf = check_exists_by_id(x_p,driver)
    time.sleep(1)
    if x_p_conf == True :
        x_res = 'testname : Planing; result : Planing was confirmed '
        print(x_res)
        return x_res
    else :
        # получение актуального поля ID
        chanel_select = 'channel-select_'
        route_select = 'route-select_'
        cashcollection_select = 'cashcollection-select_'
        menu_id = 'menu-'

        chanel = driver.find_element_by_xpath(
            "//div[contains(@class, 'MuiSelect-root') and contains(@aria-labelledby, 'driver')]").get_attribute(
            'aria-labelledby')
        num = str_in_int(chanel)
        b = int(''.join(map(str, num)))

        for j in range(b + 1):
            if j == b:
                now_chanel_select = chanel_select + str(j)
                now_route_select = route_select + str(j)
                now_cashcollection_select = cashcollection_select + str(j)
                now_menu_id = menu_id + str(j)
        # ___________________________________

        driver.find_element_by_id(now_chanel_select).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Опт')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'MuiPopover-root') and @id='" + now_menu_id + "']"))).click()

        driver.find_element_by_id(now_route_select).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Москва')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'MuiPopover-root') and @id='" + now_menu_id + "']"))).click()

        driver.find_element_by_id(now_cashcollection_select).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'ДА')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'MuiPopover-root') and @id='" + now_menu_id + "']"))).click()

        time.sleep(2)
        # Поиск следующей строк ячеек

        i = 1
        while i == 1:
            b += 1
            for j in range(10000):
                if j == b:
                    next_chanel_select = chanel_select + str(j)
                    next_route_select = route_select + str(j)
                    next_cashcollection_select = cashcollection_select + str(j)
                    next_menu_id = menu_id + str(j)
                    t = check_exists_by_id(next_chanel_select, driver)
                    print(next_chanel_select)
                    if t == False:
                        continue
                    else:
                        i = 5

        # next click
        driver.find_element_by_id(next_chanel_select).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Розница')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'MuiPopover-root') and @id='" + next_menu_id + "']"))).click()

        driver.find_element_by_id(next_route_select).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'МО')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'MuiPopover-root') and @id='" + next_menu_id + "']"))).click()

        driver.find_element_by_id(next_cashcollection_select).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'НЕТ')]"))).click()
        # ready
        driver.find_element_by_id('confirm-btn').click()
        data = driver.find_element_by_id('alert-dialog-title').text

        # read ERROR
        car = '2 шт'
        if car in data:
            pre_p_result = True
        else:
            pre_p_result = False

        driver.find_element_by_id('confirm-btn-dialog').click()

        time.sleep(2)

        x_p = 'edit-btn'
        x_p_result = check_exists_by_id(x_p, driver)
        print(x_p_result)

        if x_p_result == False and pre_p_result == False:
            p_p_result = ' testname : Planing; result : Planing Error; Preplaning ERROR; '
            print(p_p_result)
        elif pre_p_result == False and x_p_result == True:
            p_p_result = ' testname : Planing; result : Planing Success; Preplaning ERROR; '
            print(p_p_result)
        elif pre_p_result == True and x_p_result == False:
            p_p_result = ' testname : Planing; result : Planing Error; Preplaning Success; '
            print(p_p_result)
        else:
            p_p_result = ' testname : Planing; result : Planing Success; Preplaning Success; '
            print(p_p_result)
        return p_p_result

        driver.refresh()


#main(основная)
#choice user
filename = user_choice()

#reading logins file
f = read_data(filename)
login = f[0]
password = f[1]

#launch authorization autotest
result_a = test_autorization(login,password)

#writing to logfile
writing_file(result_a)

#launch planing autotest
result_p = test_planing(login,password)

#writing planing autotest
writing_file(result_p)