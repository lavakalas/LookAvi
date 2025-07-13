import undetected_chromedriver as uc

if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get("https://www.avito.ru")
    driver.save_screenshot('screenshot.png')
