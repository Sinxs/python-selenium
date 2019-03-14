from selenium import webdriver
import time

def login(driver, user, password):
    '''登录github'''
    # 打开github首页
    driver.get("https://github.com/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_id("login_field").send_keys(user)
    # 输入密码
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()

def logout(driver):
    '''退出github'''
    time.sleep(3)
    # 点右上角设置
    driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    time.sleep(1)
    # 点sign out
    driver.find_element_by_css_selector(".dropdown-item.dropdown-signout").click()
    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()  # chromedriver路径
    # 调用登录
    login(driver, "Sinxs", "sin254981")
    print("hello  Sinxs!")
    # 调用退出
    logout(driver)