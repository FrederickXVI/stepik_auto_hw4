import time


class TestLanguage():
    def test_guest_should_see_add_button(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        print("Language = " + language)
        # здесь тайм слип для того, чтобы удостовериться в правильности выбранного языка
        #time.sleep(10)
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
        assert button is not None