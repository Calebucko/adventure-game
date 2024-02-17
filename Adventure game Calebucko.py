# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:15:36 2024

@author: Caleben Jahn
"""

def main():
    game=getgame()
    print(f'{game["Start"][0]}')
    currentnode= playnode(game, "Start")
    keepgoing = True
    while(keepgoing):
        if currentnode=="Quit":
            keepgoing= False
        else:
            currentnode=playnode(game, currentnode)
    
    
    
def getgame():
    game = {
        "Name": ["Description", "OptionA", "NodeA", "OptionB", "NodeB"], 
        "Quit": ["See ya later compadre."],
         "Start": ["You're a wandering outlaw who's trying to change his ways, roaming the mojave trying to find a place to call home. After riding for 2 days straight you enter the town of babacos. The locals are mistrustful.", "Enter the saloon", "Saloon", "Mingle with the locals", "Mingle"], 
         "Saloon": ["The music stops as you enter. Everyone turns to you, leering.", "Quietly approach the bar", "Bar", "Crack a joke", "Joke"], 
         "Mingle": ["The group you've inserted yourself into sticks you with their six shooters. These locals aren't ones for mingling.", "Start over", "Start", "Quit", "Quit"], 
         "Bar": ["The bartender aims his lever action at you and tells you to get out. Your time in babacos is over.", "Start over", "Start", "Quit", "Quit"], 
         "Joke": ["Luckily, you get a rousing laugh for making light of the situation. You jaunt around the place as the music kicks up again", "Grab a drink", "Drink", "Join a card game", "Cards"], 
         "Drink": ["That one drink quickly turns into 5. People start buying you drinks for your joke. You can't control yourself, and that 5 quickly turns into 40. The alcohol eventually does you in.", "Start over", "Start", "Quit", "Quit"], 
         "Cards": ["You refrain from the drinks and ask to join an open spot at the poker table. 'Only if you play the last mans hand', one of the players says. The last man had the worst hand you've ever seen", "Decide to take your leave", "Leave", "Play the hand anyway", "Play"], 
         "Leave": ["You attempt to leave the game for something else, but the man didn't take to kindly to that. You're riddled with bullet holes before you can walk 3 feet. They call it a dead mans hand for a reason. ", "Start over", "Start", "Quit", "Quit"], 
         "Play": ["You play the hand anyway. You miraculously win as the last card is placed on the river, and one of the men is absolutely incensed, and he aims his revolver at you!", "TRY TO DODGE", "Dodge", "wait for the right moment", "Wait"], 
         "Dodge": ["Believe it or not, that brass is faster than you are. You're dead as a doornail.", "Start over", "Start", "Quit", "Quit"], 
         "Wait": ["At the moment he's about to shoot you, a drunkard sees the drawn revolver and shouts for a brawl. The place immediately goes haywire, bottles, bullets, and brass knuckles are flying freely.", "Open fire!", "Fire", "Start swingin!", "Swing"], 
         "Fire": ["You start firing in all directions, running around the place like a madman. Suddenly, you notice that a fuse attached to a large stack of dynamite is about to go off. Why is that HERE?? A stray bullet must have set it off!", "Get down!", "Down", "Get out of the building", "Building"], 
         "Swing": ["You're throwing hands in all directions, knocking drunken fellers down like the boxing champion of the world. You eventually end up swinging your fist into the stomach of a very large and very angry patron of the bar. He breaks you in half and tosses your paralyzed body to the next county.", "Start over", "Start", "Quit", "Quit"], 
         "Down": ["Dropping the floor didn't do much. The dynamit goes off about 5 seconds later and the building is blown to smithereens, and your charred carcass flies about 2 miles away. ", "Start over", "Start", "Quit", "Quit"], 
         "Building": ["You start running and bust out a window. You get about 5 feet away before the explosion goes off, and the blastwave carries you another 50. Miraculously, you pick yourself up and seem to be fine, along with a couple other survivors. That blast seems to  have blown up the whole town. You don't know how you survived.", "Settle down", "Settle", "Depart", "Depart"], 
         "Settle": ["You decide to pick up the pieces and settle down here, as you feel like you have a new found attachement to the place. You quickly come to find that its almost impossible to live here, as there is no more access to food, water, or really any housing. You're unable to escape to a more civilized place, and you die in the desert. How was that a good idea?", "Start over", "Start", "Quit", "Quit"], 
         "Depart": ["Bewildered, bruised up, and slightly traumatized, you leave babacos, a changed man leaving behind a changed town. As in that town is basically gone now. But that's okay, it would've become a ghost town anyway, gold rush was 40 years ago. You'll find somewhere else further out east. Try not to blow it up this time ok?", "Quit", "Quit", ""] 
        
        }
    return game

def playnode(game, currentnode):
    choice= input(f"""what will you do?
    1) {game[currentnode][1]}
    2) {game[currentnode][3]}   """)
                  
    if choice == "1":
        currentnode= game[currentnode][2]
        print(f'{game[currentnode][0]}')
    elif choice == "2":
        currentnode= game[currentnode][4]
        print(f'{game[currentnode][0]}')
    else:
        print("Type 1 or 2")
        
    return currentnode

main()
                  
    
                  
                  
                  
    