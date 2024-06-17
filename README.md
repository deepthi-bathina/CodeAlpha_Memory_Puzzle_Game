# CodeAlpha_Memory_Puzzle_Game

A memory puzzle game is a card game where the objective is to find pairs of matching cards.Here is the summary of my code:-

Step - 1: Initialization
      The game initializes with a 4x4 grid of cards (16 cards, 8 pairs).
      A timer is set to count down from 60 seconds.
Step - 2: Image Loading
      Images for the cards are loaded from a folder named images.
      Images are resized to fit the buttons, and a hidden image is used for the back of the cards.
Step - 3: Board Creation
      The board is created with shuffled pairs of images.
      Buttons are placed in a grid layout and display the hidden image initially.
Step - 4: Card Click Handling
      When a card is clicked, it reveals the image.
      If two cards are clicked, they are checked for a match after a short delay.
Step - 5: Match Checking
      If the two revealed cards match, they remain revealed.
      If they do not match, they are flipped back to the hidden state.
Step - 6: Game Win Condition
      The game tracks the number of matches found.
      When all pairs are matched, a "You Win!" message is displayed, and the timer stops.
Step - 7: Timer Functionality
      The timer updates every second.
      If the time runs out before all pairs are matched, the game displays "Time's up!" and disables all buttons.
Step - 8: Event Loop
      The game runs in a continuous loop, handling user input and updating the display until the game is won or time runs out.
