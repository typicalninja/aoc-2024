def process_lines(lines):
    col_a = []
    col_b = []
    
    for line in lines:
        a, b = line.split()
        col_a.append(int(a))
        col_b.append(int(b))
        
    # sort each column in ascending order
    col_a.sort()
    col_b.sort()
    
    distance_between_pairs = []
    # assume that both columns have the same length
    for i in range(len(col_a)):
       smallest_a = col_a[i]
       smallest_b = col_b[i]
       print(smallest_a, smallest_b)
       if smallest_b == smallest_a:
           distance_between_pairs.append(0)
       elif smallest_b > smallest_a:
           distance_between_pairs.append(smallest_b - smallest_a)
       else: 
            distance_between_pairs.append(smallest_a - smallest_b)
            
    return sum(distance_between_pairs)

while True:
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print(process_lines(lines))
    except FileNotFoundError:
        print("File not found. Please try again.")
    else:
        break