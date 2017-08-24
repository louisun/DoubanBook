import random
import string

BIDS_LEN = 1000
def gen_bids():
    bids = []
    for i in range(BIDS_LEN):
        bids.append(''.join(random.sample(string.ascii_letters+string.digits,11)))
    return bids
