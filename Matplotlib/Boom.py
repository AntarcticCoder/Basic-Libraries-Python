import time as t
t.sleep(2)
print("Loading..")
t.sleep(3)
hackList = [
    "Start Attacking......",
    "Boomboombing kongpop's house 0% ",
    "Boomboombing kongpop's house 20% --",
    "Boomboombing kongpop's house 40% ----",
    "Boomboombing kongpop's house 60% ------",
    "Boomboombing kongpop's house 80% --------",
    "Boomboombing kongpop's house 99% ---------",
    "ERROR!",
    "Please enter a password first!"
]

for i in range(len(hackList)):
    print(hackList[i])
    if i == 5:
        t.sleep(3)
    elif i == 5 or i == 6:
        t.sleep(4.5)
    else :
        t.sleep(2.5)

password = input("password : ")
if password.upper() == "KONGPOPISAFEMBOY" :
    t.sleep(1.5)
    print("correct!")
    t.sleep(2)
    print("Boomboomed kongpop's house successfully!")
    t.sleep(1)
    print("now just send Ez Noob to kongpop")
else :
    print("wrong!. noob")
