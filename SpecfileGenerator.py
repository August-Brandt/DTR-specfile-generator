import random
import string
import sys

args = sys.argv
lines = 150

if len(args) > 1:
    lines = int(args[1])

header = "name,ring,quadrant,isNew,moved,description"
with open("specfile.csv", "w") as file:
    file.write(header + "\n")
    # add file content
    for _ in range(lines):
        # Create line as string
        values = []
        name = ""
        for _ in range(random.randint(2, 15)):
            name += random.choice(string.ascii_letters)
        values.append(name)
        values.append(random.choice(["hold", "assess", "trial", "adopt"]))
        values.append(random.choice(
            ["techniques", "platforms", "tools", "languages & frameworks"]))
        values.append(random.choice(["true", "false"]))
        values.append(str(random.randint(-3, 3)))
        desc = ""
        for _ in range(random.randint(20, 150)):
            desc += random.choice(string.ascii_letters)
        values.append(desc)

        # Write line to file
        file.write(",".join(values) + "\n")
