import time

from util.AutoConf import configure_router
from util.perform_upgrade import perform_upgrade
from util.configure_privatization import configure_privatization

# 定义常量
WIFI_PASSWORD = "88888888"  # 输入你的WiFi密码
ADMIN_PASSWORD = "88888888"  # 输入你的管理密码
PRIVATIZATION_URL = "https://www.cxsdwan.com:3443"


# 主函数
def main():
    # 配置路由器
    print("开始配置路由器...")
    configure_router(WIFI_PASSWORD, ADMIN_PASSWORD)
    print("路由器配置完成，等待10秒...")
    time.sleep(5)

    # 升级固件
    print("开始升级固件...")
    perform_upgrade()
    print("固件升级完成")

    # 配置私有化
    print("开始配置私有化...")
    configure_privatization(ADMIN_PASSWORD, PRIVATIZATION_URL)
    print("私有化配置完成")


# 执行主函数
if __name__ == "__main__":
    main()
