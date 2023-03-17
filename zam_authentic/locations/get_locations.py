from .constants import DISTRICTS, PROVINCES, CONSTITUENCIES, TOWNS, WARDS
from .wards import WARDS


# function to return available provinces
def get_provinces() -> list:

    return PROVINCES.copy()


# function to get districts belonging to a province
def get_districts(province: str) -> list:
    return DISTRICTS.get(province)


# function to get provinces belonging to a district
def get_constituencies(district: str) -> list:
    return CONSTITUENCIES.get(district)


# function that gets all districts available limited with a given limit. Default = 10
def get_all_districts(limit: int = 10) -> list:
    all_districts: list = []
    for district in DISTRICTS.values():
        all_districts += district
    if limit > len(all_districts):
        return all_districts
    return all_districts[:limit]


# function that gets all constituencies available with a given limit. Default = 10
def get_all_constituencies(limit: int = 10) -> list:
    all_constituencies: list = []
    for constituency in CONSTITUENCIES.values():
        all_constituencies += constituency
    if limit > len(all_constituencies):
        return all_constituencies
    return all_constituencies[:limit]


# function to retrieve all towns based on district.
def get_towns(district: str) -> list:
    return TOWNS.get(district)


# function to retrieve all wards based on district.
def get_wards(district: str) -> list:
    return WARDS.get(district)

