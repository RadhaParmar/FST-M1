while True:
    player1 = input("Player1 Enter your option: ")
    player2 = input("Player2 Enter your option: ")

    if(player1.lower() == player2.lower()):
        print("Its a tie")
    elif(player1.lower() == "rock"):
        if(player2.lower() == "scissors"):
            print("Rock beates Scissors")
        else:
            print("Paper wins")
    elif(player1.lower() == "scissors"):
        if(player2.lower() == "paper"):
            print("Scissors beates Paper")
        else:
            print("Rock wins")
    elif(player1.lower() == "paper"):
        if(player2.lower() == "rock"):
            print("Paper beates rock")
        else:
            print("Scissors wins")
    elif((player1.lower() not in ("rock", "paper", "scissors")) and (player2.lower() not in ("rock", "paper", "scissors"))):
        print("Invalid option")
    
    repeat = input("Do you want to play another round? Yes/No: ").lower()
    if(repeat == "yes"):
        pass
    elif(repeat == "no"):
        raise SystemExit
    else:
        print("You entered an invalid option. Exiting now.")
        raise SystemExit
    