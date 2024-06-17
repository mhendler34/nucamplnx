#!/usr/bin/python3
price_is_right = 15

if price_is_right < 5:
    print("Price is too low!")
elif price_is_right >= 5 and price_is_right <= 9:
    print("Price is almost there!")
elif price_is_right == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")
