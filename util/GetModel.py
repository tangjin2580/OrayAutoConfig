import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.R300 import r300_configure_router
from util.AutoConf import configure_router
8

def GetModel(driver):
    try:
        footer = driver.find_element(By.ID, 'footer')
        footer_text = footer.text
        # 提取型号信息
        model = footer_text.split('|')[0].strip().replace('型号：', '')
        print(f"获取型号信息成功: {model}")
        return model
    except Exception as e:
        print(f"获取页脚信息失败: {e}")
        return None


def GetModelAndConfigureRouter(wifi_password, admin_password):
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    try:
        # 访问指定的URL
        driver.get("http://10.168.1.1/")
        print("这是初始化配置")
        time.sleep(5)  # 等待页面加载

        # 获取型号信息
        model = GetModel(driver)
        if model is None:
            print("无法获取型号信息，退出")
            driver.quit()
            return

        print(f"当前型号: {model}")

        # 根据型号执行不同的配置逻辑
        if model == "R300A-4151G":
            print("检测到型号 R300A-4151G，执行R300A系列配置...")
            # 执行Apn设置
            try:
                r300_configure_router( wifi_password, admin_password)
                print("成功执行R300A系列配置")
            except Exception as e:
                print(f"未找到输入框或点击失败: {e}")
                driver.quit()
                return

        elif model == "X5-7256":
            print("检测到型号 X5-7256，执行x5系列配置...")
            configure_router(wifi_password, admin_password)
        else:
            print(f"未知型号: {model}，跳过配置")
            driver.quit()
            return
    finally:
        driver.quit()

if __name__ == '__main__':
            GetModelAndConfigureRouter("88888888", "88888888")