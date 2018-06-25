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
from generate_screenshot import Screenshot

__author__ = "uppusaikiran"
__copyright__ = "uppusaikiran"
__license__ = "none"

_logger = logging.getLogger(__name__)

class GenerateImages(object):
    def __init__(self):
        pass

    def generate_images(self,folderpath):
	self.folderpath = folderpath
	import os
	
	with open(self.folderpath , 'r') as f:
	    for x in f:
		url = x.rstrip()
		s = Screenshot()
    		s.generate_screenshot_headless(str(url),'{}.png'.format(str(url)))


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`airgparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="Generate Screenshots for entire Folder")
    parser.add_argument(
    '-w',
    '--folderpath',
        help="Enter Folder path.",
        )
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    s = GenerateImages()
    s.generate_images(str(args.folderpath))

def run():
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO,filename='web-image.log',
            format='%(asctime)s %(message)s')
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

