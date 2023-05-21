import json
from pathlib import Path


dictionary_file = Path("dictionary.json")
print("===========================================")
print("| fuzzy search for the dictionary entries |")
print("===========================================")

# loop indefinitly searching in the dictionary
while True:
    # get the search input from the user
    search_input = input(">>> ")

    # perform fuzzy search through all keys in the dictionary
    with open(dictionary_file, "r") as f:
        dictionary: list[dict[str, str]] = json.load(f)
    for entry in dictionary:
        for value in entry.values():
            has_error = False
            # loop through the characters entered by the user
            # and check that they appear in-that-order in this entry
            for char in search_input:
                try:
                    # test to find the index of the character
                    idx = value.index(char)
                    # if the test is successful, update value and test next
                    value = value[idx:]
                except ValueError:
                    # character not found, this entry doesn't match
                    has_error = True
                    break
            if has_error:
                # continue the value loop, as this value failed
                continue
            # at this point, a value in the entry matches, print and break
            print("===========================================")
            print(f"hiragana: {entry['hiragana']}")
            print(f"nihongo: {entry['nihongo']}")
            print(f"english: {entry['english']}")
            break
