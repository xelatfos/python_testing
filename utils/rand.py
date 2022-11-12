import random
import string

def rnd_str(pre, max_len):
    sym = string.ascii_letters + string.digits  + " "*10 # + string.punctuation - known issue here
    return pre + "".join([random.choice(sym) for i in range(5+random.randrange(5+max_len))])
