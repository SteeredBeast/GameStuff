# the point in this program is to see how many times a key is obtained in the game 'lunch lady' for any player.
# the expected value of keys per spawn is 20%, so players can see if they are above, below or matching this.

# explanation to user
print("To use this program, type a \"1\" if you obtained a key and \"0\" if not.")
print("Then you will need to type how many spawns you checked after the \"-\" prompt.")
print("-------------------------------------------------------------------------------")
print("Example:\nCafe?: 1\n-----2")
print("-------------------------------------------------------------------------------")
print("This program WILL break if anything but a number is typed, and all progress will be lost.")
print("-------------------------------------------------------------------------------")
print("Expected percentage is 20%.")
print("-------------------------------------------------------------------------------")

# variables
cafe = 0
nurse = 0
pool = 0
run = 0
perCafe = 0
perNurse = 0
perPool = 0

# simple while loop for session
while run > -1:
    run = run + 1
    cafeKeys = int(input("Cafe?: "))
    cafeSpawns = int(input("-----: "))
    nurseKeys = int(input("Nurse?: "))
    nurseSpawns = int(input("------: "))
    poolKeys = int(input("Pool?: "))
    poolSpawns = int(input("-----: "))

    # add over multiple runs
    cafe = cafe + cafeKeys
    nurse = nurse + nurseKeys
    pool = pool + poolKeys
    perCafe = perCafe + cafeSpawns
    perNurse = perNurse + nurseSpawns
    perPool = perPool + poolSpawns

    # no divisions by 0
    if perCafe == 0:
        perCafe = perCafe + 1
    if perNurse == 0:
        perNurse = perNurse + 1
    if perPool == 0:
        perPool = perPool + 1

    # outputs
    print("Cafe:  ", round(cafe / run * 100), "%    -   Per spots checked: ", round(cafe / perCafe * 100), "%")
    print("Nurse: ", round(nurse / run * 100), "%  -   Per spots checked:", round(nurse / perNurse * 100), "%")
    print("Pool:  ", round(pool / run * 100), "%    -   Per spots checked: ", round(pool / perPool * 100), "%")
    print("You have done", run, "runs.")
    print("---------------------------------------------------------------------")
