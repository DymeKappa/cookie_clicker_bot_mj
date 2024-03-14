from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CookieClickerBot:
    def __init__(self):
        # Configuration
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service_object = Service("/Applications/chromedriver-mac-x64/chromedriver") #services driver
        self.driver = webdriver.Chrome(options=self.options, service=self.service_object)
        self.action = ActionChains(self.driver)

        # Options
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()

        # Initialization
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        print(self.driver.title)
        print(self.driver.current_url)

    def closeWindows(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".fc-button-label")
        for button in buttons:
            if button.text == "Consent":
                button.click()
                break

        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Got it!')]").click()

        languages = self.driver.find_elements(By.CSS_SELECTOR, ".langSelectButton.title")
        for language in languages:
            if language.text == "Polski":
                language.click()
                break
        self.driver.find_element(By.XPATH, "//img[contains(@aria-label, 'Close')]").click()
    def loadingProgress(self):
        saved_progress = "Mi4wNTJ8fDE3MDk3MDg4MDY0ODY7MTcwOTQ5Njc5Mjc3NDsxNzA5ODA0NjMzNTI4O01jR25vbWU7cmRuYXE7MCwxLDAsMCwwLDAsMHwxMTExMTEwMTEwMDEwMTEwMDEwMTAxMTAwMDF8MjQ4MTg1NDQwODcuMzcwODg0OzE3MDAyOTI4ODgwOS44NDk3Ozc2NzQ7MjE7MTEyNDIyNzkzMzIuNDI4MjU7MzAzOzA7MDsxMTEwNTA4NzIyOTEwLjYxNDswOzA7MDswOzA7MTsxNjswOzA7MDswOzA7MDs7MDswOzE7MDsxOzA7MDstMTstMTstMTstMTstMTswOzA7MDswOzc1OzA7MDswOzM7MTcwOTc5Mjg3MDQwNjswOzA7OzQxOzA7MDsxNTk4MjY4Mi4zMDAxOTg5NDQ7NTA7MDswO3wxMDAsMTAxLDc5MjE3MjE0MjQsMCwsMCwxMDA7MTEwLDExMCwzNjg0NjI4NjkxLDAsLDAsMTEwOzc1LDc1LDg2NTcwMjYyMSwwLCwwLDc1OzUwLDUwLDI2NTI1NDgzMTYsMCwsMCw1MDs1MCw1MCw5MDEwMjAwOTI0LDAsLDAsNTA7NTAsNTAsMjMzOTczNTc0NzksMSwwOjA6MDo0MjI3LjQ0NzQ1NTMwNTQzNDoxOiA2NDU6NTotMjU3OjEwODowOjA6MDowITE2MDM6MTotMjI1OjI4MDowOjA6MDowITEwNzc4OjU6MTk6MjA4OjA6MDowOjYwMSE3OTMzOjU6ODozMTowOjA6MDozODMhMTIzNzI6MzotOToyNDM6MDowOjA6NTMyNCExNTE5OjU6Mjo0MDM6MDowOjA6ODA5ITYxMjc6MjozOToxMTA6MDowOjA6Mzk2ITgwNTc6MjotMzYxOjMxNDowOjA6MDowITMyOTg6NTo0NzoxMDM6MDoxOjA6MCE2NTk5OjI6LTY2OjU4OTowOjE6MDowITQyNTU6MzotMTg3OjI3NjowOjE6MDowITU5MzY6NTotNDM6MzQxOjA6MTowOjAhNzk0NjowOi05MDo5NTowOjE6MDowITgyMDM6NTotMjEzOjUxNDowOjE6MDowITEwMzI5OjE6LTI2OjQxMzowOjE6MDowITM1ODY6MTotNDA5OjMzNDowOjE6MDowITEyNTE3OjE6LTI2Njo1NDk6MDoxOjA6MCExMzc1MjoxOi0yMzg6MzgyOjA6MTowOjAhIDEsMCw1MDszMCwzMCw0NTc4Nzk4NzczNiwwLCwwLDMwOzE1LDE1LDM3NTk0MjcyNDA1LDEsMTkgOCA4IDEsMCwxNTs1LDUsMTk5Nzk1OTQzNzksMSwsMCw1OzEsMSw0ODgzMzAxNzUyLDAsLDAsMTswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7fDExMTExMTExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTAxMDAwMTAwMDAwMDAwMDAwMDAwMDAwMTExMTExMTExMTExMTExMTExMTExMTEwMDAxMTExMTExMTAwMDAwMDAwMTEwMDEwMTAxMDExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTEwMDAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMTAwMDAwMTExMTExMDAwMDAwMTExMDAwMDAwMDAwMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8MTExMTExMTEwMDAwMDAwMDExMTExMTEwMDAxMTEwMTExMTExMTEwMDExMTExMTExMDExMDEwMDEwMDAwMDAwMDAwMDExMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTEwMDAxMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHx8%21END%21"
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".subButton")
        for button in buttons:
            if button.text == "Opcje":
                button.click()
                break
        settings = self.driver.find_elements(By.CSS_SELECTOR, ".option.smallFancyButton")
        for setting in settings:
            if setting.text == "Importuj stan gry":
                setting.click()
                break
        self.driver.find_element(By.ID, "textareaPrompt").send_keys(saved_progress)
        self.driver.find_element(By.ID, "promptOption0").click()
        self.driver.find_element(By.CSS_SELECTOR, ".close.menuClose").click()

    def bigCookieClick(self):
        cookie = self.driver.find_element(By.XPATH, "//button[@id='bigCookie']")
        cookie.click()

    def closeAchievements(self):
        achievement_close_button = self.driver.find_element(By.CSS_SELECTOR, ".close")
        if achievement_close_button.is_displayed():
            achievement_close_button.click()

    def autoBuyer(self):
        # This method isn't working yet
        # Items to buy
        items = self.driver.find_elements(By.CSS_SELECTOR, ".title.productName")
        # We would like to buy upgrades from the most expensive items at first
        items_reversed = items[::-1]
        items_prices = self.driver.find_elements(By.CSS_SELECTOR, ".price")
        items_prices_reversed = items_prices[::-1]

        for price in items_prices_reversed:
            pass

        # Cookies counter
        counter = self.driver.find_element(By.XPATH, "//div[@id='cookies']")
        counter_elements = counter.text.split()


    def gamePlay(self):
        switch_on = True

        while switch_on:
            # Cookie clicking
            cookie = self.driver.find_element(By.XPATH, "//button[@id='bigCookie']")
            cookie.click()

            # Closing achievements
            achievement_close_button = self.driver.find_element(By.CSS_SELECTOR, ".close")
            if achievement_close_button.is_displayed():
                achievement_close_button.click()

            # Otherwise we can implement this try: section down below
            """try:
                achievement_close_button = self.driver.find_element(By.CSS_SELECTOR, ".close")
                # Checking if achievements are displayed
                if achievement_close_button.is_displayed():
                    achievement_close_button.click()

            except NoSuchElementException:
                pass
                continue"""

runner = CookieClickerBot()
runner.closeWindows()
runner.loadingProgress()
runner.autoBuyer()
runner.gamePlay()

#driver.close()
