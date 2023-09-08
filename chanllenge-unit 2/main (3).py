# Define the Player class
class Player:
    # Define a method to play cricket
    def play(self):
        # Print a generic message
        print("The player is playing cricket.")

# Define the Batsman class as a subclass of Player
class Batsman(Player):
    # Override the play method
    def play(self):
        # Print a specific message
        print("The batsman is batting.")

# Define the Bowler class as a subclass of Player
class Bowler(Player):
    # Override the play method
    def play(self):
        # Print a specific message
        print("The bowler is bowling.")

# Create an object of the Batsman class
batsman = Batsman()

# Create an object of the Bowler class
bowler = Bowler()

# Call the play method for each object
batsman.play()
bowler.play()
