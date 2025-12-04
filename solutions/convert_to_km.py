'''
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.
'''

MILE_TO_KM_RATIO = 1.60934


def convert_to_km(miles):
    km = miles * MILE_TO_KM_RATIO
    return round(km, 2)


def main():
    print(convert_to_km(1))
    print(convert_to_km(21))
    print(convert_to_km(3.5))
    print(convert_to_km(0))
    print(convert_to_km(0.621371))


if __name__ == "__main__":
    main()
