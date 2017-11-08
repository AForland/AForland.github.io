import csv
import numpy as np
import random, string

def random_id():
   letters = string.ascii_uppercase
   return ''.join(random.choice(letters) for i in range(3))

def random_ip():
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(3)) + '.' + ''.join(random.choice(numbers) for i in range(1)) + '.' + ''.join(random.choice(numbers) for i in range(1)) + '.' +''.join(random.choice(numbers) for i in range(3))

def random_start_time():
    min10 = ['0','1','2','3','4','5']
    min1 = ['1','2','3','4','5','6','7','8','9','0']
    return '1:' + ''.join(random.choice(min10) for i in range(1)) + ''.join(random.choice(min1) for i in range(1))

def random_end_time():
    min10 = ['0','1','2','3','4','5']
    min1 = ['1','2','3','4','5','6','7','8','9','0']
    return '2:' + ''.join(random.choice(min10) for i in range(1)) + ''.join(random.choice(min10) for i in range(1))

def random_ave_bwith():
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(2)) + "Mbps"

def random_Phone():
    phones = ['Nexus 6','Pixel','Galaxy S8','iPhone 6','iPhone 7','LG 10']
    return ''.join(random.choice(phones) for i in range(1))

# Ip's from net. Use at own risk.
def Sites_ip():
    sites = ['216.58.194.78', '157.240.17.35', '151.101.65.140', '52.54.140.49', '13.32.240.208']
    return ''.join(random.choice(sites) for i in range(1))

def Path():
    walk = ['1','2','3']
    return ''.join(random.choice(walk) for i in range(4))

i = 0
while i in range(0,50000):
    DATA = open('/home/adam/Documents/Python/10to6Data.csv','a')
    myCsvRow = random_id() + ',' + random_ip() +',' + random_start_time() +',' + random_end_time() + ',' + random_ave_bwith() + ',' + random_Phone() + ',' + Sites_ip() + ',' + Path()
    DATA.write(myCsvRow)
    DATA.write('\n')
    DATA.close()
    i = i + 1
