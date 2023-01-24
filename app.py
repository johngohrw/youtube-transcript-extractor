from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import  ActionChains
import time

WAIT_DURATION = 20

# wait until presence of element located, then perform a click
def waitAndClickXPath(xpath, driver):
    wait = WebDriverWait(driver, WAIT_DURATION)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    ActionChains(driver)\
        .click(elem)\
        .perform()
    return elem

# wait until presence of element located, then return the elem
def waitElemXPath(xpath, driver):
    wait = WebDriverWait(driver,  WAIT_DURATION)
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.youtube.com/watch?v=AzC-_VJ0uiI") # goto a video

three_dots_button_el = waitElemXPath('//div[@id="top-row"]//div[@id="actions"]//yt-button-shape//button[@aria-label="More actions"]', driver)

ActionChains(driver)\
        .click(three_dots_button_el)\
        .perform()

# time.sleep(1)

show_transcript_button_el = waitElemXPath('//tp-yt-paper-listbox[@id="items"]//ytd-menu-service-item-renderer[@aria-selected="false"]', driver)

ActionChains(driver)\
        .click(show_transcript_button_el)\
        .perform()

# time.sleep(1)
timestampsList = waitElemXPath('//ytd-transcript-segment-list-renderer//div[@id="segments-container"]//ytd-transcript-segment-renderer', driver)
time.sleep(1)

timestampElements = driver.find_elements_by_xpath('//ytd-transcript-segment-list-renderer//div[@id="segments-container"]//ytd-transcript-segment-renderer//div[@class="segment-timestamp style-scope ytd-transcript-segment-renderer"]')
transcriptTextElements = driver.find_elements_by_xpath('//ytd-transcript-segment-list-renderer//div[@id="segments-container"]//ytd-transcript-segment-renderer//yt-formatted-string')

timestamps = []

for i in range(len(timestampElements)):
    timestamps.append([timestampElements[i].text, transcriptTextElements[i].text])

# probably want to return timestamps here

# just printing
for i in range(len(timestamps)):
    print(timestamps[i])

time.sleep(100)
driver.quit()

# waitAndClickXPath('//tp-yt-paper-listbox[@id="items"]//ytd-menu-service-item-renderer', driver)
# //ytd-transcript-segment-list-renderer//div[@id="segments-container"]//ytd-transcript-segment-renderer//div[@class="segment-timestamp"]



