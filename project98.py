def swapFileData():

    file1= input("Name it")
    file2= input("Swap it")

    with open("Research.txt",'r') as a :
        data_a = a.read()

    with open("Financial.txt",'r') as b:
        data_b = b.read()

    with open("Research.txt",'w+') as a:
        a.write(data_b)
    with open("Financial.txt",'w+') as b:
        
        b.write(data_a)        


swapFileData()