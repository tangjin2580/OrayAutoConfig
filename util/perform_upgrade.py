import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_upgrade():
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    # 访问指定的URL
    driver.get("http://10.168.1.1/")
    print("这是升级页面")
    # 输入密码到指定的输入框
    try:
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys("88888888")
        print("密码已输入到指定输入框")
    except Exception as e:
        print(f"未找到密码输入框或输入失败: {e}")
        driver.quit()
        return

    # 登录
    try:
        login_button = driver.find_element(By.ID, 'login-btn')
        login_button.click()
        print("登录成功")
    except Exception as e:
        print(f"未找到登录按钮或点击失败: {e}")
        driver.quit()
        return

    time.sleep(5)

    def get_current_version(driver):
        # 使用JavaScript获取文本
        version_info = driver.execute_script(
            "return document.getElementById('version-info').textContent.trim().split(' ')[0];")
        return version_info

    print("正在获取当前版本信息...")
    # 获取当前版本信息
    current_version = get_current_version(driver)
    print(f"当前版本: {current_version}")

    # 比较版本号
    if current_version >= "6.5.0":
        print("版本号大于等于6.5.0，跳过升级")
        driver.quit()
        return
    # 如果版本号小于6.5.0，则继续执行升级逻辑

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
        driver.quit()
        return

    try:
        # 找到升级按钮
        upgrade_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.fl.small_btn.primary"))
        )

        # 使用JavaScript直接调用onclick函数
        driver.execute_script("submitUpgrade('#upgrade-form');")
        print("使用JavaScript调用submitUpgrade函数成功")
    except Exception as e:
        print(f"未找到立即更新按钮或调用submitUpgrade函数失败: {e}")
        driver.quit()
        return

    # 等待升级完成
    time.sleep(120)  # 根据升级所需的时间调整等待时间

    # 关闭浏览器
    driver.quit()
    print("浏览器已关闭")


# 调用函数
#perform_upgrade()
