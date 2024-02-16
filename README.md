# adventure-game

    main function():
        read game dictionary
        Set intial node to start
        Create a while loop for player moving through game (playgame is active)
            start menu begings at index 0
            Make boolean false when player decides to quit or when he reaches end of the game

    Getgame function():
        Create game dictionary here
        load initial menu
        Each row of dictionary is a new node
        Return game dictionary

        Playgame function(gamedictionary):
        Read node key from dictionary
        The current node gets input from user 
        Print menu (
        Menu A
        Menu B)
        if user input is valid
            Read user input and reset state to A or B(pressing 1 or 2)
        Else: Don't change state, new node is still current node

