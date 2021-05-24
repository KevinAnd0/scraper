from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = r'C:\Windows\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://rattsinfosok.domstol.se/lagrummet/SokAvgorande.jsp?tmpMenyVal=enkel&tmpFelFocus=false&tmpBesokStatistikSparad=true&tmpDisabledReferat=&oldSokDomstol=&oldSokSortering=&oldSokSenaste=&slctDomstol=ALLAMYND&txtAvgDatumFran=&txtAvgDatumTill=&txtRubrikText=konsument')

try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sokResultat")))
    current_win = driver.current_window_handle
    links = main.find_elements_by_tag_name('a')
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lankNasta1')))
    print(button)
    # button.click()
    time.sleep(5)

    # for i in range(len(links)):
#     links[0].click()
#     windows = driver.window_handles
#     print('check')
#     driver.switch_to.window(windows[1])
# #     time.sleep(3)
# #     driver.execute_async_script("window.print();").send_key(Keys.TAB)
#     driver.switch_to.frame(driver.find_element_by_name('DetaljFrame2'))
#     text = driver.find_elements_by_class_name('textDetaljbild')
#     text_lst = []
#     case_number = ""
#     for i in range(len(text)):
#         text_lst.append(text[i].text + ' \n')
#         if str(text[i]).lower() == 'målnummer:':
#             case_number = text[i+1]
#             print(case_number)
#     # file = open(fr"C:\git\scraped\dom.txt", "a")
#     # file.writelines(text_l)
#     # file.close()
#     # time.sleep(3)
#     driver.close()
except:
    # driver.quit()
    pass
finally:
    driver.quit()