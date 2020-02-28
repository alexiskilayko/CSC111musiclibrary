# ------------------------------------------------------
#        Name: Alexis Kilayko (I did not collaborate
#              with anyone on this assignment)
#    Filename: musiclibrary.py
#        Date: 18 October 2018
# Description: This is a Python program that creates a
#              music library interface.
# ------------------------------------------------------

# Defining function that prints welcome interface.
def welcomeInterface():
    print("""
     _    _   _    _    ____   _    _____
    | \  / | | |  | |  /  __| | |  /  _  |
    |  \/  | | |  | | |  /_   | | |  / \_|
    |      | | |  | |  \_  \  | | | |
    | |\/| | | |  | |    \  \ | | | |   _
    | |  | | |  \/  |  __/  / | | |  \_/ |
    |_|  |_|  \____/  |____/  |_|  \_____|   
     _        _   ____    ____     ___    ____  __     __
    | |      | | |    \  |    \   /   \  |    \ \ \   / /
    | |      | | |     | |     | |     | |     | \ \_/ /
    | |      | | |    /  |   _/  |  _  | |   _/   \   /
    | |      | | |    \  |   \   | | | | |   \     | |
    | |____  | | |     | | |\ \  | | | | | |\ \    | |
    |______| |_| |____/  |_| \_\ |_| |_| |_| \_\   |_|

    """)
    

# Defining function that takes user input and responds accordingly.
def userOperation():

    # Define empty playlist list.
    playlist = []

    # Define list of user operations.
    listOperations = "ADD", "REMOVE", "PRINT", "PLAY", "QUIT"

    # Ask user for input.
    userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
    print("")
    
    # While-loop for user operations.
    while userSelect != "QUIT":

        # User chooses add operation.
        if userSelect == "ADD":
            song = {} # Defining empty dictionary to be filled with sing info.
            # dictionary[key] = value
            song["Title"] = input("Song Title: ") 
            song["Artist"] = input("Artist: ")
            song["Album"] = input("Album: ")
            song["URL"] = input("Spotify URL: ")
            
            playlist.append(song) # Append dictionary of each song to playlist list.

            # Ask again for input.
            print("")
            userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
            print("")

        # User chooses remove operation.
        if userSelect == "REMOVE":
            numRemove = eval(input("Which # would you like to remove? ")) # Evals user input.
            del playlist[numRemove-1] # Deletes selected song by index.
            print("Song #" + str(numRemove), "removed.") # Prints message.

            # Ask again for input.
            print("")
            userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
            print("")

        # User chooses print operation.
        c = 1 # Declaring counter.
        if userSelect == "PRINT":
            # For-loop printing each song (and its info) in the playlist list.
            for song in playlist:
                print(str(c) + ".", # number of song in playlist
                      "'" + song["Title"] + "'", # song name
                      "by", song["Artist"], # song artist
                      "(" + song["Album"] + ")") # song album
                c += 1 # Adds 1 to counter for next song in playlist.

            # Ask again for input.
            print("")
            userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
            print("")

        # User chooses play operation.
        if userSelect == "PLAY":
            numPlay = eval(input("Which # would you like to play? ")) # Evals user input.
            songPlay = playlist[numPlay-1] # Assigns dictionary of selected song to new object songPlay.
            songURL = songPlay["URL"] # Assigns URL value from song dictionary to new object songURL.
            # ----- BEGIN CITED CODE (1) ----- 
            sleep(2) # Waits 2 seconds before opening URL.
            webbrowser.open(songURL)
            # ----- END CITED CODE (1) -----

            # Ask again for input.
            print("")
            userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
            print("")
        
        # User enters in unsupported function.
        if userSelect not in listOperations:
            print("Unsupported function. Please try again.") # Prints error message.

            # Ask again for input.
            print("")
            userSelect = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
            print("")

    # User chooses to quit.
    if userSelect == "QUIT":
        print("")
        print("Thanks for listening!")


# Defining main function.
def main():

    # Import modules.
    # ----- BEGIN CITED CODE (1) -----
    import webbrowser
    from time import sleep
    # ----- END CITED CODE (1) -----

    # Call functions.
    welcomeInterface()    
    userOperation()
    
# Call main function if not file is not imported.
if __name__ == "__main__":
    main()


# ------------------------------------------------------
# RESOURCES:
# (1) code by R. Jordan Crouser, CSC111 Lab 6: YouTube Playlist
# (2) consulted Caitlin Ong, my shinyuu
