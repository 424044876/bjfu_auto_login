from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
baseUrl = "http://202.204.122.1"


# 无需启动浏览器模式
def openChromBack():
    return webdriver.Remote(command_executor="0.0.0.0:9515/wd/hub",
                            desired_capabilities=DesiredCapabilities.HTMLUNIT)

# 授权操作
def operationAuth(driver):
    driver.get(baseUrl)
    elem = driver.find_element_by_id("username")
    elem.send_keys(171002312)
    elem = driver.find_element_by_id("password")
    elem.send_keys("fangzidong")
    # 提交表单
    driver.find_element_by_class_name("connect").click()

    print("success")


if __name__ == '__main__':
    # 获取浏览器驱动
    driver = openChromBack()
    operationAuth(driver)
