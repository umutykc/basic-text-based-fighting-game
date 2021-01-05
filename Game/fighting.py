my_health = 100
mana = 200
energy = 200
orge_health = 300
while True:
    command = input()
    
    if command == "fighting help":
        print("""
        light attack -- take 10 health point(takes 10 energy point)
        med attack -- take 20 health point(takes 20 energy point)
        heavy attack -- take 30 health point(takes 30 energy point)
        light magic -- take 10 health point(takes 10 mana)
        med magic -- take 20 health point(takes 20 mana)
        heavy magic -- take 30 health point(takes 30 mana)
        health cure -- gives 30 health""")

    if command == "light attack":
        if energy < 10:
            print("You don't have enough energy.")
        orge_health = orge_health - 10
        energy = energy - 10
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your energy is {energy}\nOrge punched you, now your health is {my_health}.")
    
    if command == "med attack":
        if energy < 20:
            print("You don't have enough energy.")
        orge_health = orge_health - 20
        energy = energy - 20
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your energy is {energy}\nOrge punched you, now your health is {my_health}.")

    if command == "heavy attack":
        if energy < 30:
            print("You don't have enough energy.")
        orge_health = orge_health - 30
        energy = energy - 30
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your energy is {energy}\nOrge punched you, now your health is {my_health}.")

    if command == "light magic":
        if mana < 10:
            print("You don't have enough mana.")
        orge_health = orge_health - 10
        mana = mana - 10
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your mana is {mana}\nOrge punched you, now your health is {my_health}.")

    if command == "med magic":
        if mana < 20:
            print("You don't have enough mana.")
        orge_health = orge_health - 20
        mana = mana - 20
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your mana is {mana}\nOrge punched you, now your health is {my_health}.")

    if command == "heavy magic":
        if mana < 30:
            print("You don't have enough mana.")
        orge_health = orge_health - 30
        mana = mana - 30
        my_health = my_health - 30
        print(f"Orge has damaged, now orge's health is {orge_health}\nNow your mana is {mana}\nOrge punched you, now your health is {my_health}.")

    if command == "health cure":
        if my_health <= 70:
            my_health = my_health + 30
            print(f"Your health increased to {my_health}.")
        elif my_health >70 and my_health < 100:
            my_health = my_health + (100 - my_health)
            print(f"Your health increased to {my_health}.")
        elif my_health == 100:
            print("Your health is already full.")         

    if my_health == 0:
        print("You lose.")
        break
    
    if orge_health == 0:
        print("You win.")
        break

