from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os

from selenium.webdriver.firefox.options import Options

def create_firefox_driver(executable_name):
    working_directory = os.getcwd()
    path = os.path.join(working_directory, executable_name)
    service = Service(executable_path=path)

    """Change Firefox Download Directory Source: https://stackoverflow.com/a/69974916"""
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", working_directory)

    return webdriver.Firefox(service=service, options=options)

def locate_element(driver, by_type, value, seconds=30):
    return WebDriverWait(driver, seconds).until(expected_conditions.presence_of_element_located((by_type, value)))

def locate_elements(driver, by_type, value, seconds=30):
    return WebDriverWait(driver, seconds).until(expected_conditions.presence_of_all_elements_located((by_type, value)))

def wait(driver, seconds=3):
    try:
        locate_element(driver, By.NAME, "Halt program execution for some time before proceeding", seconds)

    except:
        return

"""Function Source: https://stackoverflow.com/a/56570364"""
def get_downloaded_file_name(driver, seconds_per_download=5):
    driver.execute_script("window.open()")
    wait(driver)
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("about:downloads")

    while True:
        try:
            wait(driver, seconds_per_download)
            file_name = driver.execute_script("return document.querySelector('#contentAreaDownloadsView .downloadMainArea .downloadContainer description:nth-of-type(1)').value")
            break

        except:
            continue

    driver.switch_to.window(driver.window_handles[-2])
    wait(driver)
    return file_name
