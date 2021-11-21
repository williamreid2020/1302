from Card import Card, Hand, Deck

NUMBER_OPPONENTS = 2
MAX_POINTS = 21
MAX_DEALER_POINTS = 17
user = ''
player_points = [0]*(2 + NUMBER_OPPONENTS)
player_cards = [[None for j in range(1)] for i in range(2 + NUMBER_OPPONENTS)]
player_state = [1]*(2 + NUMBER_OPPONENTS) #0 bust, 1 still playing, 2 stay, 3 win

bust = 0
still_playing = 1
stay = 2
win = 3

game_start = False

def restart():
    global play
    print("Do you want to play blackjack?\n")
    x = input("Enter Y for Yes and N for No: \n")
    if x.upper() == "Y":
      print('Starting game!')
      play = True
    elif x.upper() == "N":
      print('\nThank you!')
      play = False    
    else:
      restart()
    return play  

def play_game():
    print()       

def hit(hand):
    #add another card to hand, sum cards in hand and return value
    hand.add(game_deck.deal())
    sum_points(hand)
    display_hands(game_start)

def display_hands(game_start):
    if(game_start == False):
        for hand in hands_list:
            sum_points(hand)
        game_start = True
    #Have logic here if players stand or bust, add dealer card back into hand    
    for name, i in zip(player_names, hands_list):
        print(name,"'s hand:\n",i, "\n")
    if(player_state[hands_list.index(hands_list[0])] == still_playing):
        print("Next round")
        print("_"*20)
        
def sum_points(hand):
    n = all_hands.index(hand)
    cards = hand.get_ranks()
    card_values = []
    card_sum = 0
    for card in cards:
        if(card>=11):
            card = 10
        if(card == 1):
            if(player_points[n] + 11 > MAX_POINTS):
                card = 1
            else:
               card = 11
        card_values.append(card)
    player_points[n] = sum(card_values)
    #Creates list of cards for each player
    player_cards[n] = card_values
        
def update_state(state, n):    
    if(player_points[n] > MAX_POINTS):
        state = bust        
    if(player_points[n] == MAX_POINTS):
       state = win     
    player_state[n] = state
       
def display_points():
    for name, i in zip(player_names, player_points):
        print(name,"'s points:",i, "\n")

def user_play():
    while(player_state[1] == still_playing):
        if(player_points[hands_list.index(hands_list[1])] < MAX_POINTS):
            print("Would you like to hit or stand?\n")
            answer = input("Enter H for hit and S for stand: \n")
            if answer.upper() == "S":
                state = stay
            elif answer.upper() == "H":
                state = still_playing
                hit(hands_list[1])  
            else:
                user_play()
            update_state(state, hands_list.index(hands_list[1]))

def computers_play():
    for i in range(NUMBER_OPPONENTS):
        i = i + 2
        while(player_state[i] == still_playing):
            if(player_points[i] < 12):
                state = still_playing
                hit(hands_list[i])
            else:
                state = stay                
            update_state(state, i)

def dealer_play():
#Dealer plays until game ends
    while(player_state[0] == still_playing):
#Checks if dealer has flipped card, and shows flipped card if not already
        if(player_cards[0] == 1):
            hands_list[0].add(dealers_first_card)
#If dealer is >= 17 points, it doesn't hit. If its not, it hits.
        if(player_points[0] < MAX_DEALER_POINTS):
            state = still_playing
            hit(hands_list[0])
        if(player_points[0] >= MAX_DEALER_POINTS):
            state = stay
        update_state(state, hands_list.index(hands_list[0]))
    
def compare():
    #compare player hands against max_points
    for i in range(len(player_names)):
        if((max(player_points)) > MAX_POINTS):
            max_index = player_points.index(max(player_points))
            player_points[max_index] = 0
    winner = player_names[player_points.index(max(player_points))]
    print("player points: ", player_points)
    print("The winner is", winner)

        
##START CODE##
user = input("What is your name?\n")

#Shuffle deck
game_deck = Deck()
game_deck.shuffle()

#Create players
player_names = ['Dealer', user]
for n in range(NUMBER_OPPONENTS):
    name = 'Computer%s' % str(int(n)+1)
    player_names.append(name)

#Create player hands
hands = [None] * len(player_names)

all_hands = []
for i in range(len(hands)):
    hands[i] = Hand()
    hands[i].add(game_deck.deal())
    hands[i].add(game_deck.deal())
    all_hands.append(hands[i])

dealers_first_card = all_hands[0].discard_top()
##TODO##
#for loop to create 'n' computer hands

hands_list = []
for i in range(len(all_hands)):
    hands_list.append(all_hands[i])
print('ok')

##TODO##
#append computer hands to hands_list
#hands_list = [hands_list[0],hands_list[1]]
#hands_list.append(new_opponents) to append hands into list

#Running game code/while loop

display_hands(game_start)
user_play()
computers_play()
dealer_play()
compare()
print('game over')

#When all players stay or bust, dealer shows full hand then stays or hits


#play = restart()
