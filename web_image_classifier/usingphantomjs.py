from selenium import webdriver
import time
import sys

print 'Without Headless'
_start = time.time()
br = webdriver.PhantomJS()
br.get('http://' + sys.argv[1])
br.save_screenshot('screenshot-phantom.png')
br.quit
_end = time.time()
print 'Total time for non-headless {}'.format(_end - _start)

"""
print 'Headless'
_start = time.time()
options = webdriver.ChromeOptions()
#options.binary_location = '/usr/bin/chromedriver'
options.add_argument('--headless')
#options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver' ,chrome_options=options)
driver.get('http://www.stackoverflow.com')
driver.save_screenshot('screenshot-headless.png')
driver.quit()
_end = time.time()
print 'Total time for headless {}'.format(_end - _start)
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print 'Headless'
_start = time.time()
options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
driver.get('http://' + sys.argv[1])
driver.save_screenshot('screenshot-headless.png')
driver.quit()
_end = time.time()
print 'Total time for headless {}'.format(_end - _start)
