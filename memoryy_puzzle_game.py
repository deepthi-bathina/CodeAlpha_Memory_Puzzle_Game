import tkinter as tk
import random
from itertools import product
from PIL import Image, ImageTk

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        
        self.rows = 4
        self.columns = 4
        self.num_pairs = (self.rows * self.columns) // 2
        self.time_limit = 60
        self.flipped_cards = []
        self.matches_found = 0
        self.start_time = None
        self.game_won = False
        self.buttons = []
        self.values = []
        self.images = []
        self.hidden_image = None
        self.timer_label = tk.Label(root, text=f"Time: {self.time_limit}")
        self.timer_label.grid(row=0, column=0, columnspan=self.columns)
        
        self.load_images()
        self.create_board()
        self.root.after(1000, self.update_timer)

    def load_images(self):
        # Load images and resize them to fit on the buttons
        for i in range(1, self.num_pairs + 1):
            image = Image.open(f'images\{i}.png')  # Assuming images are named 1.png, 2.png, etc.
            image = image.resize((80, 80), Image.ANTIALIAS)
            self.images.append(ImageTk.PhotoImage(image))
        
        # Create a hidden image for the back of the cards
        hidden_image = Image.open('images/hidden.png')  # Image for the back of the cards
        hidden_image = hidden_image.resize((80, 80), Image.ANTIALIAS)
        self.hidden_image = ImageTk.PhotoImage(hidden_image)

    def create_board(self):
        self.values = list(range(self.num_pairs)) * 2
        random.shuffle(self.values)
        
        for i, (r, c) in enumerate(product(range(1, self.rows + 1), range(self.columns))):
            btn = tk.Button(self.root, image=self.hidden_image, command=lambda i=i: self.on_card_click(i))
            btn.grid(row=r, column=c)
            self.buttons.append(btn)
        
    def on_card_click(self, index):
        if len(self.flipped_cards) == 2 or index in self.flipped_cards:
            return

        btn = self.buttons[index]
        btn.config(image=self.images[self.values[index]], state='disabled')
        self.flipped_cards.append(index)
        
        if len(self.flipped_cards) == 2:
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        first, second = self.flipped_cards
        if self.values[first] == self.values[second]:
            self.matches_found += 1
            if self.matches_found == self.num_pairs:
                self.game_won = True
                self.timer_label.config(text="You Win!")
        else:
            for idx in self.flipped_cards:
                self.buttons[idx].config(image=self.hidden_image, state='normal')
        self.flipped_cards = []
    
    def update_timer(self):
        if self.game_won:
            return

        if self.start_time is None:
            self.start_time = self.time_limit
        else:
            self.start_time -= 1

        if self.start_time <= 0:
            self.timer_label.config(text="Time's up!")
            for btn in self.buttons:
                btn.config(state='disabled')
        else:
            self.timer_label.config(text=f"Time: {self.start_time}")
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()

