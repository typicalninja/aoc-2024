import re
regex = re.compile(r"mul\([0-9]+, ?[0-9]+\)")
numberRegex = re.compile(r"[0-9]+")
dontsRegex = re.compile(r"don't\(\)")
doRegex = re.compile(r"do\(\)")

def mul_string(a, b):
    return int(a) * int(b)

with open("input_file.txt", "r") as file:
    file_contents = file.read()
    muls = regex.finditer(file_contents)
    donts = dontsRegex.finditer(file_contents)
    dos = doRegex.finditer(file_contents)

    donts_end = []
    dos_end = []

    for donts in donts:
        statement_end = donts.end()
        donts_end.append(statement_end)

    for dos in dos:
        statement_end = dos.end()
        dos_end.append(statement_end)

    result = 0
    # meaybe better optimization is possible
    # brute force for now
    for mul in muls:
       statement = mul.group()
       statement_end = mul.end()
       statement_dont = False
       matched_dont = 0

       # check if the statement has a dont() or do() before it
       # if it has a dont() before it, check if it has a do() after it but before the statement
       for dont in donts_end:
            if dont < statement_end:
                matched_dont = dont
                statement_dont = True

       if statement_dont:
        for do in dos_end:
                if do > matched_dont and do < statement_end:
                    statement_dont = False



       if statement_dont:
           continue

       numbers = numberRegex.findall(statement)
       a, b = numbers
       print(f"{a} * {b}")
       result += mul_string(a, b)

    print(f"The result of the multiplication is: {result}")
