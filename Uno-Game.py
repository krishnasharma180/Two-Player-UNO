import random

str = " \033[42;1;91m NOT SOO EPIC GAME PRESENTS \033[m "
str2 = "  \033[1;91m Two Player UNO  \033[m "

#Starting of the game

print("|{: ^100}|\n".format(str))
print("|{:*^100}|\n".format(str2))

# Instruction for game 

def print_instructions():
    print("\n\033[1;92m--- GAME INSTRUCTIONS ---\033[m\n")
    print("1. This is a two-player UNO game. Each player is dealt 7 cards at the start.")
    print("2. The game begins with a card from the deck being placed in the center.")
    print("3. Players take turns to match a card from their hand with the card in the center.")
    print("   - A match occurs when the colors or the numbers on the cards are the same.")
    print("   - Special cards such as Skip, Reverse, Draw Two, and Wild can also be played.")
    print("4. If a player cannot match a card, they must draw a card from the deck.")
    print("   - A card is drawn from the deck by writing 456 in the choice.")
    print("5. The game continues until one player runs out of cards or the game is interrupted.")
    print("6. The player who runs out of cards first wins the game!")
    print("\n\033[1;92m--- SPECIAL CARDS ---\033[m")
    print("   - \033[1;31mSkip\033[m: The next player loses their turn.")
    print("   - \033[1;32mReverse\033[m: Reverses the direction of play.")
    print("   - \033[1;33mDraw Two\033[m: The next player must draw two cards and skip their turn.")
    print("   - \033[1;35mWild\033[m: Allows the player to choose the next color to play.")
    print("   - \033[1;34mWild Draw Four\033[m: Allows the player to choose the next color and forces the next player to draw four cards.")
    print("\nGood luck and have fun playing UNO!")
    print("\n\033[1;92m--- END OF INSTRUCTIONS ---\033[m\n")

print_instructions()

first = input(f"\033[1;94m Enter name of 1st player :\033[m ").capitalize()
second = input(f"\033[1;104m Enter name of 2nd player :\033[m ").capitalize()

#all cards
cards = [
    "Red 0", "Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
    "Yellow 0", "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7", "Yellow 8", "Yellow 9",
    "Green 0", "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7", "Green 8", "Green 9",
    "Blue 0", "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8", "Blue 9",
    "Skip Red", "Skip Yellow", "Skip Green", "Skip Blue",
    "Reverse Red", "Reverse Yellow", "Reverse Green", "Reverse Blue",
    "Draw Two Red", "Draw Two Yellow", "Draw Two Green", "Draw Two Blue",
    "Wild", "Wild", "Wild", "Wild",
    "Wild Draw Four", "Wild Draw Four", "Wild Draw Four", "Wild Draw Four"
]

# colors for cards
coc={
   "Red":31,
   "Blue":96,
   "Green":32,
   "Yellow":93,
   "Red":31,
   "Wild":37,
}

left =[cards[0]]
cards.pop(0)

# first card from remaining deck
def first_card():

   print(f"\033[1;98;101m Main Card \033[m",end="  ")
   x= left[0]
   q = x.split()
   if(q[0]=="Skip" or q[0]== "Reverse"):
      print(" "*37+ f"\033[1;{coc[f'{q[1]}']}m------------------",end="")
   elif(q[0]=="Draw"):
      print(" "*37+ f"\033[1;{coc[f'{q[2]}']}m------------------",end="")
   else:   
      print(" "*37+ f"\033[1;{coc[f'{q[0]}']}m------------------",end="")
   print(" ")
   for i in range(0,5):
    if(i==2):
        print(" "*50+ f"  {left[0]}")
    
    print(" "*50+"|                |")
   2
   
   print(" "*50+"------------------\033[m",end="")
   print("\n")
# function for pritnting cards
def card(name,total,player):
 if total==0:
      return 
 print(f"{name} cards")
 print("------------------  " * total)
 for i in range(5):
    if  i == 2: 
        for j in range(total):
            
            print("{: ^18}".format(player[j]), end="  ")
        print()
    
    for j in range(total):
          x= player[j]
          q = x.split()
          if(q[0]=="Skip" or q[0]== "Reverse"):
           print(f"\033[1;{coc[f'{q[1]}']}m|                |\033[m", end="  ")
          elif(q[0]=="Draw"):
              print(f"\033[1;{coc[f'{q[2]}']}m|                |\033[m", end="  ")
          else:   
           print(f"\033[1;{coc[f'{q[0]}']}m|                |\033[m", end="  ")
         
    print()

 print("------------------  " * total)
 print("\n")

# distribution of cards to players
player1=[]
for i in range(0,7):
   n1 = random.randint(0,len(cards))-1
   player1.append(cards[n1])
   cards.pop(n1)
player2=[]
for i in range(0,7):
   n2 = random.randint(0,len(cards))-1
   player2.append(cards[n2])
   cards.pop(n2)

# function for how game works
def game_play(player,j,r,name):
      any= random.randint(0,len(cards))-1
      while r:       
        first_card() 
        card(name,len(player),player)
        print("|{:*^100}|\n".format(f" \033[93;1m{name}'s chance to play \033[m"))

        choice = int(input(f"Enter your choice: "))
        if(choice==456):
           print("|{:*^100}|\n".format("A card is taken from the deck"))
           another = random.randint(0,len(cards))-1
           player.insert(-1,cards[another])
           cards.pop(another)
           r=False
           continue
        elif(choice>len(player)):
           print("\033[2J\033[H", end="")
           print("|{:!^100}|\n".format("\033[1;94mEnter a valid number\033[m"))
           continue
        a = left[0]
        d=a.split()
        b = player[choice -1]
        c=b.split()
        an=list(filter(lambda x: x in d, c))
        if(len(an)==0):  
           if("Wild" in c):
              if(len(c)==1):
                color = (input("Enter your color choice:").capitalize())
                player.pop(choice-1)
                left.insert(0,color)
                r =False
                d = color
              else: 
                 color = (input("Enter your color choice:").capitalize())
                 player.pop(choice-1)
                 left.insert(0,color)
                 d = color
                 for i in range(0,4):
                   any= random.randint(0,len(cards))-1
                   j.append(cards[any])
                 r=False
           else:
               print("\033[2J\033[H", end="") 
               print("|{:!^100}|\n".format("\033[1;94mEnter a valid card or take it from the deck\033[m "))
               continue

        elif(len(an)!=0):
           if("Skip" in c):
               print("skip")
           elif("Reverse" in c):
               print("reverse")
           elif("Four" in c):
                 color = (input("Enter your color choice:").capitalize())
                 player.pop(choice-1)
                 left.insert(0,color)
                 d = color
                 for i in range(0,4):
                   any= random.randint(0,len(cards))-1
                   j.append(cards[any])
                 r=False
           elif(len(c)==3):  
              v=random.randint(0,len(cards))-1   
              print(len(cards),v,any)
              j.append(cards[v])
              cards.pop(v)
              j.append(cards[any])
              cards.pop(any)
              r = False
           else:
              r=False
           left.insert(0,player[choice-1])

           player.pop(choice-1)        
some = True
# Game play chance by chance
while some:
        game_play(player1, player2, True, first)
        if len(player1) == 0 or len(player2) == 0: 
             print("\033[2J\033[H", end="")  # Clears the screen
             print("|{:*^100}|\n".format(" UNO... "))
             print("|{: ^100}|\n".format(f"{first} Won"))
             print("#" * 100, "\n\nMade By : Krishna\nPlayed By :", first, "and", second, "\nLanguage Use : Python\nThank You for Playing  ^v^\n", "\033[1B \033[51D", "#" * 100, sep=" ")
             some = False  # Stop the game
             break 
        game_play(player2, player1, True, second)
        if len(player1) == 0 or len(player2) == 0: 
             print("\033[2J\033[H", end="") 
             print("|{:*^100}|\n".format(" UNO... "))
             print("|{: ^100}|\n".format(f"{second} Won"))
             print("#" * 100, "\n\nMade By : Krishna\nPlayed By :", first, "and", second, "\nLanguage Use : Python\nThank You for Playing  ^v^\n", "\033[1B \033[51D", "#" * 100, sep=" ")
             some = False 
             break  
