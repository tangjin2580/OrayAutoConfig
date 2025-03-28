import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def r300_configure_router(wifi_password, admin_password):
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    try:
        # 访问指定的URL
        driver.get("http://10.168.1.1/")
        print("这是初始化配置")
        time.sleep(5)  # 等待页面加载

        # 检查是否存在“忘记密码”链接
        try:
            forget_password_link = driver.find_element(By.XPATH, '//div[@class="forget"]/a[@class="a_link"]')
            print("已配置，直接关闭浏览器")
            driver.quit()
            return
        except:
            print("新设备，初始化配置")

        # 点击下拉菜单输入框以展开下拉选项
        try:
            dropdown_input = driver.find_element(By.XPATH,
                                                 '//input[@class="form_input click_dropdown_input ieleft"]')
            dropdown_input.click()
            print("下拉菜单已展开")
        except Exception as e:
            print(f"未找到下拉菜单输入框或点击失败: {e}")
            driver.quit()
            return
        # 找到并点击“动态IP”按钮以设置为自动获取IP
        try:
            dhcp_button = driver.find_element(By.XPATH,
                                              '//div[@class="click_dropdown_item" and @onclick="changeMod(\'dhcp\')"]')
            dhcp_button.click()
            print("动态IP按钮已成功点击")
        except Exception as e:
            print(f"未找到动态IP按钮或点击失败: {e}")

        time.sleep(2)  # 等待下拉菜单更新

        # 点击立即上网按钮
        try:
            confirm_button = driver.find_element(By.XPATH, '//button[@class="btn" and @onclick="checkMod()"]')
            confirm_button.click()
            print("立即上网按钮已成功点击")
        except Exception as e:
            print(f"未找到立即上网按钮或点击失败: {e}")

            # 等待页面加载
        time.sleep(5)  # 根据情况调整

        # 找到WiFi密码输入框并设置密码
        try:
            wifi_password_input = driver.find_element(By.XPATH, '//input[@id="wifi-pwd"]')
            wifi_password_input.send_keys(wifi_password)  # 输入WiFi密码
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

        time.sleep(5)
        # 尝试找到“跳过，晚点再绑定”按钮并点击
        try:
            skip_button = driver.find_element(By.XPATH, '//a[text()="跳过，晚点再绑定"]')
            skip_button.click()
            print("已成功点击跳过按钮")
        except Exception as e:
            print(f"未找到跳过按钮或点击失败: {e}")

        time.sleep(5)  # 等待配置完成

        # 管理密码
        try:
            admin_pwd_input = driver.find_element(By.XPATH, '//input[@id="admin-pwd"]')
            admin_pwd_input.send_keys(admin_password)
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

    finally:
        driver.quit()  # 关闭浏览器
