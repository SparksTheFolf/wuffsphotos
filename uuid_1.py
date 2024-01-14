import json
import random
import string

def generate_short_uuid(length=11):
    characters = string.digits + string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def generate_json_file(num_entries):
    data = {}

    for i in range(num_entries):
        photoname_ext = f"photo{i + 1}.jpg"  # Replace this with actual photo names and extensions
        fursona = input(f"Enter Fursona for {photoname_ext}: ")
        twitter_handle = input(f"Enter Twitter Handle for {photoname_ext} (Enter 'N/A' if not available): ")
        date_of_picture = input(f"Enter Date Of Picture for {photoname_ext}: ")

        # Generate 11-character UUID
        uuid = generate_short_uuid()

        data[photoname_ext] = {
            "Fursona": fursona,
            "TwitterHandle": twitter_handle,
            "DateOfPicture": date_of_picture,
            "UUID": uuid
        }

    with open('info.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Allow the user to choose the number of entries
num_entries = int(input("Enter the number of entries you want in the file: "))
generate_json_file(num_entries)
