from constants import ALLOWED_DELIMITERS
from utils import validate_delimiter, create_nrc_regex


# A function to check if the nrc is valid.
def validate_nrc(nrc_number: str, delimiter: str = None) -> bool:
    is_valid = validate_delimiter(delimiter)
    if not is_valid:
        raise Exception(f'NRC delimiter is invalid! values should be seperated by {ALLOWED_DELIMITERS}')
    nrc_pattern = create_nrc_regex(delimiter)
    print(delimiter)


validate_nrc('sdadfa', delimiter='-')
