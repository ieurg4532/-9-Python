
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "TF14_1.txt"

file2_name = "TF14_2.txt"

file1w = Open(file1_name, "w")

if (file1w != None): 
    file1w.write("I want 10 candies, 13 cookies and 1 can of cola")
    print("Information was succesfully added to TF14_1.txt!")
    file1w.close()
    print("File TF14_1.txt was closed!")

file1r = Open(file1_name, "r")
file2w = Open(file2_name, "w")

if file1r != None and file2w != None: 
    for block in file1r.read().split(", "):
        for word in block.split(" "):
            if word.isnumeric():
                file2w.write(word + ' ')

print("Sequences of numbers are written through spaces in the file TF14_2")

file1r.close()
file2w.close()

print("Files was closed!")

file2r = Open(file2_name, "r")

number = 0 

if file2r != None:
    for i in file2r.read().split():
        print(i, end=' ')
        if int(i) > number: 
            number = int(i)

print("\nThe greatest number: ", number)

file2r.close()

print("File TF14_2.txt was closed!")