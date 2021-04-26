import random


def roll(lower, upper):
    while True:
        print("Rolling the dices...")
        print(f"Your number is {random.randint(lower, upper)}")
        answerroll = input("Do you want to roll the dices again? (y/n) ")
        if answerroll.lower() == "n":
            print("""A pity that you want to play. Please leave my Inn. After that rude comment you find yourself back
                        #outside of The inn""")
            break

#class Location:
    #def __init__(self, name, gold):
        #self.name = name
        #self.gold = gold

    #def __str__(self):
        #return 'This location is called {}, there ' \
               #'is {} gold pieces here!'.format(self.name, self.gold)

    #def loot(self, amount_of_gold=10):
        #self.gold = self.gold - amount_of_gold
        #print('You have looted {} gold from {}!'.format(amount_of_gold, self.name))


#if __name__ == '__main__':
    #castle = Location('Castle Ravenloft', 50)
    #print(castle)

    # loot specific amount of gold from the castle
    #castle.loot(amount_of_gold=25)
    #print(castle)

    # loot the default amount
    #castle.loot()
    #print(castle)

    # loot a random amount of gold from the castle
    #random_amount = random.randint(0, 5)
    #print('Picked randomly this amount of gold: ', random_amount)
    #castle.loot(amount_of_gold=random_amount)
    #print(castle)


# main game loop:
# game_ongoing = True
#while game_ongoing:
        #answer = input('Want to continue playing?\n')
        #print('You said: {}, when asked if you want to play.')
#if answer == 'no':
         #game_ongoing = False
#pass



answer = input("""Welcome to ''Hunters of the truth'' a D&D choose-your-own-adventure game" 

You have been summoned to the tiny hamlet of Erwan, as many people have disappearance in the last weeks. 
As an heroic adventurer, this could be your first step into glory!...Or a certain death.
Are you ready to fulfill your destiny and become a hero to be reckon by? (yes/no)""")

if answer.lower().strip() == "yes":

    answer = input("""As so, your adventure begins...
After a few days of traveling you reach the hamlet of Erwan. 
The place seems desolate, as not a single soul can be seen around. An eerie silence engulfs the place as a shallow yellow 
mist engulfs the surroundings. Among the few battered houses, you see two places of interest, one seems to be an inn and
the other a trade post. Where do you want to go? (Inn/Trade Post)""").lower().strip()

    if answer.lower().strip() == "inn":
        answer = input("""There's an old crooked wooden post hanging outside of the inn with the name ''The Snappy Raven'' 
on it. As you enter the place you only see one person in the abandon place. A man stands behind the bar. He bids you
welcome and ask if you would you like to play a dice chance game. There's some money to be made in case you win. What do 
you say? Would you like to play (Yes/No)""").lower().strip()

if answer.lower().strip() == "yes":

    answer = input(""""Good! You pick up a set a dice set. The Innkeeper also pick up one and says: "Ok, let's play, who
    ever roll the highest number wins! You go first (Type OK to roll your dice)""").lower().strip()

    roll(1, 6)







#elif answer == "trade post":
        #print("A nice place indeed!")

        #else:
            #print("""Invalid choice. choose the inn or the trade post, sucker""""")

#else:
    #print("An unwise choice. As you choose to leave the hamlet of Erwan, darkness takes over the place.\n"
          #"    In a few months it disappears in a mist of shadows, never to be seen again.")
