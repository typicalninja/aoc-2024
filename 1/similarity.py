import process

def gather_similarities(colA, colB):
    sim_score = 0
    for a in colA:
        # check how many elements in colB are equal to a
        count = colB.count(a)
        sim_score += a * count
        
    return sim_score
    

while True:
    file_path = input("Enter the file path: ")
    try:
        colA, colB = process.read_input_file(file_path)
    except FileNotFoundError:
        print("File not found. Please try again.")
    else:
        sims = gather_similarities(colA, colB)
        print(sims)
        break