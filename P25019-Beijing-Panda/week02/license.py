import string
import random


def generate_license(n, length=6):
    licenses = list()
    while n:
        digits_length = random.randint(1, length // 2)
        license_1 = random.sample(string.digits, digits_length)

        license_2 = random.sample(string.ascii_letters, length - digits_length)

        license_final = license_1 + license_2

        random.shuffle(license_final)

        license_final = ''.join(license_final)

        if license_final in licenses:
            continue

        licenses.append(license_final)

        n -= 1

    return licenses


print(generate_license(200))
