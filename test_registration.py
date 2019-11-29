
class TestRegistration():


  def test_registration(self, browser, get_login, get_password):
    browser.get("http://selenium1py.pythonanywhere.com/")
    browser.maximize_window()
    browser.find_element_by_id("login_link").click()
    print("\nsend registration data..")
    browser.find_element_by_name("registration-email").send_keys(get_login)
    browser.find_element_by_name("registration-password1").send_keys(get_password)
    browser.find_element_by_name("registration-password2").send_keys(get_password)
    browser.find_element_by_name("registration_submit").click()
    # проверяем наличие сообщения об успехе
    success_msg = browser.find_element_by_css_selector(".alert-success")
    assert success_msg is not None
    print("\n.. success")

    # удаляем только что созданный аккаунт
    print("\nstart delete new account..")
    # какой-то длинный селектор для кнопки "Аккаунт" получился
    browser.find_element_by_css_selector("ul.nav.navbar-nav.navbar-right li:first-child").click()
    browser.find_element_by_id("delete_profile").click()
    browser.find_element_by_id("id_password").send_keys(get_password)
    browser.find_element_by_css_selector(".btn-danger").click()
