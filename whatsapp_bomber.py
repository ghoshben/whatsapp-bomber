from selenium import webdriver
import string
import random
import time


def bomber(ress):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group(Try to make group name simple as I wrote it in 5 min and for fun) : ')
    count = int(input('Enter the count: '))

    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count):
        msg_box.send_keys(ress)
        print(i)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        # so that wp dont block u :P
        time.sleep(1)
    print('Bombing Complete!!')


if __name__ == '__main__':
    N = 7

    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))

    banner = '''
                     ____  _   _ _   _ ____  _   _    _    __  __ 
                    / ___|| | | | | | | __ )| | | |  / \  |  \/  |
                    \___ \| |_| | | | |  _ \| |_| | / _ \ | |\/| |
                     ___) |  _  | |_| | |_) |  _  |/ ___ \| |  | |
                    |____/|_| |_|\___/|____/|_| |_/_/   \_\_|  |_|

    '''
    print(banner)
    bomber(res)
