from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from driver import create_firefox_driver, locate_element, locate_elements, wait, get_downloaded_file_name

import environment_info

def login_and_download_zybook_grades():
    driver = create_firefox_driver("geckodriver.exe")
    driver.get("https://learn.zybooks.com/signin")

    try:
        locate_element(driver, By.CLASS_NAME, "card-header-large")
        zybook_input_fields = locate_elements(driver, By.CLASS_NAME, "zb-input")
        zybook_email_field = zybook_input_fields[0]
        zybook_password_field = zybook_input_fields[1]

        zybook_email_field.send_keys(environment_info.zybook_email)
        zybook_password_field.send_keys(environment_info.zybook_password)

        zybook_sign_in_button = locate_element(driver, By.CLASS_NAME, "signin-button")
        zybook_sign_in_button.click()

    except:
        return
    
    locate_elements(driver, By.CLASS_NAME, "zybooks-section-header")

    wait(driver)
    # driver.get("https://learn.zybooks.com/zybook/"+ environment_info.zybook_identifier +"?selectedPanel=assignments-panel")
    driver.get("https://learn.zybooks.com/zybook/"+ environment_info.zybook_identifier)

    while True:
        try:
            zybook_tab_buttons = locate_elements(driver, By.CLASS_NAME, "full-tab")
            zybook_assignment_tab_button = zybook_tab_buttons[-1]
            zybook_assignment_tab_button.click()
            break

        except:
            continue

    zybook_assignments = locate_elements(driver, By.CLASS_NAME, "assignment-summary")

    # Defaults to latest past assignment
    selected_zybook_assignment_index = -1
    selected_zybook_assignment_button = zybook_assignments[selected_zybook_assignment_index]
    selected_zybook_assignment_button.click()

    zybook_assignment_name_header = locate_element(driver, By.CLASS_NAME, "my-0")
    zybook_assignment_name = zybook_assignment_name_header.text

    report_button = locate_element(driver, By.XPATH, "//button[contains(@class, 'zb-button')]//*[contains(., 'Report')]/..")
    report_button.click()

    download_report_button = locate_element(driver, By.XPATH, "//button[contains(@class, 'zb-button')]//*[contains(., 'Download assignment report')]/..")
    download_report_button.click()

    wait(driver)
    downloaded_file_name = get_downloaded_file_name(driver)
    driver.quit()
    return zybook_assignment_name, downloaded_file_name
