import random

glow_green = "\033[42m"
glow_red = "\033[41m"
glow_yellow= "\033[43m"
glow_blue = "\033[44m"
glow_purple = "\033[45m"
glow_cyan = "\033[46m"
glow_orange = "\033[38;2;255;165;0m\033[7m"
glow_pink = "\033[38;2;255;105;180m\033[7m"
green = "\033[92m"
red = "\033[91m"
yellow= "\033[93m"
blue = "\033[94m"
purple = "\033[95m"
cyan = "\033[96m"
pink = "\033[38;2;255;105;180m"
orange = "\033[38;2;255;165;0m"
reset = "\033[0m"

ROCK = """
    ________
---|   _____)
      (______)
      (______)
      (_____)
---|__(_____)
"""

PAPER = """
    _______
---|   ____)____
          ______)
          _______)
         _______)
---|__________)
"""

SCISSORS = """
    _______
---|   ____)____
          ______)
       __________)
       (____)
---|___(____)
"""

MATCH = """
##    ##    ####    ########  ######  ##    ##
###  ###   ##  ##      ##    ##       ##    ##
########  ########     ##    ##       ########
## ## ##  ##    ##     ##    ##       ##    ##
##    ##  ##    ##     ##     ######  ##    ##
"""

DRAW = """
########   #######     ####    ##    ##
##     ##  ##    ##   ##  ##   ##    ##
##     ##  #######   ########  ## ## ##
##     ##  ##   ##   ##    ##  ###  ###
########   ##    ##  ##    ##  ##    ##
"""

USER_WON = """
##  ##   ####   ##  ##    ##   ##   ####   ##  ## 
##  ##  ##  ##  ##  ##    ##   ##  ##  ##  ### ## 
 ####   ##  ##  ##  ##    ## # ##  ##  ##  ###### 
  ##    ##  ##  ##  ##    #######  ##  ##  ## ### 
  ##     ####    ####      ## ##    ####   ##  ## 
"""

USER_LOSS = """
##  ##   ####   ##  ##     ##      ####    #####  ###### 
##  ##  ##  ##  ##  ##     ##     ##  ##  ##      ##     
 ####   ##  ##  ##  ##     ##     ##  ##   ####   ####   
  ##    ##  ##  ##  ##     ##     ##  ##      ##  ##     
  ##     ####    ####      ######  ####   #####   ###### 
"""

simple_help = """
- The following are the winning rules: Consider Human Player as the user and the computer as AI.
- If the user makes a paper gesture and AI selects Scissors then AI will win in that throw.
- If the user makes a rock gesture and AI selects Scissors then the user will win in that throw.
- If the user makes the exact gesture what AI selected then the that throw is a draw.
"""

winning_tricks = """
- Exploit the "Win-Stay, Lose-Shift" Rule

- The AI's Logic: AI knows that human winners usually repeat their winning move, 
  and human losers usually shift to the next option in the sequence (Rock ➔ Paper ➔ Scissors).

- The Counter: If you just won a round, do not throw that move again.
  Instead, switch to the move that beats your previous move. The AI will try to counter your expected repeat,
  playing right into your hands.
"""

randomness_help = """
- The Ultimate Weapon: Randomness

- The AI's Logic:
  The AI may try to recognize patterns in your behavior.

- The Counter:
  Use a random method to choose your move.
  For example:
  1-2 = Rock
  3-4 = Paper
  5-6 = Scissors

- If both players choose randomly and independently,
  each outcome has approximately a 33.3% probability:
  Player win = 33.3%
  Computer win = 33.3%
  Draw = 33.3%
"""

how_to_use_help = """
========================================
    HOW TO USE THE ZENITH GAME BOX
========================================

Welcome to Zenith Game Box! This app lets you play the classic Rock Paper Scissors game against a computer opponent right in your terminal.

----------------------------------------
1. STARTING THE APP
----------------------------------------
When you run the program, you will see a welcome banner. The app will then ask you a few questions to set up your session:

- Enter your name: Type your name using letters only (no numbers or symbols). If the name is invalid, you'll be asked again.
- Enter your age: Type your age as a whole number. Based on your age, the app assigns you an identity (Kid, Teenager, Young Man, Grown Man, Old Man, or Older Man).
- How many rounds do you want: Enter a positive whole number. This is how many rounds of Rock Paper Scissors you will play.
- Enter the id of game you want to play: Currently only one game is available. Type 1 to select Rock Paper Scissors.

After these questions, you will enter the main menu.

----------------------------------------
2. MAIN MENU OPTIONS
----------------------------------------
The main menu shows four options:

- Start: Begin playing Rock Paper Scissors.
- Help: Open the help center with guides and tricks.
- FeedBack: Give a rating or leave a message.
- Exit: Quit the app.

Type the name of the option you want (for example: start, help, feedback, exit, or quit). The app is not case-sensitive and will ignore extra spaces.

----------------------------------------
3. PLAYING THE GAME (START)
----------------------------------------
When you choose "start", the game screen appears. It shows your player information: name, age, identity, current round, remaining rounds, and scores (won, loss, draw).

You will then be prompted:
   "Enter rock, paper or scissor:"

Type one of these three words: rock, paper, or scissor. You may also type "scissors" and it will be accepted. If you type anything else, you'll see an error and be asked to try again.

After you make your choice, the computer randomly selects its move. The app then displays:
- The computer's choice (ASCII art)
- Your choice (ASCII art)
- The result: MATCH (if same), DRAW, USER_WON, or USER_LOSS

The scores are updated automatically.

The game continues until you have played the number of rounds you specified at the beginning. Once all rounds are finished, the app will tell you that your rounds are over and exit automatically.

----------------------------------------
4. ROCK PAPER SCISSORS RULES
----------------------------------------
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same, it's a draw.

The app's help center also provides this information and more advanced strategies.

----------------------------------------
5. HELP CENTER
----------------------------------------
If you choose "help" from the main menu, you'll see a help menu with these options:

   1. How to play – simple rules
   2. Tricks to win – advanced strategy using the "Win-Stay, Lose-Shift" rule
   3. How to use random moves – using randomness to be unpredictable
   4. How to use this app – this guide

Type the number of the help topic you want to see. The app will display the relevant information.

----------------------------------------
6. FEEDBACK
----------------------------------------
Choose "feedback" from the main menu to share your opinion.

You will see:
   1. Rate us – Give a star rating from 1 to 5. The app responds with a heart emoji based on your rating.
   2. Leave a message – Type a short note. The app will thank you based on the length of your message.

Follow the prompts and type the number of the method you want, then provide your rating or message.

----------------------------------------
7. EXITING
----------------------------------------
You can exit at any time from the main menu by typing "exit" or "quit". The app will display a goodbye message and close.

You can also stop the app at any prompt by pressing Ctrl+C. This will show an error message and exit safely.

----------------------------------------
8. TIPS
----------------------------------------
- Keep an eye on the scores displayed before each round.
- Use the help center's tricks to try to outsmart the computer, but remember the computer may not always follow predictable patterns.
- Have fun!

========================================
"""

won_rounds = 0
loss_rounds = 0
draw_rounds = 0

art = {
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}

all_choices = ["rock", "paper", "scissors"]

print(f"{glow_green}|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("========================= WELCOME TO THE ZENITH GAME BOX ==============================")
print(f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")

try:
    while True:
        try:
                user_name = str(input(f"{purple}[?] Enter your name: {blue}")).title().strip()
                temp_user_name = user_name
                if not user_name.replace(" ", "").isalpha():
                    print(f"{glow_red}ERROR:{reset}{red} Invalid name identity (Name only can contain letters and spaces){reset}\n\n")
                    continue
                if not user_name:
                    print(f"{glow_red}ERROR:{reset}{red} Invalid name identity (name cannot be empty){reset}\n\n")
                    continue
                break
        except Exception:
                print(f"{glow_red}ERROR:{reset}{red} Invalid name identity (name cannot be empty){reset}\n\n")
                continue

    while True:
        try:
                user_age = int(input(f"{purple}[?] Enter your age {user_name}: {blue}"))
                if user_age > 3 and user_age <= 12:
                    user_identity = "Kid"
                    break
                elif user_age <= 18 and user_age > 12:
                    user_identity = "Teenager"
                    break
                elif user_age > 18 and user_age <= 30:
                    user_identity = "Young Man"
                    break
                elif user_age > 30 and user_age <= 50:
                    user_identity = "Grown Man"
                    break
                elif user_age > 50 and user_age <= 75:
                    user_identity = "Old Man"
                    break
                elif user_age > 75 and user_age <= 100:
                    user_identity = "Older Man"
                    break
                else:
                    print(f"{glow_red}ERROR:{reset}{red} Invalid age identity{reset}\n\n")
                    continue
        except Exception:
                print(f"{glow_red}ERROR:{reset}{red} Invalid age identity{reset}\n\n")
                continue

    while True:
        try:
                rounds = int(input(f"{purple}[?] How many rounds do you want {user_name}: {blue}"))
                if rounds <= 0:
                    print(f"{glow_red}ERROR:{reset}{red} Unauthorized number{reset}\n\n")
                    continue
                break
        except Exception:
                print(f"{glow_red}ERROR:{reset}{red} Unauthorized number{reset}\n\n")
                continue

    print(f"\n\n\n{glow_cyan}Available Games ||| Zenith Game Box{reset}\n")
    print(f"{cyan}- rock paper scissor game | id: 1\n")

    while True:
        try:
            user_choice = int(input(f"{purple}[?] Enter the id of game you want to play: {blue}"))
            if user_choice == 1:
                break
            else:
                print(f"{glow_red}ERROR:{reset}{red} Unauthorized game id{reset}\n\n")
                continue
        except:
            print(f"{glow_red}ERROR:{reset}{red} Unauthorized game id{reset}\n\n")
            continue

    remaining_rounds = rounds
    current_round = 0

    while True:
        print(f"\n\n{glow_green}|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}")
        print(f"{glow_green}========================= WELCOME TO THE ROCK PAPER SCISSORS GAME ========================{reset}")
        print(f"{glow_green}|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")

        print(f"{glow_cyan}Options:{reset}\n")
        print(f"{cyan}- Start")
        print(f"{cyan}- Help")
        print(f"{cyan}- FeedBack")
        print(f"{cyan}- Exit")

        try:
            user_input = str(input(f"{purple}[?] Enter an option: {blue}")).lower().strip()
            if user_input not in ("start", "help", "feed back", "feedback", "exit", "quit"):
                print(f"{glow_red}ERROR:{reset}{red} Invalid option (please enter the name of option you want){reset}\n\n")
                continue
            if user_input == "feed back":
                user_input = "feedback"
                break
        except (KeyboardInterrupt, EOFError):
            print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
            exit(0)
        except Exception:
            print(f"{glow_red}ERROR:{reset}{red} Invalid option (please enter the name of option you want){reset}\n\n")
            continue

    # ====================================================================================================================== #
    # ======================================================= START ======================================================== #
    # ====================================================================================================================== #
        user_name = temp_user_name
        if user_input == 'start':
            print(f"\n\n{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}")
            print(f"{glow_green}========================= ROCK PAPER SCISSORS GAME STARTED ========================{reset}")
            print(f"{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")
            print(f"{glow_pink} User | Game -> Infomation{reset}")
            print(f"{orange}Player: {user_name}")
            print(f"Age: {user_age}")
            print(f"Identity: {user_identity}")
            print(f"Round: {current_round + 1}")
            print(f"Remaining Rounds: {remaining_rounds - 1}")
            print(f"Selected Game: {user_choice}")
            print(f"Won Rounds: {won_rounds}")
            print(f"Loss Rounds: {loss_rounds}")
            print(f"Draw Rounds: {draw_rounds}{reset}")

            while True:
                try:
                    user = str(input(f"\n\n{purple}[?] Enter rock, paper or scissor: {blue}")).lower().strip()
                    if user == "scissor":
                        user = "scissors"
                    if user not in ("rock", "paper", "scissors"):
                        print(f"{glow_red}ERROR:{reset}{red} Unauthorized input (please enter rock, paper or scissor){reset}\n\n")
                        continue
                    break
                except (KeyboardInterrupt, EOFError):
                    print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
                    exit(0)
                except Exception:
                    print(f"{glow_red}ERROR:{reset}{red} Unauthorized input{reset}\n\n")
                    continue

            current_round += 1
            remaining_rounds -= 1

            computer = random.choice(all_choices)

    # ====================================================================================================================== #
    # ======================================================= ROCK ========================================================= #
    # ====================================================================================================================== #

            if computer == "rock" and user == "rock":
                draw_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{ROCK}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{DRAW}{reset}")

            elif computer == "rock" and user == "paper":
                won_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{PAPER}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_WON}{reset}")

            elif computer == "rock" and user == "scissors":
                loss_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{SCISSORS}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_LOSS}{reset}")

            # ============================================================================================================== #
            # ================================================== PAPER ===================================================== #
            # ============================================================================================================== #

            if computer == "paper" and user == "paper":
                draw_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{PAPER}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{DRAW}{reset}")

            elif computer == "paper" and user == "scissors":
                won_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{SCISSORS}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_WON}{reset}")

            elif computer == "paper" and user == "rock":
                loss_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{ROCK}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_LOSS}{reset}")

            # ============================================================================================================== #
            # ================================================= SCISSORS =================================================== #
            # ============================================================================================================== #

            if computer == "scissors" and user == "scissors":
                draw_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{SCISSORS}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{DRAW}{reset}")

            elif computer == "scissors" and user == "rock":
                won_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{ROCK}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_WON}{reset}")

            elif computer == "scissors" and user == "paper":
                loss_rounds += 1
                print(f"\n\n{glow_yellow}computer choice: {reset}\n{yellow}{art[computer]}")
                print(f"{glow_yellow}your choice: {reset}\n{yellow}{PAPER}\n")
                print(f"{glow_yellow}{MATCH}")
                print(f"{glow_yellow}{USER_LOSS}{reset}")

            if rounds == current_round:
                print(f"\n\n{glow_red}Your rounds are over{reset}")
                print(f"{glow_red}If you want to play more, please run this code again!{reset}")
                print(f"{glow_red}Then make sure to enter the exact number of rounds you want!{reset}")
                exit(0)
            continue

    # ====================================================================================================================== #
    # ======================================================= HELP ========================================================= #
    # ====================================================================================================================== #
        elif user_input == "help":
            print(f"\n\n{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}")
            print(f"{glow_green}========================= ROCK PAPER SCISSORS GAME HELP ==========================={reset}")
            print(f"{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")
            print(f"{glow_pink}Our Help Center Options{reset}")
            print(f"{orange}How to play -> enter 1")
            print(f"Tricks to win -> enter 2")
            print(f"How to use random moves -> enter 3")
            print(f"How to use this app -> enter 4{reset}")

            while True:
                try:
                    wanted_help = int(input(f"\n\n{purple}[?] Choose a help from our help center (enter a number provided in the options for each help): {blue}").strip())
                    if wanted_help not in (1, 2, 3, 4):
                        print(f"{glow_red}ERROR:{reset}{red} Unauthorized input (please enter a one of the numbers provided by the help center){reset}\n\n")
                        continue
                    break
                except (KeyboardInterrupt, EOFError):
                    print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
                    exit(0)
                except Exception:
                    print(f"{glow_red}ERROR:{reset}{red} Invalid option (please enter the number of option you want){reset}\n\n")
                    continue

            if wanted_help == 1:
                print(f"\n{glow_yellow}{simple_help}{reset}")

            elif wanted_help == 2:
                print(f"\n{glow_yellow}{winning_tricks}{reset}")

            elif wanted_help == 3:
                print(f"\n{glow_yellow}{randomness_help}{reset}")

            elif wanted_help == 4:
                print(f"\n{glow_yellow}{how_to_use_help}{reset}")
            continue

    # ====================================================================================================================== #
    # ======================================================= FEEBACK ====================================================== #
    # ====================================================================================================================== #
        elif user_input == "feedback":
            print(f"{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")
            print(f"{glow_green}========================= ROCK PAPER SCISSORS GAME FEEDBACK ======================{reset}")
            print(f"{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")
            print(f"{glow_pink}Our FeedBack Center Options{reset}")
            print(f"{orange}Rate us -> enter 1")
            print(f"Leave a message -> enter 2{reset}")

            while True:
                try:
                    wanted_feedback = int(input(f"\n\n{purple}[?] Choose a feedback method from our feedback center (enter a number provided in the options for each method): {blue}").strip())
                    if wanted_feedback not in (1, 2):
                        print(f"{glow_red}ERROR:{reset}{red} Unauthorized feedback method{reset}\n\n")
                        continue
                    break
                except (KeyboardInterrupt, EOFError):
                    print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
                    exit(0)
                except Exception:
                    print(f"{glow_red}ERROR:{reset}{red} Please enter a number{reset}\n\n")
                    continue
            
    # ============================================================================================================== #
    # ================================================== RATING ==================================================== #
    # ============================================================================================================== #
            if wanted_feedback == 1:
                while True:
                    try:
                        rate = int(input(f"\n\n{purple}[?]⭐⭐⭐⭐⭐ Rate us out of 5: {blue}").strip())
                        if not 1 <= rate <= 5:
                            print(f"{glow_red}ERROR:{reset}{red} Rating must be between 1 and 5.{reset}\n\n")
                            continue
                        break
                    except (KeyboardInterrupt, EOFError):
                        print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
                        exit(0)
                    except Exception:
                        print(f"{glow_red}ERROR:{reset}{red} Unauthorized feedback{reset}\n\n")
                        continue

                if rate > 3:
                    print(f"{glow_orange}❤️❤️❤️ Thank you for your feedback: ❤️❤️❤️{reset}")
                elif rate == 3:
                    print(f"{glow_orange}❤️‍🩹❤️‍🩹❤️‍🩹 Thank you for your feedback: ❤️‍🩹❤️‍🩹❤️‍🩹{reset}")
                else:
                    print(f"{glow_orange}💔💔💔 Thank you for our feedback: 💔💔💔{reset}")

    # ============================================================================================================== #
    # ================================================== MESSAGE =================================================== #
    # ============================================================================================================== #
            elif wanted_feedback == 2:
                while True:
                    try:
                        message = str(input(f"\n\n{purple}[?] Leave a small note: {blue}")).strip().lower()
                        if not message:
                            print(f"{glow_red}ERROR:{reset}{red} Feedback cannot be empty{reset}\n\n")
                            continue
                        if message.isdigit():
                            print(f"{glow_red}ERROR:{reset}{red} Unauthorized feedback{reset}\n\n")
                            continue
                        break
                    except (KeyboardInterrupt, EOFError):
                        print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}\n\n")
                        exit(0)
                    except Exception:
                        print(f"{glow_red}ERROR:{reset}{red} Unauthorized feedback{reset}\n\n")
                        continue

                if len(message) >= 10:
                    print(f"\n\n{glow_orange}❤️❤️❤️ Thank you for your feedback: ❤️❤️❤️{reset}")
                elif len(message) > 5:
                    print(f"{glow_orange}❤️‍🩹❤️‍🩹❤️‍🩹 Thank you for your feedback: ❤️‍🩹❤️‍🩹❤️‍🩹{reset}")
                else:
                    print(f"{glow_orange}💔💔💔 Thank you for your feedback: 💔💔💔{reset}")
            continue

    # ============================================================================================================== #
    # ==================================================== EXIT ==================================================== #
    # ============================================================================================================== #
        elif user_input in ("exit", "quit"):
                print(f"\n\n{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}")
                print(f"{glow_green}========================= ROCK PAPER SCISSORS GAME EXIT ==========================={reset}")
                print(f"{glow_green}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{reset}\n\n")
                print(f"{glow_green}🚀🚀🚀 Thank you for using our Zenith Game Box! 🚀🚀🚀{reset}")
                print(f"{glow_green}🚀🚀🚀 Come Back Later 🚀🚀🚀. . .{reset}")
                exit(0)

except KeyboardInterrupt:
    print(f"{glow_red}ERROR:{reset}{red} App was stopped by user!{reset}")
    exit(0)