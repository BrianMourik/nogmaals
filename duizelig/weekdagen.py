week = input("weekdag? ")

if (week.lower() == "maandag"):
    day = 1

elif (week.lower() == "dinsdag"):
    day = 2

elif (week.lower() == "woensdag"):
    day = 3

elif (week.lower() == "donderdag"):
    day = 4

elif (week.lower() == "vrijdag"):
    day = 5

elif (week.lower() == "zaterdag"):
    day = 6

elif (week.lower() == "zondag"):
    day = 7

else:
    print("Eyo das geen weekdag")

alter = 1
while alter <= day:
    if alter== 1:
        naam = "maandag"
    
    if alter== 2:
        naam = "dinsdag"

    if alter== 3:
        naam = "woensdag"

    if alter== 4:
        naam = "donderdag"

    if alter== 5:
        naam = "vrijdag"

    if alter== 6:
        naam = "zaterdag"

    if alter== 7:
        naam = "zondag"

    print(naam)
    alter = alter + 1
