from payment import paymnet_details
import os
import sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), 'pwskills/payment')))


def course():
    print("this is my course file")


paymnet_details.payment()
