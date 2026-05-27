from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from driver import create_firefox_driver, get_downloaded_file_name, locate_element, wait

import environment_info

import os

def export_canvas_gradebook(driver):
    wait(driver)
    driver.get("https://"+ environment_info.canvas_school_acronym +".instructure.com/courses/"+ environment_info.canvas_course_identifier +"/gradebook")

    
    export_button = locate_element(driver, By.ID, "Menu__label_2")
    export_button.click()

    export_entire_gradebook_button = locate_element(driver, By.CLASS_NAME, "css-1g68bbu-menuItem")
    export_entire_gradebook_button.click()

    canvas_gradebook_file_name = get_downloaded_file_name(driver)
    return canvas_gradebook_file_name

def get_current_authentication_code(driver):
    try:
        authentication_code = locate_element(driver, By.ID, "idRichContext_DisplaySign", 5)
        """Source for line below: https://stackoverflow.com/a/2084628"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nCode: " + authentication_code.text)

    except:
        return

def get_new_authentication_code(driver):
    try:
        resend_request = locate_element(driver, By.ID, "idA_SAASDS_Resend", 5)
        resend_request.click()

    except:
        try:
            resend_request = locate_element(driver, By.ID, "idA_SAASTO_Resend", 5)
            resend_request.click()

        except:
            return

def login_and_export_canvas_gradebook():
    driver = create_firefox_driver("geckodriver.exe")
    # NOTE: This works for only one type of login page
    driver.get("https://myapps.microsoft.com/")

    email_field = locate_element(driver, By.NAME, "loginfmt")
    email_field.send_keys(environment_info.canvas_email, Keys.RETURN)
    
    wait(driver)
    password_field = locate_element(driver, By.NAME, "passwd", 60)
    password_field.send_keys(environment_info.canvas_password, Keys.RETURN)

    while driver.title != "My Apps":
        get_current_authentication_code(driver)
        get_new_authentication_code(driver)

    canvas_gradebook_file_name = export_canvas_gradebook(driver)

    return canvas_gradebook_file_name, driver

def import_grades(file_path, driver):
    import_button = locate_element(driver, By.ID, "import_btn")
    import_button.click()

    browse_files_button = locate_element(driver, By.ID, "gradebook_upload_uploaded_data")
    browse_files_button.send_keys(file_path)

    upload_data_button = locate_element(driver, By.CLASS_NAME, "Button--primary")
    upload_data_button.click()

    print("\nUpload complete. Please manually review and upload grades when you're ready.")
