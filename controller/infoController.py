from model.model import add_movie,list_movies,find_title,find_director,find_genre

#movies = []
START = "\nEnter 'a' to add a movie, \n 'l' to see your movies, \n 'f' to find a movie by title, \n 'd' to find a movie by director,\n 'g' to find a movie by genre, \n or 'q' to quit: "


user_selection = {
    'a': add_movie,
    'l': list_movies,
    'f': find_title,
    'd': find_director,
    'g': find_genre
}

def menu():
    selection = input(START).lower()
    while selection != 'q':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')



if __name__ == '__main__':
    menu()
