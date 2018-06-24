#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
        hello_world = web_image_classifier.module:function

Then run `python setup.py install` which will install the command `hello_world`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
import sys
import time
import os
import urlparse
import subprocess
import signal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

__author__ = "uppusaikiran"
__copyright__ = "uppusaikiran"
__license__ = "none"

_logger = logging.getLogger(__name__)

#class Screenshot(QWebView):
class Screenshot(object):
    def g__init__(self):
	self.app = QApplication(sys.argv)
	QWebView.__init__(self)
	self._loaded = False
	self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
	_logger.info('Received url {}'.format(url))
	_start = time.time()
	try:
	    #Check for http/https
            if url[0:4] == 'http' or url[0:5] == 'https':
		self.url = url
		output_file = output_file[8:].replace('/','-')
	    else:
		url = 'http://' + url
            self.load(QUrl(url))
            self.wait_load(url)
            # set to webpage size
            frame = self.page().mainFrame()
            self.page().setViewportSize(frame.contentsSize())
            # render image
            image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
            painter = QPainter(image)
            frame.render(painter)
            painter.end()
	    _logger.info('Saving screenshot {} for {}'.format(output_file,url))
	    image.save('data_bad/'+output_file)
	except Exception as e:
	    _logger.error('Error in capturing screenshot {} - {}'.format(url,e))
	_end = time.time()
	_logger.info('Time took for processing url {} - {}'.format(url,_end - _start))
    
    def wait_load(self,url,delay=1,retry_count=60):
        # process app events until page loaded
        while not self._loaded and retry_count:
	    _logger.info('wait_load for url {} retry_count {}'.format(url,retry_count))
            self.app.processEvents()
            time.sleep(delay)
	    retry_count -=1
	_logger.info('wait_load for url {} expired'.format(url))
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True 

    def clean_url(self,url):
	return urlparse.urlparse(url).path

    def generate_screenshot_headless(self,url,output_file):
	_logger.info('url received {}'.format(url))
	_start = time.time()
	if url[0:4] == 'http' or url[0:5] == 'https':
            self.url = url
            output_file = output_file[7:].replace('/','-')

        else:
            url = 'http://' + url
	options = Options()
	options.add_argument("--headless") # Runs Chrome in headless mode.
	options.add_argument('--no-sandbox') # # Bypass OS security model
	options.add_argument('start-maximized')
        options.add_argument('--disable-dev-shm-usage')
	options.add_argument('disable-infobars')
	options.add_argument("--disable-extensions")
	options.add_argument("window-size=1920,1080")
        try:
	    driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
	    driver.set_page_load_timeout(10)
            driver.get(url)
	    screenshot_path = 'data_good/' + output_file 
	    _logger.info('screenshot for url {} is saved at {}'.format(url,screenshot_path))
	    driver.save_screenshot(screenshot_path)
	    driver.quit()
	except Exception as e:
	    _logger.error('error while using chrome {}'.format(e))
	_end = time.time()
	_logger.info('Time took for processing url {} - {}'.format(url,_end - _start))

    def generate_screenshot(self,url,output_file):
	#import pdb;pdb.set_trace()
        _logger.info('url received {}'.format(url))
	self.br = webdriver.PhantomJS()
	self.br.set_window_size(1120, 550)
	#import pdb;pdb.set_trace()
        if url[0:4] == 'http' or url[0:5] == 'https':
            self.url = url
            output_file = output_file[7:].replace('/','-')

        else:
            url = 'http://' + url
	self.br.get(url)
	_logger.info('Saving screenshot {} for {}'.format(output_file,url))
        screenshot_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data_good',output_file)
	print('URL {} screenshot saving in {}'.format(url,screenshot_path))
	self.br.set_page_load_timeout(5)
        self.br.save_screenshot(screenshot_path)
	try:
	    self.br.service.process.send_signal(signal.SIGTERM) # kill the specific phantomjs child proc

            self.br.quit()
            self.phantom_js_clean_up()
    	except Exception as err:
            _logger.error('Error in Browser cleanup {}'.format(err))
		
    def phantom_js_clean_up(self):
    	"""Clean up Phantom JS.
	    Kills all phantomjs instances, disregard of their origin.
    	"""
        processes = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = processes.communicate()

        for line in out.splitlines():
            if 'phantomjs' in line:
            	pid = int(line.split(None, 1)[0])
            	os.kill(pid, signal.SIGKILL)


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`airgparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="Just a Website Screenshot Tool")
    parser.add_argument(
	'-w',
	'--website',
        help="Enter a website url to take screenshot",
        )
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    s = Screenshot()
    #import pdb;pdb.set_trace()
    #s.capture('{}'.format(str(args.website)),'{}.png'.format(str(args.website)))	    
    #s.generate_screenshot(str(args.website),'{}.png'.format(str(args.website)))
    s.generate_screenshot_headless(str(args.website),'{}.png'.format(str(args.website)))

def run():
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO,filename='web-image.log',
			format='%(asctime)s %(message)s')
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
