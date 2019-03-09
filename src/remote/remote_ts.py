from selenium.webdriver import Remote

lists = {'http://192.168.19.102:5555/wd/hub': 'chrome'}
lists2 = {'http://127.0.0.1:4444/wd/hub': 'chrome'}

for host, browser in lists2.items():
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
