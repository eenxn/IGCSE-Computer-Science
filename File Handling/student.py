fr = open("File Handling/student.txt",'r')
fa = open("File Handling/student.txt",'a')

ls = []
for line in fr:
    line=line.strip()
    d = line.split(',')
    #print(d)
    print(f"Name: {d[0]}")
    print(f"Marks: {d[1]}")

    cur_mark = int(d[1])
    if cur_mark >= 90:
        d.append("A*")
    elif cur_mark>= 80:
        d.append("A")
    elif cur_mark>= 70:
        d.append("B")
    elif cur_mark>= 60:
        d.append("C*")
    elif cur_mark>= 50:
        d.append("D")
    elif cur_mark>= 40:
        d.append("E")
    elif cur_mark>= 30:
        d.append("F")
    else:
        d.append("U")

    print(f"Grade: {d[2]}")
    ls.append(d)
    print("")

fw = open("File Handling/student.txt", 'w')

print(ls)

for i in range(0, len(ls)):
    fa.write(ls[i][0])
    fa.write(',')
    fa.write(ls[i][1])
    fa.write(',')
    fa.write(ls[i][2])
    fa.write('\n')