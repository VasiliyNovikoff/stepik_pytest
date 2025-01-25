from selenium.webdriver.common.by import By


class TestItems:
    def test_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert len(buttons) > 0, "Button is not displayed"
