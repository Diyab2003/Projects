import phonenumbers
from phonenumbers import geocoder

# List of phone numbers to parse
phone_numbers = [
    "+971 589397436",
    "+91 9935678231",
    "+974 66844755",
    "+1 12505550199",
    "+64 0218321436"
]

# Function to parse and get location of a phone number
def get_phone_number_location(number):
    try:
        parsed_number = phonenumbers.parse(number)
        return geocoder.description_for_number(parsed_number, "en")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return f"Error: {e}"

# Track phone numbers
print("\nPhone numbers location\n")
for number in phone_numbers:
    location = get_phone_number_location(number)
    print(f"{number}: {location}")
