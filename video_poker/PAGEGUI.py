'''Module ran to start the program, Poker: 5 Card Redraw'''
import sys
import os.path

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

import video_poker
import video_poker_functions

PLAYERHAND = []
DECK = []

#Variables for buttons deciding whether a card is held or redrawn.
Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold = False, False, False, False, False

#Get the current directory and default the bet amount to 0.
localFileDirectory = os.path.dirname(os.path.realpath(__file__))
assetFileDirectory = os.path.join(localFileDirectory + '\Assets')


def load_player_balance(bank_file_location = localFileDirectory) -> int:
    '''Load the player balance from bank.txt'''
    bank_store_path = os.path.join(bank_file_location, 'bank.txt' )
    bank_store = open(bank_store_path, 'r', encoding = 'utf-8')
    return int(bank_store.read())
PLAYERMONEY = load_player_balance()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Credits (root)
    video_poker.init(root, top)
    root.mainloop()

"""
w = None
def create_Credits(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Credits(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = rt
    w = tk.Toplevel (root)
    top = Credits (w)
    video_poker.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Credits():
    '''Destroy the window'''
    global w
    w.destroy()
    w = None
"""

class Credits:
    ''' '''
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.
        All other window objects are initialized and defined here.
        '''
        #Initializing runtime values
        self.bet_amount = 0
        self.status_deal_button = True #Start state as "new hand"

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85' was d9d9d9
        _fgcolor = '#000000'  # X11 color: 'black'

        #This Section controls the game window name and color
        top.geometry("1920x1060")
        top.minsize(120, 1)
        top.maxsize(1920, 1080)
        top.resizable(1,  1)
        top.title("5 Card Draw")
        top.configure(background="#00008b")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        #global card image
        default_card_back_file = os.path.join(assetFileDirectory + '\cardBack.png')
        defaultImage = tk.PhotoImage(file=default_card_back_file)

        #Intialize card 1 (Furthest card left)
        self.Card1 = tk.Button(top)
        self.Card1.place(relx=0.016, rely=0.386, height=508, width=349)
        self.Card1.configure(activebackground="#ececec")
        self.Card1.configure(
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=defaultImage,
            pady="0",
            command=self.Card1_command,
            text='''Button'''
        )
        self.Card1.Image = defaultImage

        #Intialize card 2
        self.Card2 = tk.Button(top)
        self.Card2.place(relx=0.203, rely=0.386, height=508, width=350)
        self.Card2.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=defaultImage,
            pady="0",
            command=self.Card2_command,
            text='''Button'''
        )
        self.Card2.Image = defaultImage

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        #Intialize card 3
        self.Card3 = tk.Button(top)
        self.Card3.place(relx=0.391, rely=0.386, height=508, width=350)
        self.Card3.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=defaultImage,
            pady="0",
            command=self.Card3_command,
            text='''Button'''
        )
        self.Card3.Image = defaultImage

        #Intialize card 4
        self.Card4 = tk.Button(top)
        self.Card4.place(relx=0.578, rely=0.386, height=508, width=350)
        self.Card4.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=defaultImage,
            pady="0",
            command=self.Card4_command,
            text='''Button'''
        )
        self.Card4.Image = defaultImage

        #Intialize card 5
        self.Card5 = tk.Button(top)
        self.Card5.place(relx=0.766, rely=0.386, height=508, width=350)
        self.Card5.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=defaultImage,
            pady="0",
            command=self.Card5_command,
            text='''Button'''
        )
        self.Card5.Image = defaultImage

        #Initialize the bottom center display the number of winnings
        self.Winnings = tk.Message(top)
        self.Winnings.place(relx=0.026, rely=0.877, relheight=0.093, relwidth=0.178)
        self.Winnings.config(font=("Courier", 44))
        self.Winnings.configure(
            background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Winnings''',
            width=342
        )

        #Initialize display for current credits
        self.CurrentCredits = tk.Message(top)
        self.CurrentCredits.place(relx=0.771, rely=0.877, relheight=0.094, relwidth=0.178)
        self.CurrentCredits.config(font=("Courier", 55))
        self.CurrentCredits.configure(background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text=PLAYERMONEY,
            width=341
        )

        #Initialize the banner image at the top
        self.Banner = tk.Button(top)
        self.Banner.place(relx=0.015, rely=0.019, height=300, width=1800)
        bannerFile = (os.path.join(assetFileDirectory + '\BackgroundImage3.png'))
        bannerImage = tk.PhotoImage(file=bannerFile)
        self.Banner.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=bannerImage,
            pady="0",
            text='''Button'''
        )
        self.Banner.image = bannerImage

        #Initialize the button for holding card 1
        self.CardHeld1 = tk.Message(top)
        self.CardHeld1.place(relx=0.096, rely=0.358, relheight=0.024, relwidth=0.026)
        self.CardHeld1.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held''',
            width=60
        )

        #Initialize the button for holding card 2
        self.CardHeld2 = tk.Message(top)
        self.CardHeld2.place(relx=0.276, rely=0.358, relheight=0.024, relwidth=0.026)
        self.CardHeld2.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held''',
            width=60
        )

        #Initialize the button for holding card 3
        self.CardHeld3 = tk.Message(top)
        self.CardHeld3.place(relx=0.464, rely=0.358, relheight=0.025, relwidth=0.026)
        self.CardHeld3.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held''',
            width=60
        )

        #Initialize the button for holding card 4
        self.CardHeld4 = tk.Message(top)
        self.CardHeld4.place(relx=0.651, rely=0.358, relheight=0.025, relwidth=0.026)
        self.CardHeld4.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held''',
            width=60
        )

        #Initialize the button for holding card 5
        self.CardHeld5 = tk.Message(top)
        self.CardHeld5.place(relx=0.849, rely=0.358, relheight=0.025, relwidth=0.026)
        self.CardHeld5.configure(width=60)
        self.CardHeld5.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held'''
        )

        #Initialize the bet_one button
        self.Bet_One = tk.Button(top)
        self.Bet_One.place(relx=0.214, rely=0.877, height=90, width=150)
        self.Bet_One.config(font=("Courier", 22))
        self.Bet_One.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            pady="0",
            text='''Bet One''',
            command=self.bet_one_command
        )

        #Initialize the bet_max button
        self.Bet_Max = tk.Button(top)
        self.Bet_Max.place(relx=0.297, rely=0.877, height=90, width=140)
        self.Bet_Max.config(font=("Courier", 22))
        self.Bet_Max.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            pady="0",
            text='''Bet Max''',
            command=self.bet_max_command
        )

        #Initialize the current bet display
        self.Current_Bet = tk.Message(top)
        self.Current_Bet.place(relx=0.391, rely=0.877, relheight=0.09, relwidth=0.178)
        self.Current_Bet.config(font=("Courier Bold", 100))
        self.Current_Bet.configure(
            background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''1''',
            width=342
        )

        #initialize the deal and redraw button
        self.Deal = tk.Button(top)
        self.Deal.place(relx=0.604, rely=0.877, height=90, width=300)
        self.Deal.config(font=("Courier", 44))
        self.Deal.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",highlightbackground="#d9d9d9",
            highlightcolor="black",
            pady="0",
            text='''New Hand''',
            command=self.deal_command
        )

        #Initialize winning Hand banner in top center
        self.winning_hand = tk.Message(top)
        self.winning_hand.place(relx=0.325, rely=0.300, relheight=0.053, relwidth=0.300)
        self.winning_hand.config(font=("Courier", 44))
        self.winning_hand.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="Red",
            text='''Hand Rank''',
            width=500
        )

        #Intial update of images into client
        root.update_idletasks()

    def deal_command(self):
        '''Function progressing state of the hand.
        Alternates between redrawing cards or starting a new hand, and starting scoring.'''
        global PLAYERMONEY, Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold, PLAYERHAND, DECK
        print(f' Player Hand: {PLAYERHAND}')

        #This list is used to update the card images for both redrawing and starting new hands.
        card_list = [self.Card1, self.Card2, self.Card3, self.Card4, self.Card5]
        
        if self.status_deal_button:
            print("Starting New Hand")
            #Creating player hand and clearing previous winning hand rank and winnings.
            PLAYERHAND, DECK = video_poker_functions.create_hand(DECK)
            self.winning_hand.configure(text='')
            self.Winnings.configure(text='')

            #Subract Bet Amount
            PLAYERMONEY = PLAYERMONEY - (self.bet_amount + 1)
            self.CurrentCredits.configure(text=PLAYERMONEY)


            #Updating the image of all cards in hand
            for index, card in enumerate(PLAYERHAND):
                new_card_file = (os.path.join(assetFileDirectory, card)) + '.png'
                new_card_image = tk.PhotoImage(file = new_card_file)
                card_list[index].configure(image = new_card_image)
                card_list[index].image = new_card_image

            #change the redraw / new hand button to redraw
            self.status_deal_button = False
            self.Deal.configure(text='''Redraw''')
            root.update_idletasks()

        else:
            #This phase redraws cards and immediately scores the redrawn cards.
            print("Redrawing unheld cards")

            #Drawing new cards for each held card and updating their images.
            card_hold_status_list = [Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold]
            for index, card_hold_status in enumerate(card_hold_status_list):
                if card_hold_status is False:
                    new_card, DECK = video_poker_functions.draw_cards(DECK, 1)
                    new_card = ''.join(new_card)
                    PLAYERHAND[index] = new_card
                    new_card_file = os.path.join(assetFileDirectory, new_card) + '.png'
                    new_card_file = tk.PhotoImage(file=new_card_file)
                    card_list[index].configure(image=new_card_file)
                    card_list[index].Image = new_card_file
                    root.update_idletasks()

            #Display the hand ranking and associated score
            hand_score, hand_type = video_poker_functions.score_hand(PLAYERHAND)
            self.winning_hand.configure(text=hand_type)

            #Calculate and Display Winnings
            hand_winnings = video_poker_functions.calculate_payout(hand_score, self.bet_amount)
            self.Winnings.configure(text=hand_winnings)
            print(f'Player won ${hand_winnings}')

            #Provide playout to player balance and update player credit balance
            PLAYERMONEY = PLAYERMONEY + hand_winnings
            self.CurrentCredits.configure(text=PLAYERMONEY)

            #Update state to start new hand.
            self.Deal.configure(text='''New Hand''')
            self.status_deal_button = True

            #Resetting Holds
            self.CardHeld1.configure(background="#d9d9d9")
            self.CardHeld2.configure(background="#d9d9d9")
            self.CardHeld3.configure(background="#d9d9d9")
            self.CardHeld4.configure(background="#d9d9d9")
            self.CardHeld5.configure(background="#d9d9d9")
            Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold = (False,False,False,False,False)


    def Card1_command(self):
        '''Toggles holding or redrawing card 1'''
        print("command card one")
        global Card1Hold, PLAYERHAND
        print(PLAYERHAND[0])
        if self.status_deal_button is not True:
            if Card1Hold:
                Card1Hold = False
                self.CardHeld1.configure(background="#d9d9d9")
            elif Card1Hold is False:
                Card1Hold = True
                self.CardHeld1.configure(background="#ff0000")
        root.update_idletasks()

    def Card2_command(self):
        '''Toggles holding or redrawing card 2'''
        print("command card two")
        global Card2Hold, PLAYERHAND
        print(PLAYERHAND[1])
        if self.status_deal_button is not True:
            if Card2Hold:
                Card2Hold = False
                self.CardHeld2.configure(background="#d9d9d9")
            elif Card2Hold is False:
                Card2Hold = True
                self.CardHeld2.configure(background="#ff0000")
        root.update_idletasks()

    def Card3_command(self):
        '''Toggles holding or redrawing card 3'''
        print("command card three")
        global Card3Hold,PLAYERHAND
        print(PLAYERHAND[2])
        if self.status_deal_button is not True:
            if Card3Hold:
                Card3Hold = False
                self.CardHeld3.configure(background="#d9d9d9")
            elif Card3Hold is False:
                Card3Hold = True
                self.CardHeld3.configure(background="#ff0000")
        root.update_idletasks()

    def Card4_command(self):
        '''Toggles holding or redrawing card 4'''
        print("command card four")
        global Card4Hold,PLAYERHAND
        print(PLAYERHAND[3])
        if self.status_deal_button is not True:
            if Card4Hold:
                Card4Hold = False
                self.CardHeld4.configure(background="#d9d9d9")
            elif Card4Hold is False:
                Card4Hold = True
                self.CardHeld4.configure(background="#ff0000")
        root.update_idletasks()

    def Card5_command(self):
        '''Toggles holding or redrawing card 5'''
        print("command card one")
        global Card5Hold, PLAYERHAND
        print(PLAYERHAND[4])
        if self.status_deal_button is not True:
            if Card5Hold:
                Card5Hold = False
                self.CardHeld5.configure(background="#d9d9d9")
            elif Card5Hold is False:
                Card5Hold = True
                self.CardHeld5.configure(background="#ff0000")
        root.update_idletasks()


    def bet_max_command(self):
        '''Sets the bet to the maximum. Bet amount is 4 since we start at 0.'''
        print("Bet Max Button")
        self.bet_amount = 4
        self.Current_Bet.configure(text='''5''')


    def bet_one_command(self):
        '''Increments bet by one, starting at 0. Bet amount resets to 0 if incremented beyond 4.'''
        print("Bet One Button")

        if self.bet_amount == 4:
            self.bet_amount = 0
            self.Current_Bet.configure(text='''1''')
        else:
            self.bet_amount += 1
            self.Current_Bet.configure(text=self.bet_amount + 1)

    '''
    @staticmethod
    def popup1(event):
        ''' '''
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(
            activebackground="#ececec",
            activeborderwidth="1",
            activeforeground="#000000",
            background="#d9d9d9",
            borderwidth="1",
            disabledforeground="#a3a3a3",
            foreground="#000000"
        )
        Popupmenu1.post(event.x_root, event.y_root)
    '''

if __name__ == '__main__':
    '''Starts the GUI and begin the program.'''
    vp_start_gui()
