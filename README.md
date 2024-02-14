# adventure-game

    main function():
        read game dictionary
        Set intial node to start
        Create a while loop for player moving through game
            Make boolean false when player decides to quit or when he reaches end of the game

    Getgame function():
        Create game dictionary here
        load initial menu
        Each row of dictionary is a new node
        Return game dictionary

        Playgame function(gamedictionary):
        Load game dictionary
        Start menu begins at index 0
        create keepgoing while loop that moves player through each node to play
        print menu option
        Read input from player and move to menu A or B accordingly
        keepgoing is false when player reaches a lose node and decides to start over and play again
        return player node

