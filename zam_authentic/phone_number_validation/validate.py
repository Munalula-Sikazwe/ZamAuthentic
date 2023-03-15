from phonenumbers import parse, NumberParseException


def phonenumber_is_valid(phonenumber: str) -> bool:
    try:
        phonenumber = parse(phonenumber, 'ZM')
    except NumberParseException:
        return False
    if not phonenumber:
        return False


print(phonenumber_is_valid("0(((9"))
