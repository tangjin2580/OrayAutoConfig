import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_model_from_footer(driver):
    """
    从页脚获取型号信息
    """
    try:
        footer = driver.find_element(By.ID, 'footer')
        footer_text = footer.text
        # 提取型号信息
        model = footer_text.split('|')[0].strip().replace('型号：', '')
        return model
    except Exception as e:
        print(f"获取页脚信息失败: {e}")
        return None


def configure_router(wifi_password, admin_password):
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    try:
        # 访问指定的URL
        driver.get("http://10.168.1.1/")
        print("这是初始化配置")
        time.sleep(5)  # 等待页面加载

        # 获取型号信息
        model = get_model_from_footer(driver)
        if model is None:
            print("无法获取型号信息，退出")
            driver.quit()
            return

        print(f"当前型号: {model}")

        # 根据型号执行不同的配置逻辑
        if model == "R300A-4151G":
            print("检测到型号 R300A-4151G，执行R300A系列配置...")
            try:
                input_box = driver.find_element(By.CSS_SELECTOR, "input.form_input.click_dropdown_input.ieleft")
                input_box.click()
                print("成功点击输入框，展开下拉菜单")
            except Exception as e:
                print(f"未找到输入框或点击失败: {e}")
                driver.quit()
                return

            # 选择“动态IP”选项
            try:
                dhcp_option = driver.find_element(By.XPATH,
                                                  "//div[@class='click_dropdown_item' and contains(@onclick, 'changeMod(\'dhcp\')')]")
                dhcp_option.click()
                print("成功选择动态IP选项")
            except Exception as e:
                print(f"未找到动态IP选项或点击失败: {e}")
                driver.quit()
                return
        elif model == "X5-7256":
            print("检测到型号 X5-7256，执行x5系列配置...")
            # 这里可以添加针对 X5-7256 的配置逻辑
        else:
            print(f"未知型号: {model}，跳过配置")
            driver.quit()
            return

        # 检查是否存在“忘记密码”链接
        try:
            forget_password_link = driver.find_element(By.XPATH, '//div[@class="forget"]/a[@class="a_link"]')
            print("已配置，直接关闭浏览器")
            driver.quit()
            return
        except:
            print("新设备，初始化配置")

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


# 调用函数
wifi_password = "88888888"  # 输入你的WiFi密码
admin_password = "88888888"  # 输入你的管理密码
configure_router(wifi_password, admin_password)
