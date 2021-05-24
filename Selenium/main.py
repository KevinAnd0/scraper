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
    next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lankNasta1')))
    while next_button:
        search_main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sokResultat")))
        parent_win = driver.current_window_handle
        links = search_main.find_elements_by_tag_name('a')

        for i in range(len(links)):
            links[i].click()
            time.sleep(1)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            driver.switch_to.frame(driver.find_element_by_name('DetaljFrame2'))
            text = driver.find_elements_by_class_name('textDetaljbild')
            text_lst = []
            case_number = ""

            for j in range(len(text)):
                if text[j].text == 'Målnummer:' or text[j].text == 'Domsnummer:':
                    if case_number == text[j + 1]:
                        break
                    case_number = text[j + 1].text
                if j % 2 != 0:
                    text_lst.append(text[j].text + ' \n')
                else:
                    text_lst.append(text[j].text)

            if case_number:
                file = open(fr"C:\git\scraped\mål_{case_number}.txt", "a")
                file.writelines(text_lst)
                file.close()
            driver.close()
            driver.switch_to.window(parent_win)
            
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lankNasta1')))
        time.sleep(1)
        next_button = button
        button.click()
        time.sleep(1)

except:
    pass
# finally:
    # driver.quit()