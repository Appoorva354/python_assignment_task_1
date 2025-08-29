try:
    with open("sample.txt","r") as f:
        print("Reading file content:")
        line_num=1
        for line in f:
            print(f"line {line_num}:{line.strip()}")
            line_num+=1
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")