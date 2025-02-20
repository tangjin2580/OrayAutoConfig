import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化Chrome浏览器
driver = webdriver.Chrome()

# 访问指定的URL
driver.get("http://10.168.1.1/")

# 等待页面加载，确保按钮可以被找到
time.sleep(5)

# 找到并点击第一个按钮
try:
    button = driver.find_element(By.XPATH, '//button[@class="btn" and @onclick="checkMod()"]')
    button.click()
    print("按钮已成功点击")
except Exception as e:
    print(f"未找到按钮或点击失败: {e}")

# 等待配置页面加载
time.sleep(5)  # 根据情况调整

# 找到WiFi密码输入框并设置密码
try:
    wifi_password_input = driver.find_element(By.XPATH, '//input[@id="wifi-pwd"]')
    wifi_password_input.send_keys("88888888")  # 输入WiFi密码
    print("WiFi密码已设置")
except Exception as e:
    print(f"未找到WiFi密码输入框或设置失败: {e}")

# 找到“下一步”按钮并点击
try:
    next_button = driver.find_element(By.XPATH, '//button[@class="btn" and @onclick="submit()"]')
    next_button.click()
    print("已成功点击下一步按钮")
except Exception as e:
    print(f"未找到下一步按钮或点击失败: {e}")

time.sleep(5)  # 等待配置完成

#管理密码
try:
    admin_pwd_input = driver.find_element(By.XPATH, '//input[@id="admin-pwd"]')
    admin_pwd_input.send_keys("88888888")
    print("管理密码已成功设置")
except Exception as e:
    print(f"未找到管理密码输入框或设置失败: {e}")
    # 点击配置完成按钮
try:
    submit_button = driver.find_element(By.XPATH, '//button[@class="btn" and @onclick="submit()"]')
    submit_button.click()
    print("配置完成按钮已成功点击")
except Exception as e:
    print(f"未找到配置完成按钮或点击失败: {e}")


time.sleep(10)  # 等待配置完成


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

# 等待配置完成，然后关闭浏览器
#time.sleep(10)  # 根据配置完成所需的时间调整等待时间
#driver.quit()
