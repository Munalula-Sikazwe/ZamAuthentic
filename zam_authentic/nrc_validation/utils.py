from re import match

from constants import NRC_PATTERN, ALLOWED_DELIMITERS


# function to modify regex pattern based on delimiter passed .
def create_nrc_regex(delimiter: str) -> str:
    return NRC_PATTERN.replace('p', delimiter)


# checks if the delimiter is one of the expected delimiters.

def validate_delimiter(delimiter: str) -> bool:
    return delimiter in ALLOWED_DELIMITERS


# function checks if  nrc is valid with the given delimiter.
def is_valid_nrc(nrc_number: str, nrc_pattern: str):
    return bool(match(nrc_pattern, nrc_number))
