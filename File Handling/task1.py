fr = open("student.txt",'r')
#fw = open("student.txt",'a')
for line in fr:
    line=line.strip()
    d = line.split(',')
    print(f"Name: {d[0]}")
    print(f"Marks: {d[1]}")

    print("")
