import json
from pathlib import Path


dictionary_file = Path("dictionary.json")
dictionary_backup = Path("dictionary.json.bak")
print("============================================")
print("| add vocabulary entries to the dictionary |")
print("===========================================")

# ensure dictionary file exists, create empty dictionary if not
if not dictionary_file.is_file():
    with open(dictionary_file, "w") as f:
        print("dictionary not existing, creating empty dictionary")
        json.dump([], f)
# ensure dictionary is json-loadable, create empty dictionary if not
try:
    with open(dictionary_file, "r") as f:
        json.load(f)
except:
    backup_file = dictionary_backup.name
    print(f"dictionary invalid, creating a backup '{backup_file}'")
    dictionary_backup.write_bytes(dictionary_file.read_bytes())
    print("creating empty dictionary")
    with open(dictionary_file, "w") as f:
        json.dump([], f)


def store_entry(entry: dict):
    with open(dictionary_file, "r") as f:
        dictionary: list[dict] = json.load(f)
    dictionary.append(entry)
    with open(dictionary_file, "w") as f:
        json.dump(dictionary, f, indent=2)


# loop indefinitly adding vocabulary to the dictionary
ctrl_d = False
while True:
    try:
        print("======================")
        print("new entry:")
        # get the information from the user
        print("enter hiragana:")
        hiragana = input(">>> ")
        ctrl_d = False  # reset Ctrl+D when the user added a new input

        print("enter nihongo (leave empty to use hiragana input):")
        nihongo = input(">>> ")
        if not nihongo:
            nihongo = hiragana

        print("enter english:")
        english = input(">>> ")

        # store entry in the dictionary
        entry = {
            "hiragana": hiragana,
            "nihongo": nihongo,
            "english": english,
        }
        store_entry(entry)
    except EOFError:
        print()  # newline to finish the input line of the user
        if ctrl_d:
            print("exiting...")
            break
        ctrl_d = True
        print("aborting current entry, press Ctrl+D again to exit")
