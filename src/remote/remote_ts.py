from selenium.webdriver import Remote
from selenium.webdriver import R

lists = {'http://127.0.0.1:4445/wd/hub': 'chrome',
         'http://192.168.1.243/wd/hub': 'chrome'}

for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True
                                        }
                    )

    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()
    driver.close()
