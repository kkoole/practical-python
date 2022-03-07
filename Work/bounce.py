# bounce.py
#
# Exercise 1.5

height = 100 # 100 meters
bounces = 10 # amount of bounces
bounce = 0 # current bounce

while bounce < bounces:
    height = height * 0.6
    print(round(height, 4))
    bounce = bounce + 1
