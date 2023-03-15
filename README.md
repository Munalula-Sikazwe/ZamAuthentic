# Zam-Authentic

Zam-Authentic is a Python package that provides validation functions for applications created in Zambia. It includes
validation for phone numbers, National Registration Card (NRC) numbers, and location data.

## Installation

You can install Zam-Authentic using pip:

Copy code

```commandline
pip install zam-authentic
```

Usage
Phone Number Validation
To validate a phone number, you can use the phonenumber_is_valid function:

python
Copy code

``` python
from zam_authentic.phone_number_validation import phonenumber_is_valid

is_valid = phonenumber_is_valid('+260978123456') # Returns True
```

## NRC Validation

To validate an NRC number, you can use the validate_nrc function:

python
Copy code

```python
from zam_authentic.nrc_validation.validate import validate_nrc

is_valid = validate_nrc('123456/78/9', delimiter='/')  # Returns True

```

Location Data Validation
To validate location data, you can use the validate_location function:

python
Copy code

License
This project is licensed under the MIT License - see the LICENSE file for details.
Get Districts
To get a list of districts in Zambia, you can use the get_districts function:

python
Copy code

```python
from zam_authentic.locations.get_locations import get_districts

districts = get_districts('province-name')
```

## Returns a list of district names

# Get Provinces

To get a list of provinces in Zambia, you can use the get_provinces function:

python
Copy code

```python
from zam_authentic.locations.get_locations import get_provinces

provinces = get_provinces()
```

## Returns a list of province names

# Get Constituencies

To get a list of constituencies in Zambia, you can use the get_constituencies function:

python
Copy code

```python
from zam_authentic.locations.get_locations import get_constituencies

constituencies = get_constituencies("district-name")
```

print(constituencies) # Returns a list of constituency names

Disclaimer
This package is intended for educational purposes only and is not intended to be used in production systems without
proper review and testing. The authors of this package are not responsible for any damages that may occur as a result of
using this package. Use at your own risk.