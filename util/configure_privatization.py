# util/configure_privatization.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_driver(url):
    """初始化Chrome浏览器并访问指定URL"""
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def input_password(driver, password):
    """输入密码并登录"""
    try:
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        print("密码已输入到指定输入框")

        login_button = driver.find_element(By.ID, 'login-btn')
        login_button.click()
        print("登录成功")
    except Exception as e:
        print(f"未找到密码输入框或登录失败: {e}")


def click_more(driver):
    """点击'更多'按钮"""
    try:
        more_button = driver.find_element(By.XPATH, "//span[text()='更多']")
        more_button.click()
        print("已点击'更多'按钮")
    except Exception as e:
        print(f"未找到'更多'按钮或点击失败: {e}")


def click_privatization_setting(driver):
    """点击私有化设置链接"""
    try:
        privatization_setting = driver.find_element(By.CSS_SELECTOR, 'div.private-icon a[data-dialog="open"]')
        privatization_setting.click()
        print("私有化设置已点击")
    except Exception as e:
        print(f"未找到私有化设置按钮或点击失败: {e}")


def set_privatization_address(driver, address):
    """输入服务器地址并保存"""
    try:
        privatization_address_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'privatization_address'))
        )
        privatization_address_input.clear()  # 清空输入框内容，防止之前的地址残留
        privatization_address_input.send_keys(address)
        print("服务器地址已输入到指定输入框")

        save_button = driver.find_element(By.XPATH,
                                          '//a[@onclick="submitPrivatization()" and @class="fl small_btn primary"]')
        save_button.click()
        print("保存按钮已点击")
    except Exception as e:
        print(f"未找到服务器地址输入框或保存失败: {e}")


def configure_privatization(password, address):
    """执行私有化配置"""
    url = "http://10.168.1.1/"
    driver = init_driver(url)

    time.sleep(3)  # 等待页面加载
    input_password(driver, password)
    time.sleep(1)  # 等待登录完成

    click_more(driver)
    click_privatization_setting(driver)
    set_privatization_address(driver, address)

    time.sleep(5)  # 等待操作完成
    driver.quit()  # 关闭浏览器
