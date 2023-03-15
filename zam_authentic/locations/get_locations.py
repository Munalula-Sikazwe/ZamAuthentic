from constants import DISTRICTS, PROVINCES, CONSTITUENCIES


# function to return available provinces
def get_provices() -> list:
    return PROVINCES.copy()


# function to get districts belonging to a province
def get_districts(province: str) -> list:
    return DISTRICTS.get(province)


# function to get provinces belonging to a district
def get_constituencies(district: str) -> list:
    return CONSTITUENCIES.get(district)


# return
def get_all_districts(limit: int = 10) -> list:
    all_districts: list = []
    for district in DISTRICTS.values():
        all_districts += district
    return all_districts[:limit]


def get_all_constituencies(limit: int = 10) -> list:
    all_constituencies: list = []
    for constituency in CONSTITUENCIES.values():
        all_constituencies += constituency
    return all_constituencies[:limit]
