import time
from telnetlib import EC

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 初始化Chrome浏览器
driver = webdriver.Chrome()


def is_webpage_accessible(url, retries=3, delay=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print("网页可访问")
                return True
            else:
                print(f"网页状态码: {response.status_code}")
        except requests.RequestException as e:
            print(f"请求网页时出错: {e}")

        # 如果不是最后一次尝试，等待一段时间后重试
        if attempt < retries - 1:
            print(f"等待{delay}秒后重试...")
            time.sleep(delay)
        else:
            print("网页不可访问，已达到最大重试次数")
            return False


url = "http://10.168.1.1/"
if is_webpage_accessible(url):
    # 刷新网页
    driver.refresh()
else:
    print("由于网页不可访问，无法刷新网页")

time.sleep(10)  # 等待页面刷新

# 输入密码到指定的输入框
try:
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("88888888")
    print("密码已输入到指定输入框")
except Exception as e:
    print(f"未找到密码输入框或输入失败: {e}")

# 登录
try:
    login_button = driver.find_element(By.ID, 'login-btn')
    login_button.click()
    print("登录成功")
except Exception as e:
    print(f"未找到登录按钮或点击失败: {e}")

time.sleep(5)

try:
    # 等待元素加载并可点击
    check_upgrade_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'check-upgrade'))
    )

    # 滚动到元素位置
    driver.execute_script("arguments[0].scrollIntoView();", check_upgrade_link)

    try:
        # 尝试常规点击
        check_upgrade_link.click()
        print("成功点击检查升级链接")
    except Exception:
        # 如果常规点击失败，尝试使用JavaScript点击
        driver.execute_script("document.getElementById('check-upgrade').click();")
        print("使用JavaScript成功点击检查升级链接")
except Exception as e:
    print(f"未找到检查升级链接或点击失败: {e}")

# 如果你使用的是onclick属性的元素，可以尝试直接调用该函数
try:
    # 等待元素加载
    upgrade_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".fl.small_btn.primary"))
    )

    # 使用JavaScript直接调用onclick函数
    driver.execute_script("submitUpgrade('#upgrade-form');")
    print("使用JavaScript调用submitUpgrade函数成功")
except Exception as e:
    print(f"未找到立即更新按钮或调用submitUpgrade函数失败: {e}")
