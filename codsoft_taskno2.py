import tkinter as tk
from tkinter import messagebox

def play():
        print("Lets Play rock, paper and scissors")
        user=int(input("Choose rock(0), paper(1), scissors(2):"))
        print(user)
        import random
        computer=random.randint(0,2)
        print("computer's choice: ", computer)
        if user==computer:
            print("Its a draw")
        elif user==0 and computer==2:
            print("You win")
        elif user==1 and computer==2:
            print("You Lose")
        elif user==2 and computer==0:
            print("You Lose")
        elif user>=3:
            print("Invalid!! Try again")
        elif user<computer:
            print("You Lose")
        elif user>computer:
            print("You win")
        else:
            print("Bye Bye")
        play_again=messagebox.askyesno("Play Again","Do you want to play again?")
        if play_again:
            play()
        else:
            window.destroy

def show_rules():
    rules = (
        "Rules of Rock-Paper-Scissors:\n"
        "1. Rock beats Scissors.\n"
        "2. Scissors beats Paper.\n"
        "3. Paper beats Rock.\n"
        "4. If both players choose the same, it's a draw."
    )
    messagebox.showinfo("Game Rules", rules)

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")

welcome_label = tk.Label(window, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 14))
welcome_label.pack(pady=10)

rules_button = tk.Button(window, text="Show Rules", command=show_rules)
rules_button.pack(pady=5)


play_button = tk.Button(window, text="Play", command=play)
play_button.pack(pady=10)


exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=10)

window.mainloop()
