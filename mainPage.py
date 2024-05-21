import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://jusan.kz/')
driver.maximize_window()
driver.implicitly_wait(10)


def check_search():
    try:
        # Click search button
        driver.find_element(By.CLASS_NAME, 'desktop-header_search_container__0PRER').click()
        # Find input field
        input_search = driver.find_element(By.CLASS_NAME, 'ais-SearchBox-input')
        search_text = 'bank'
        input_search.send_keys(search_text)
        time.sleep(2)
        results = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')
        print(driver.find_element(By.CLASS_NAME, 'search-content_search_result_probably__qIEF3').text)
        for result in results:
            if search_text.lower() in result.text.lower():
                print(result.text)
            else:
                print('Not found')
        driver.find_element(By.ID, 'search-icon').click()
        driver.implicitly_wait(10)

        driver.find_elements(By.CLASS_NAME, 'search-result_categoryFaq__o5kVI')[0].click()
        # Find opened title use CSS selector
        wait = WebDriverWait(driver, 10)
        title = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.accordion-button[aria-expanded='true']"))
        )
        # title = driver.find_element(By.CSS_SELECTOR, "button.accordion-button[aria-expanded='true']")
        print(title.text)
        description = (driver.find_element(By.CSS_SELECTOR, 'div.accordion-collapse.collapse.show')
                       .find_element(By.CLASS_NAME, 'accordion-body')
                       .find_element(By.TAG_NAME, 'div')
                       .find_element(By.TAG_NAME, 'p'))
        print(description.text)
        print(search_text.lower() in title.text.lower() or search_text in description.text.lower())
        driver.implicitly_wait(10)

        driver.back()

        # Check search categories options
        # search_categories = (driver.find_element(By.CLASS_NAME, 'search-categories-options_list__izSo5')
        #                      .find_elements(By.TAG_NAME, 'li'))
        # for i in range(len(search_categories)):
        # try:
        #     print(f'Clicked {search_categories[0].text}')

            # option = wait.until(
            #     EC.element_to_be_clickable(search_categories[i])
            # )
            # option.click()
            # search_categories[0].click()
            # time.sleep(5)
            # driver.execute_script("window.history.go(-1)")
            # driver.back()
            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-categories-options_list__izSo5')))
            # time.sleep(5)
        #     print(f'Closed {search_categories[0].text}')
        # except Exception as error:
        #     print(f'Error in search categories {error}')
    except Exception as error:
        print(error)


def check_change_language():
    for i in range(0, 6, 2):
        driver.find_element(By.CLASS_NAME, 'desktop-header_language_container__9uasj').click()
        driver.implicitly_wait(10)
        languages = driver.find_element(By.CLASS_NAME, 'language-box').find_elements(By.TAG_NAME, 'a')
        # Choose the language
        print(f'Language {languages[i].text} selected')
        languages[i].click()
        driver.implicitly_wait(10)


def check_map():
    pass


def check_visually_impaired():
    driver.find_element(By.ID, 'bvi_open').click()
    driver.implicitly_wait(10)

    settings = driver.find_elements(By.CLASS_NAME, 'n3__vision__settings-group__buttons')

    # Change font size
    for i in range(3):
        settings[0].find_elements(By.TAG_NAME, 'button')[i].click()
        print('Changed font size')
        driver.implicitly_wait(10)

    # Change color
    for i in range(3):
        settings[1].find_elements(By.TAG_NAME, 'button')[i].click()
        print('Changed color')
        driver.implicitly_wait(10)

    # Off images
    settings[2].find_elements(By.TAG_NAME, 'button')[0].click()
    print('Off images')
    driver.implicitly_wait(10)
    # time.sleep(2)
    # On images
    settings[2].find_elements(By.TAG_NAME, 'button')[1].click()
    print('On images')
    driver.implicitly_wait(10)

    # On voice assistant
    voice = driver.find_element(By.CLASS_NAME, 'desktop-header_voice_btn__WjhsO')
    print('On voice assistant')
    voice.find_elements(By.TAG_NAME, 'button')[0].click()
    driver.find_element(By.CLASS_NAME, 'speech-modal_close_btn_speech__NdjNe').click()
    driver.implicitly_wait(10)
    # JavaScript to select the text
    select_text_script = """
        var element = arguments[0];
        var range = document.createRange();
        var selection = window.getSelection();
        range.selectNodeContents(element);
        selection.removeAllRanges();
        selection.addRange(range);
    """
    # Check voice assistant
    select_element = driver.find_element(By.CLASS_NAME, 'react-vision-label')
    driver.execute_script(select_text_script, select_element)
    driver.find_element(By.CLASS_NAME, 'voice_speech_volume_off__Bb1LF').click()
    # voice_speech_volume_on__2_U2I
    time.sleep(5)

    # Click regular version
    regular_version = driver.find_elements(By.CLASS_NAME, 'n3__vision__action-button')[1]
    print(f'Choose {regular_version.text}')
    regular_version.click()
    driver.implicitly_wait(10)

    # Close the visually impaired
    driver.find_element(By.CLASS_NAME, 'desktop-header_react_vision_panel_close_btn__HgxBj').click()


def check_link_content():
    pass


def check_link_in_the_footer():
    pass


# check_visually_impaired()
check_search()
time.sleep(100)
