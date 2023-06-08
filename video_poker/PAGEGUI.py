'''Module ran to start the program, Poker: 5 Card Redraw'''
import sys
import os.path

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

import video_poker
import video_poker_functions

local_file_directory = os.path.dirname(os.path.realpath(__file__))
asset_file_directory = os.path.join(local_file_directory + '\Assets')

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Credits (root)
    video_poker.init(root, top)
    root.mainloop()


class Credits:
    '''Class containing the GUI interface.'''
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.
        All other window objects are initialized and defined here.
        '''
        #Initializing runtime values
        self.bet_amount = 0
        self.status_deal_button = True #Start state as "new hand"
        self.card_hold_status = [False, False, False, False, False] #cards start unheld.
        self.player_hand = []
        self.deck = []
        self.player_money = video_poker_functions.load_player_balance()

        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'

        #This Section controls the game window name and color
        top.geometry("1920x1060")
        top.minsize(120, 1)
        top.maxsize(1920, 1080)
        top.resizable(1,  1)
        top.title("5 Card Draw")
        top.configure(
            background="#00008b",
            highlightbackground="#d9d9d9",
            highlightcolor="black"
        )

        #global card image
        default_card_back_file = os.path.join(asset_file_directory + '\cardBack.png')
        default_card_back_file = tk.PhotoImage(file=default_card_back_file)

        #Initialize the bottom center display the number of winnings
        self.player_winnings_display = tk.Message(top)
        self.player_winnings_display.place(relx=0.026, rely=0.877, relheight=0.093, relwidth=0.178)
        self.player_winnings_display.config(font=("Courier", 44))
        self.player_winnings_display.configure(
            background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Winnings''',
            width=342
        )

        #Initialize display for current credits
        self.player_credits = tk.Message(top)
        self.player_credits.place(relx=0.771, rely=0.877, relheight=0.094, relwidth=0.178)
        self.player_credits.config(font=("Courier", 55))
        self.player_credits.configure(background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text=self.player_money,
            width=341
        )

        #Initialize the banner image at the top
        self.banner = tk.Button(top)
        self.banner.place(relx=0.015, rely=0.019, height=300, width=1800)
        banner_image = os.path.join(asset_file_directory + '\BackgroundImage.png')
        banner_image = tk.PhotoImage(file=banner_image)
        self.banner.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=banner_image,
            pady="0",
            text='''Button'''
        )
        self.banner.image = banner_image

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        #Initialize the 1 through 5 "hold" toggle displays
        self.hold_button_1 = tk.Message(top)
        self.hold_button_1.place(relx=0.096, rely=0.358, relheight=0.024, relwidth=0.026)
        self.hold_button_2 = tk.Message(top)
        self.hold_button_2.place(relx=0.276, rely=0.358, relheight=0.024, relwidth=0.026)
        self.hold_button_3 = tk.Message(top)
        self.hold_button_3.place(relx=0.464, rely=0.358, relheight=0.025, relwidth=0.026)
        self.hold_button_4 = tk.Message(top)
        self.hold_button_4.place(relx=0.651, rely=0.358, relheight=0.025, relwidth=0.026)
        self.hold_button_5 = tk.Message(top)
        self.hold_button_5.place(relx=0.849, rely=0.358, relheight=0.025, relwidth=0.026)

        hold_objects = [self.hold_button_1, self.hold_button_2, self.hold_button_3, self.hold_button_4, self.hold_button_5]
        for index, hold_object in enumerate(hold_objects):
            hold_object.configure(
            background="#d9d9d9",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''Held'''
        )
            hold_object.Image = default_card_back_file

        #Intialize card 1 through 5, left to right
        self.card_one = tk.Button(top)
        self.card_one.place(relx=0.016, rely=0.386, height=508, width=350)
        self.card_two = tk.Button(top)
        self.card_two.place(relx=0.203, rely=0.386, height=508, width=350)
        self.card_three = tk.Button(top)
        self.card_three.place(relx=0.391, rely=0.386, height=508, width=350)
        self.card_four = tk.Button(top)
        self.card_four.place(relx=0.578, rely=0.386, height=508, width=350)
        self.card_five = tk.Button(top)
        self.card_five.place(relx=0.766, rely=0.386, height=508, width=350)

        card_objects = [self.card_one, self.card_two, self.card_three, self.card_four, self.card_five]
        for index, card_object in enumerate(card_objects):
            card_object.configure(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            disabledforeground="#a3a3a3",
            foreground="#000000",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            image=default_card_back_file,
            pady="0",
            command=lambda card_count = index + 1: self.toggle_card_hold(card_count),
            text='''Button'''
        )
            card_object.Image = default_card_back_file

        #Initialize the bet_one button
        self.bet_one_button = tk.Button(top)
        self.bet_one_button.place(relx=0.214, rely=0.877, height=90, width=150)
        self.bet_one_button.config(font=("Courier", 22))
        self.bet_one_button.configure(
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
        self.bet_max_button = tk.Button(top)
        self.bet_max_button.place(relx=0.297, rely=0.877, height=90, width=140)
        self.bet_max_button.config(font=("Courier", 22))
        self.bet_max_button.configure(
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
        self.current_bet = tk.Message(top)
        self.current_bet.place(relx=0.391, rely=0.877, relheight=0.09, relwidth=0.178)
        self.current_bet.config(font=("Courier Bold", 100))
        self.current_bet.configure(
            background="#00008b",
            foreground="#cc3300",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            text='''1''',
            width=342
        )

        #initialize the deal and redraw button
        self.deal_button = tk.Button(top)
        self.deal_button.place(relx=0.604, rely=0.877, height=90, width=300)
        self.deal_button.config(font=("Courier", 44))
        self.deal_button.configure(
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
        print(f' Player Hand: {self.player_hand}')

        #This list is used to update the card images for both redrawing and starting new hands.
        card_list = [self.card_one, self.card_two, self.card_three, self.card_four, self.card_five]

        if self.status_deal_button:
            print("Starting New Hand")
            #Creating player hand and clearing previous winning hand rank and winnings.
            self.player_hand, self.deck = video_poker_functions.create_hand(self.deck)
            self.winning_hand.configure(text='')
            self.player_winnings_display.configure(text='')

            #Subract Bet Amount
            self.player_money = self.player_money - (self.bet_amount + 1)
            self.player_credits.configure(text=self.player_money)

            #Updating the image of all cards in hand
            for index, card in enumerate(self.player_hand):
                new_card_file = (os.path.join(asset_file_directory, card)) + '.png'
                new_card_image = tk.PhotoImage(file = new_card_file)
                card_list[index].configure(image = new_card_image)
                card_list[index].image = new_card_image

            #change the redraw / new hand button to redraw
            self.status_deal_button = False
            self.deal_button.configure(text='''Redraw''')
            root.update_idletasks()

        else:
            #This phase redraws cards and immediately scores the redrawn cards.
            print("Redrawing unheld cards")

            #Drawing new cards for each held card and updating their images.
            for index, card_hold_status in enumerate(self.card_hold_status):
                if card_hold_status is False:
                    new_card, self.deck = video_poker_functions.draw_cards(self.deck, 1)
                    new_card = ''.join(new_card)
                    self.player_hand[index] = new_card
                    new_card_file = os.path.join(asset_file_directory, new_card) + '.png'
                    new_card_file = tk.PhotoImage(file=new_card_file)
                    card_list[index].configure(image=new_card_file)
                    card_list[index].Image = new_card_file
                    root.update_idletasks()

            #Display the hand ranking and associated score
            hand_score, hand_type = video_poker_functions.score_hand(self.player_hand)
            self.winning_hand.configure(text=hand_type)

            #Calculate and Display Winnings
            hand_winnings = video_poker_functions.calculate_payout(hand_score, self.bet_amount)
            self.player_winnings_display.configure(text=hand_winnings)
            print(f'Player won ${hand_winnings}')

            #Provide playout to player balance and update player credit balance
            self.player_money = self.player_money + hand_winnings
            self.player_credits.configure(text=self.player_money)

            #Update state to start new hand.
            self.deal_button.configure(text='''New Hand''')
            self.status_deal_button = True

            #Resetting Holds displays and back end values
            hold_buttons = [self.hold_button_1, self.hold_button_2, self.hold_button_3, self.hold_button_4, self.hold_button_5]
            for hold_button in hold_buttons:
                hold_button.configure(background="#d9d9d9")
            self.card_hold_status = [False,False,False,False,False]


    def toggle_card_hold(self, card: int) -> None:
        '''Toggles the hold or redrawing of a card in hand.'''
        hold_buttons = [self.hold_button_1, self.hold_button_2, self.hold_button_3, self.hold_button_4, self.hold_button_5]

        #If card is held, then toggle to false or vice versa. Update UI visual to match.
        if self.status_deal_button is not True:
            if self.card_hold_status[card-1]:
                self.card_hold_status[card-1] = False
                hold_buttons[card-1].configure(background="#d9d9d9")
            else:
                self.card_hold_status[card-1] = True
                hold_buttons[card-1].configure(background="#ff0000")
        root.update_idletasks()


    def bet_max_command(self):
        '''Sets the bet to the maximum. Bet amount is 4 since we start at 0.'''
        print("Bet Max Button")

        #Disallow changing bet mid hand by checking status_deal_button
        if self.status_deal_button:
            self.bet_amount = 4
            self.current_bet.configure(text='''5''')
        root.update_idletasks()


    def bet_one_command(self):
        '''Increments bet by one, starting at 0. Bet amount resets to 0 if incremented beyond 4.'''
        print("Bet One Button")

        #Disallow changing bet mid hand by checking status_deal_button
        if self.status_deal_button:
            if self.bet_amount == 4:
                self.bet_amount = 0
                self.current_bet.configure(text='''1''')
            else:
                self.bet_amount += 1
                self.current_bet.configure(text=self.bet_amount + 1)
        root.update_idletasks()


if __name__ == '__main__':
    '''Starts the GUI and begin the program.'''
    vp_start_gui()
