from constants import NRC_PATTERN


def create_regex(delimiter):
    return NRC_PATTERN.replace('p', 'delimiter')
