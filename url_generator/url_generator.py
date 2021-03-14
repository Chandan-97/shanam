import random
import time
from hashlib import sha256


def get_random(salt=None):
    return str(time.time())
