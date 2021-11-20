from Card import Card, Hand, Deck

NUMBER_OPPONENTS = 2
MAX_POINTS = 21
MAX_DEALER_POINTS = 17
user = ''
player_points = [0]*(2 + NUMBER_OPPONENTS)
player_cards = [[0 for j in range(1)] for i in range(2 + NUMBER_OPPONENTS)]
player_state = [0]*(2 + NUMBER_OPPONENTS) #0 play, 1 stay, 2 bust, 3 win
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
#    sum_points()
    display_hands()
    
def stand(player):
    #return hand numerical value after standing
    stand = True
    points = sum(player.get_ranks())
    return points
    
def compare(player):
    #compare player hands against max_points
    print('ok')

def display_dealer_hand():
    dealer_hand.add(dealers_first_card)
    points = sum(dealer_hand.get_ranks())
    return points

def display_hands():
    #Have logic here if players stand or bust, add dealer card back into hand    
    for name, i in zip(player_names, hands_list):
        print(name,"'s hand:\n",i, "\n")
    sum_points()    
    print("_"*20)

def sum_points():
    player_cards.clear()
    for n, i in zip(range(len(player_names)), hands_list):
        cards = i.get_ranks()
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
#        player_points.append(sum(card_values))
        player_points[n] = sum(card_values)
        #Creates list of cards for each player
        player_cards.append(card_values)
        update_state(n)
        
def update_state(n):
    state = 0
    if(player_names[n] == player_names[0]):
        if(player_points[n] >= MAX_DEALER_POINTS):
            state = 1
    if(player_points[n] > MAX_POINTS):
        state = 2
    player_state[n] = state
    
def display_points():
    for name, i in zip(player_names, player_points):
        print(name,"'s points:",i, "\n")

def dealer_play():
#Dealer plays until game ends
    while(player_state[0] == 0):
        print(player_state[0])
#Checks if dealer has flipped card, and shows flipped card if not already
        if(player_cards[0] == 1):
            dealer_hand.add(dealers_first_card)
#If dealer is >= 17 points, it doesn't hit. If its not, it hits.
        if(player_points[0] < MAX_DEALER_POINTS):
            hit(dealer_hand)
    
##START CODE##
player = input("What is your name?\n")

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

dealer_hand = all_hands[0]
dealers_first_card = dealer_hand.discard_top()
player_hand = all_hands[1]

##TODO##
#for loop to create 'n' computer hands
computer1_hand = all_hands[2]
computer2_hand = all_hands[3]

hands_list = [dealer_hand, player_hand, computer1_hand, computer2_hand]

##TODO##
#append computer hands to hands_list
#hands_list = [dealer_hand, player_hand]
#hands_list.append(new_opponents) to append hands into list

#Running game code/while loop
display_hands()


dealer_play()

print(player_cards)
print(player_points)
print(player_state)
print("All hands have been dealt")

#When all players stay or bust, dealer shows full hand then stays or hits


#play = restart()
