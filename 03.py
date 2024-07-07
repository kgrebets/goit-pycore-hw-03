import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d]', '', phone_number)
    phone_number = (phone_number
                    .removeprefix("38")
                    .removeprefix("8"))
    phone_number = "+38" + phone_number
    return phone_number

numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "8(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print("Normalized phones:")
for number in numbers:
    print(normalize_phone(number) + ' <- ' + number)
