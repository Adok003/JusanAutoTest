import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jusan.kz/')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_elements(By.CLASS_NAME, 'nav-item')[0].click()
driver.implicitly_wait(5)
# Jusan Family
items = driver.find_elements(By.CLASS_NAME, 'dropdown-item')
print(f'Clicked button {items[0].text}')
items[0].click()

# # Scrolling page to top
# time.sleep(2)
# scroll_to_top = driver.find_element(By.CLASS_NAME, 'scroll-to-top_scrollToTopButton___Zu7y')
# scroll_to_top.click()
# time.sleep(2)

# Show more details in the Родителям
driver.execute_script('window.scrollBy(0, 1500);')
time.sleep(2)
more_details = driver.find_elements(By.CLASS_NAME, 'jusan-family-card-steps_jusan_family_card_steps_info__R7_H0')
for i in range(3):
    more_details[i].find_element(By.TAG_NAME, 'button').click()
    print(f"Opened details '{more_details[i].find_element(By.TAG_NAME, 'h4').text}'")
    driver.implicitly_wait(10)
    # time.sleep(2)
    # Close the details
    driver.find_element(By.CLASS_NAME, 'jusan-family-card-steps_close_btn__flv_V').click()

# Show more details in the Детям
driver.execute_script('window.scrollBy(0, 1200);')
time.sleep(2)
for i in range(3, 6):
    more_details[i].find_element(By.TAG_NAME, 'button').click()
    print(f"Opened details '{more_details[i].find_element(By.TAG_NAME, 'h4').text}'")
    driver.implicitly_wait(10)
    # time.sleep(2)
    # Close the details
    driver.find_element(By.CLASS_NAME, 'jusan-family-card-steps_close_btn__flv_V').click()

# Scrolling page to top
time.sleep(2)
scroll_to_top = driver.find_element(By.CLASS_NAME, 'scroll-to-top_scrollToTopButton___Zu7y')
scroll_to_top.click()
time.sleep(2)

# Click the Родителям
for i in range(2, -1, -1):
    driver.execute_script('window.scrollBy(0, 30);')
    time.sleep(2)
    text_link = (driver.find_element(By.CLASS_NAME, 'with-jusan-card-navigation_navigation_section_with_card__VADNp').
                 find_element(By.TAG_NAME, 'ul').
                 find_elements(By.TAG_NAME, 'li'))
    text_link[i].click()
    print(text_link[i].text)
    if i == 0:
        time.sleep(2)
        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(2)
    else:
        # Scrolling page to top
        time.sleep(2)
        scroll_to_top = driver.find_element(By.CLASS_NAME, 'scroll-to-top_scrollToTopButton___Zu7y')
        scroll_to_top.click()
        time.sleep(2)

# Create order
orders = driver.find_elements(By.CLASS_NAME, 'btn-order')
orders[0].click()
print(f'Clicked button {orders[0].text}')
# Scrolling page to top
time.sleep(2)
scroll_to_top = driver.find_element(By.CLASS_NAME, 'scroll-to-top_scrollToTopButton___Zu7y')
scroll_to_top.click()
time.sleep(2)

orders[1].click()
print(f'Clicked button {orders[1].text}')
time.sleep(2)

driver.quit()
