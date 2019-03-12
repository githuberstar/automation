from selenium.webdriver import Remote
from threading import Thread
from selenium import webdriver


lists = {'http://192.168.19.102:5555/wd/hub': 'chrome', 'http://192.168.19.102:5556/wd/hub': 'chrome'}


def browser_driver(host, browser_name):
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser_name,
                                          'version': '',
                                          'javascriptEnabled': True
                                        }
                    )
    return driver


def thread_test():
    threads = []
    files = range(len(lists))
    for host, browser_name in lists.items():
        t = Thread(target=browser_driver, args=[host, browser_name])
        threads.append(t)
    for i in threads:
        i.start()
        print(1)

