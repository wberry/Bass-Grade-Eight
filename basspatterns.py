import random
import gradefuncs

# Grade eight bass patterns

def get_rnb_example():
    return gradefuncs.get_rnb_sequence(0,6,3,4)

def get_rnb_random():
    return gradefuncs.get_rnb_sequence(random.randint(0,6),random.randint(0,6),
                                       random.randint(0,6),random.randint(0,6))

def get_ballad_example():
    return gradefuncs.get_ballad_sequence(0,0,1,5,2,3)

def get_ballad_random():
    return gradefuncs.get_ballad_sequence(random.randint(0,5),random.randint(0,5),random.randint(0,5),
                                          random.randint(0,5),random.randint(0,5),random.randint(0,5))

