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
from PIL import Image
from pytesseract import image_to_string

__author__ = "uppusaikiran"
__copyright__ = "uppusaikiran"
__license__ = "none"

_logger = logging.getLogger(__name__)

class ImageToText(object):
    def __init__(self):
        pass

    def extract_text(self,imagepath):
        self.imagepath = imagepath
        raw_text = image_to_string(Image.open(self.imagepath), lang='eng')
	#raw_text = ",".join(raw_text.split("\n"))
	raw_text = [x for x in raw_text.split("\n") if x]
	_logger.info('Text extracted from Image {} - {}'.format(imagepath,raw_text))
	print(raw_text)
	return raw_text



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
    '--imagepath',
        help="Enter Image path to look for text",
        )
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    s = ImageToText()
    #import pdb;pdb.set_trace()
    #s.capture('{}'.format(str(args.website)),'{}.png'.format(str(args.website)))
    print('Image Received {}'.format(str(args.imagepath)))

    s.extract_text(str(args.imagepath))

def run():
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO,filename='web-image.log',
            format='%(asctime)s %(message)s')
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

