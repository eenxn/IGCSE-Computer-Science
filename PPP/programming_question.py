Video = []
Results = []


while True:
    chose = int(input())

    if chose==1:
        while True:
            temp = []
            temp.append(input("Video Title: "))
            temp.append(input("Format: "))
            temp.append(input("Year Released: "))
            temp.append(input("Primary ID: "))

            Video.append(temp)

            continuemai = input("Do you want to add more (yes/no)? ")
            if continuemai.lower() == "no":
                break
    
    if chose==2:
        whattofind = input("Which Video you're looking for? ")
        isFound = False

        for i in range(0, len(Video)):
            if Video[i][0] == whattofind:
                Results.append(Video[i])
                isFound = True
        
        if isFound == False:
            print("not found")
            continue
        
        for row in range(0, len(Results)):
            for column in range(0, 4):
                print(Results[row][column], end = " ")
            print("")

    if chose==3:
        break