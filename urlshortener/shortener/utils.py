import random
import string

def randomize_strings():

    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )