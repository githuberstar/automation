from selenium.webdriver import Remote
from selenium import webdriver


def browser():
    # driver = webdriver.Chrome()
    host = '127.0.0.1:4444'
    dc = {'browserName': 'chrome'}
    driver_name = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    return driver_name


if __name__ == '__main__':
    driver = browser()
    driver.get('http://aonxin.com:8889')
    driver.quit()
