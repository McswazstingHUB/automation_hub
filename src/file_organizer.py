import os
import shutil

def organize_downloads():
    source = input("Directory to organize: ")

    if not os.path.isdir(source):
        print("Directory not found.")
        return

    for file in os.listdir(source):
        filepath = os.path.join(source, file)

        if os.path.isfile(filepath):
            ext = file.split(".")[-1] if "." in file else "other"

            target = os.path.join(source, ext)

            os.makedirs(target, exist_ok=True)

            shutil.move(filepath, os.path.join(target, file))

    print("Organization complete.")
