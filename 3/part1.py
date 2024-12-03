import re
regex = re.compile(r"mul\([0-9]+, ?[0-9]+\)")
numberRegex = re.compile(r"[0-9]+")

# just a shortcut
def mul_string(a, b):
    return int(a) * int(b)

with open("input_file.txt", "r") as file:
    file_contents = file.read()
    muls = regex.finditer(file_contents)
    result = 0
    # meaybe better optimization is possible
    # brute force for now
    for mul in muls:
       statement = mul.group()
       
       numbers = numberRegex.findall(statement)
       a, b = numbers
       print(f"{a} * {b}")
       result += mul_string(a, b)

    print(f"The result of the multiplication is: {result}")
