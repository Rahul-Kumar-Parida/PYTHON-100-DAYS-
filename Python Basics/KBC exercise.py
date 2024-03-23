Questions = [
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,2],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,2],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,2],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,2],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,2],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language w4as used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which 2anguage was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language 2as used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4],
    ["Which language was used to create Free Fire?", "Python" , "Java", "JavaScript","Ruby", "None" ,4]
]
levels = [1000,2000,3000, 5000, 10000, 20000,40000,80000,160000,320000]
money = 0
for i in range(0 , len(Questions)):
    question = Questions[i]
    print(f"\n\n Question for Rs. {levels[i]} \n  " )
    print(f"a. {question[1]} b. {question[2]}")
    print(f"c. {question[3]} d. {question[4]}")
    reply = int(input("enter your answer (1-4) or press 0 to quit game:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer , you have won Rs. {levels[i]}")
        if(i == 4):
            money = 1000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money =10000000
    else:
        print("wrong answer")
        break
print(f"your take home money is{money}")