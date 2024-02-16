# adventure-game

    main function():
        read game dictionary
        Set intial node to start(using currentnode)
        Create a while loop for player moving through game (playgame is active)
            currentnode=playnode(next)
            Make boolean false when player decides to quit or when he reaches end of the game

    Getgame function():
        Create game dictionary here
        load initial menu
        Each row of dictionary is a new node
        Return game dictionary

        Playgame function(gamedictionary, currentnode):
        Read node key from dictionary
        The current node gets input from user 
        Print menu (
        Menu A
        Menu B)
        if user input is valid and input is 1
            Change state to node A
        elif user input is valid and input is 2
            Change to state node B
        Else: Invalid input
            Don't change state, new node is still current node
            Return current node

