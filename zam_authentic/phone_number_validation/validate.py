from phonenumbers import parse, NumberParseException, is_valid_number, carrier

from constants import CARRIERS


def phonenumber_is_valid(phonenumber: str) -> bool:
    try:
        phonenumber = parse(phonenumber, 'ZM')
    except NumberParseException:
        return False
    return is_valid_number(phonenumber)


# function returning the carrier that the phonenumber belongs to .
def get_carrier(phone_number: str) -> str:
    is_valid = phonenumber_is_valid(phone_number)
    phone_number = parse(phone_number, 'ZM')
    if not is_valid:
        raise Exception('Cannot return the carrier of an invalid number')
    return carrier.name_for_number(phone_number, 'en')


def get_available_carriers():
    return list(CARRIERS.keys())


print(get_available_carriers())
