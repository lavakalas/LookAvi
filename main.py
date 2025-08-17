import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.avito.ru/brands/c99bb54f2fc5327c77925ead8f852834")

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

page_source = driver.page_source

with open("page_source.html", "w") as f:
    f.write(page_source)

print("саккесс")
driver.quit()
