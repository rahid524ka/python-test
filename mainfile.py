import random

feat_miles = 5280
meter_kilo = 1000
beatles = ["rahid","hamza","sirtaj","waqar"]

def get_file(filename):
    return filename[filename.index(".") + 1 :]
def roll_dice(num):
    return random.randint(1, num)