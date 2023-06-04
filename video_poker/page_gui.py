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
CARD_HOLDS = []

#Variables for buttons deciding whether a card is held or redrawn.
Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold = False, False, False, False, False

#Variables deciding whether hand is in deal or redraw phase
dealCardButton = True
drawCardButton = False
previousHand = None

#Get the current directory and default the bet amount to 0.
local_file_directory = os.path.dirname(os.path.realpath(__file__))
asset_file_directory = os.path.join(local_file_directory + '\Assets')
BET_AMOUNT = 0

def load_player_balance() -> int:
    ''''''
    bankStorePath = os.path.join(local_file_directory, 'bank.txt' )
    bankStore = open(bankStorePath, 'r', encoding = 'utf-8')
    #bankStore.close()
    #playerMoney = bankStore.read()
    return int(bankStore.read())
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


w = None
def create_credits(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_credits(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
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


class Credits:
    ''' '''
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        Top is the toplevel containing window.
        All other window objects are initialized and defined here.
        '''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85' was d9d9d9
        _fgcolor = '#000000'  # X11 color: 'black'

        #This Section controls the game window name and color
        top.geometry("1920x1061")
        top.minsize(1024, 768)
        top.maxsize(1920, 1080)
        top.resizable(1,  1)
        top.title("5 Card Draw")
        top.configure(background="#00008b")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        #global card image
        default_cardback_image = os.path.join(asset_file_directory + '\cardBack.png')
        default_cardback_image = tk.PhotoImage(file=default_cardback_image)

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
            image=default_cardback_image,
            pady="0",
            command=self.Card1_command,
            text='''Button'''
        )
        self.Card1.Image = default_cardback_image

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
            image=default_cardback_image,
            pady="0",
            command=self.Card2_command,
            text='''Button'''
        )
        self.Card2.Image = default_cardback_image

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
            image=default_cardback_image,
            pady="0",
            command=self.Card3_command,
            text='''Button'''
        )
        self.Card3.Image = default_cardback_image

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
            image=default_cardback_image,
            pady="0",
            command=self.Card4_command,
            text='''Button'''
        )
        self.Card4.Image = default_cardback_image

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
            image=default_cardback_image,
            pady="0",
            command=self.Card5_command,
            text='''Button'''
        )
        self.Card5.Image = default_cardback_image

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
        bannerFile = os.path.join(asset_file_directory + '\BackgroundImage3.png')
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
            command=self.bet_one_button
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
            command=self.bet_max_button
        )

        #initialize the current bet display
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
            command=self.Deal_command
        )

        #Initialize winning Hand banner in top center
        self.Winning_Hand = tk.Message(top)
        self.Winning_Hand.place(relx=0.325, rely=0.300, relheight=0.053, relwidth=0.300)
        self.Winning_Hand.config(font=("Courier", 44))
        self.Winning_Hand.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="Red",
            text='''Hand Rank''',
            width=500
        )

        #Intial update of images into client
        root.update_idletasks()

    def Deal_command(self):
        '''Fucntion/Button alternating between redrawing cards or starting a new hand, and starting scoring.'''
        global PLAYERMONEY, dealCardButton, drawCardButton, previousHand, Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold, CARD_HOLDS

        #If it is time to start a new hand, this function runs.
        if dealCardButton:
            print("command deal")
            global PLAYERHAND, previousHand, DECK
            PLAYERHAND, DECK = video_poker_functions.create_hand(DECK)
            self.Winning_Hand.configure(text='')
            self.Winnings.configure(text='')

            #Subract Bet Amount from player money to play.
            PLAYERMONEY = PLAYERMONEY - (BET_AMOUNT + 1)
            self.CurrentCredits.configure(text=PLAYERMONEY)

            #Updating the image of all cards in hand
            newCard1File = (os.path.join(asset_file_directory, PLAYERHAND[0] )) + '.png'
            newCard2File = (os.path.join(asset_file_directory, PLAYERHAND[1] )) + '.png'
            newCard3File = (os.path.join(asset_file_directory, PLAYERHAND[2] )) + '.png'
            newCard4File = (os.path.join(asset_file_directory, PLAYERHAND[3] )) + '.png'
            newCard5File = (os.path.join(asset_file_directory, PLAYERHAND[4] )) + '.png'
            newCard1Image = tk.PhotoImage(file=newCard1File)
            newCard2Image = tk.PhotoImage(file=newCard2File)
            newCard3Image = tk.PhotoImage(file=newCard3File)
            newCard4Image = tk.PhotoImage(file=newCard4File)
            newCard5Image = tk.PhotoImage(file=newCard5File)
            self.Card1.configure(image=newCard1Image)
            self.Card2.configure(image=newCard2Image)
            self.Card3.configure(image=newCard3Image)
            self.Card4.configure(image=newCard4Image)
            self.Card5.configure(image=newCard5Image)
            self.Card1.Image = newCard1Image
            self.Card2.Image = newCard2Image
            self.Card3.Image = newCard3Image
            self.Card4.Image = newCard4Image
            self.Card5.Image = newCard5Image

            #RefreshInstance (Updates display)
            root.update_idletasks()

            #change the redraw / new hand button to redraw
            dealCardButton = False
            drawCardButton = True
            self.Deal.configure(text='''Redraw''')

        #If it is the second part of the hand, this function runs.
        elif drawCardButton:

            #change the redraw / new hand button to New Hand
            print("command redraw")
            self.Deal.configure(text='''New Hand''')
            dealCardButton = True
            drawCardButton = False

            if Card1Hold is False or 'card_1_hold' not in CARD_HOLDS:
                newCard1, DECK = video_poker_functions.draw_cards(DECK, 1)
                newCard1 = ''.join(newCard1)
                PLAYERHAND[0] = newCard1
                newCard1File = (os.path.join(asset_file_directory, newCard1 )) + '.png'
                newCard1Image = tk.PhotoImage(file=newCard1File)
                self.Card1.configure(image=newCard1Image)
                self.Card1.Image = newCard1Image
                root.update_idletasks()

            if Card2Hold is False or 'card_2_hold' not in CARD_HOLDS:
                newCard2, DECK = video_poker_functions.draw_cards(DECK, 1)
                newCard2 = ''.join(newCard2)
                PLAYERHAND[1] = newCard2
                newCard2File = (os.path.join(asset_file_directory, newCard2 )) + '.png'
                newCard2Image = tk.PhotoImage(file=newCard2File)
                self.Card2.configure(image=newCard2Image)
                self.Card2.Image = newCard2Image
                root.update_idletasks()

            if Card3Hold is False or 'card_3_hold' not in CARD_HOLDS:
                newCard3, DECK = video_poker_functions.draw_cards(DECK, 1)
                newCard3 = ''.join(newCard3)
                PLAYERHAND[2] = newCard3
                newCard3File = (os.path.join(asset_file_directory, newCard3 )) + '.png'
                newCard3Image = tk.PhotoImage(file=newCard3File)
                self.Card3.configure(image=newCard3Image)
                self.Card3.Image = newCard3Image
                root.update_idletasks()

            if Card4Hold is False or 'card_4_hold' not in CARD_HOLDS:
                newCard4, DECK = video_poker_functions.draw_cards(DECK, 1)
                newCard4 = ''.join(newCard4)
                PLAYERHAND[3] = newCard4
                newCard4File = (os.path.join(asset_file_directory, newCard4 )) + '.png'
                newCard4Image = tk.PhotoImage(file=newCard4File)
                self.Card4.configure(image=newCard4Image)
                self.Card4.Image = newCard4Image
                root.update_idletasks()

            if Card5Hold is False or 'card_5_hold' not in CARD_HOLDS:
                #Draw Card
                newCard5, DECK = video_poker_functions.draw_cards(DECK, 1)
                newCard5 = ''.join(newCard5)
                #Update card into hand
                PLAYERHAND[4] = newCard5
                newCard5File = (os.path.join(asset_file_directory, newCard5 )) + '.png'
                newCard5Image = tk.PhotoImage(file=newCard5File)
                self.Card5.configure(image=newCard5Image)
                self.Card5.Image = newCard5Image
                root.update_idletasks()

            print(PLAYERHAND)

            #Need to add a comment here describing what this logic is doing.
            previousHand = True
            if previousHand is not None:
                hand_type = ''
                CurrentHandScore, hand_type = video_poker_functions.score_hand(PLAYERHAND)
                self.Winning_Hand.configure(text=hand_type)

                #Calculate and Display Winnings
                handWinnings = video_poker_functions.calculate_payout(CurrentHandScore, BET_AMOUNT)
                self.Winnings.configure(text=handWinnings)

                #Calculate, provide, and update payout
                PLAYERMONEY = PLAYERMONEY + handWinnings
                self.CurrentCredits.configure(text=PLAYERMONEY)
                previousHand = None

        #Resetting Holds
        self.CardHeld1.configure(background="#d9d9d9")
        self.CardHeld2.configure(background="#d9d9d9")
        self.CardHeld3.configure(background="#d9d9d9")
        self.CardHeld4.configure(background="#d9d9d9")
        self.CardHeld5.configure(background="#d9d9d9")
        Card1Hold, Card2Hold, Card3Hold, Card4Hold, Card5Hold = (False, False, False, False, False)
        CARD_HOLDS = []

    def Card1_command(self):
        '''Toggles holding or redrawing card 1'''
        print("command card one")
        global Card1Hold, PLAYERHAND
        print(PLAYERHAND[0])
        if dealCardButton is not True:
            if Card1Hold:
                Card1Hold = False
                self.CardHeld1.configure(background="#d9d9d9")
            else:
                Card1Hold = True
                self.CardHeld1.configure(background="#ff0000")
        root.update_idletasks()

    def Card2_command(self):
        '''Toggles holding or redrawing card 2'''
        print("command card two")
        global Card2Hold, PLAYERHAND
        print(PLAYERHAND[1])
        if dealCardButton is not True:
            if Card2Hold:
                Card2Hold = False
                self.CardHeld2.configure(background="#d9d9d9")
            else:
                Card2Hold = True
                self.CardHeld2.configure(background="#ff0000")
        root.update_idletasks()

    def Card3_command(self):
        '''Toggles holding or redrawing card 3'''
        print("command card three")
        global Card3Hold,PLAYERHAND
        print(PLAYERHAND[2])
        if dealCardButton is not True:
            if Card3Hold:
                Card3Hold = False
                self.CardHeld3.configure(background="#d9d9d9")
            else:
                Card3Hold = True
                self.CardHeld3.configure(background="#ff0000")
        root.update_idletasks()

    def Card4_command(self):
        '''Toggles holding or redrawing card 4'''
        print("command card four")
        global Card4Hold,PLAYERHAND
        print(PLAYERHAND[3])
        if dealCardButton != True:
            if Card4Hold:
                Card4Hold = False
                self.CardHeld4.configure(background="#d9d9d9")
            else:
                Card4Hold = True
                self.CardHeld4.configure(background="#ff0000")
        root.update_idletasks()

    def Card5_command(self):
        '''Toggles holding or redrawing card 5'''
        print("command card one")
        global Card5Hold, PLAYERHAND
        print(PLAYERHAND[4])
        if dealCardButton is not True:
            if Card5Hold:
                Card5Hold = False
                self.CardHeld5.configure(background="#d9d9d9")
            else:
                Card5Hold = True
                self.CardHeld5.configure(background="#ff0000")
        root.update_idletasks()


    def bet_max_button(self):
        '''Sets the bet to the maximum. Bet amount is 4 since we start at 0.'''
        global BET_AMOUNT
        print("Bet Max Button")
        BET_AMOUNT = 4
        self.Current_Bet.configure(text='''5''')


    def bet_one_button(self):
        '''Increments bet by one, starting at 0. Bet amount resets to 0 if incremented beyond 4.'''
        global BET_AMOUNT
        print("Bet One Button")

        if BET_AMOUNT == 4:
            BET_AMOUNT = 0
            self.Current_Bet.configure(text='''1''')
        else:
            BET_AMOUNT += 1
            self.Current_Bet.configure(text=BET_AMOUNT + 1)


    @staticmethod
    def popup1(event):
        ''' '''
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    '''Starts the GUI and begin the program.'''
    vp_start_gui()
    bankStore = open('bank.txt', 'w')
    PLAYERMONEY = str(PLAYERMONEY)
    bankStore.write(PLAYERMONEY)
    bankStore.close()
