from selenium import webdriver
import time
browser = webdriver.Chrome("/home/jarbas/projects/ai-chess/chromedriver")
browser.get('https://www.chess.com/games/alexander-alekhine')

any_page_left = True

while any_page_left:
    checkboxes = browser.find_elements_by_class_name("master-games-checkbox")
    download = browser.find_element_by_class_name("master-games-download-button")

    try:
        nextpage = browser.find_element_by_class_name("pagination-next")
    except:
        any_page_left = False
    
    print(any_page_left)
    
    for i in range(len(checkboxes)):
        time.sleep(0.2)
        checkboxes[i].click()
        #browser.execute_script(f"arguments[0].click();", checkboxes[i])
        time.sleep(0.2)
        #browser.execute_script(f"arguments[0].click();", checkboxes[i-1]) if i > 0 else None
        checkboxes[i-1].click() if i > 0 else None
        time.sleep(0.2)
        #browser.execute_script("arguments[0].click();", download)
        # download.click()

    if i == len(checkboxes) - 1 and any_page_left:
        #browser.execute_script("arguments[0].click();", nextpage)
        nextpage.click()
        time.sleep(2)