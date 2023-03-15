from constants import NRC_PATTERN

### function to modify regex pattern based on delimiter passed .
def create_regex(delimiter:str)->str:
    return NRC_PATTERN.replace('p', 'delimiter')
def validate_delimiter(delimiter:str)->str:
    return