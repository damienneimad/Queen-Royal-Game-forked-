import wikipedia


# Jonas
def get_user_names(player_count):
    greet = "Hello"
    players = []

    # +1 starts the player counter at 1, not 0
    for player in range(1, player_count + 1):
        players.append(input(f"Player {player}: "))

        # create two string variables, salutation with the value
        # Ibrahim
        name = players[player - 1]
        new_string = f"{greet} {name}!"
        print(new_string)

    return players


# Vasanthy
def find_queen():
    return wikipedia.search("Elizabeth II")


# Damien
# Retrieve 5 random Wikipedia articles
def wikipedia_random_search(number):
    rand_wiki = wikipedia.random(5)
    return rand_wiki


# Vasanthy
def get_initial_random_articles():
    number_of_initial_articles = 5
    initial_random_articles = wikipedia_random_search(
        number_of_initial_articles)

    # Display the random articles and their indices, Vasanthy
    print("\nYou will begin your search at one of the following places:")
    print("")

    for index, title in enumerate(initial_random_articles, start=1):
        print(f"{index}. {title}")

    print("")
    return initial_random_articles


# Vasanthy
def is_queen_article(player_article, queen_title):
    if player_article == queen_title:
        return True
    else:
        print("\nWe are getting closer for sure, but we have not found her yet! Where to go next?.")
        return False


# Damian
# create a function that gives the next search
def wikipedia_next_link(title):
    page = wikipedia.page(title)
    links = page.links
    print(f"Links from '{title}':")

    for link in range(0, len(links)):
        print(f"{link + 1}. {links[link]}")

    return links, page


# Jonas
def track_and_print_route(list_of_articles):
    print("She got lost on this way:")

    article_number = 0

    for article in list_of_articles:
        article_number += 1
        print(f"{article_number}. {article}")


def while_answer_wrong_loop(player_article, list_of_articles, link_counter, queen_article_title):
    links, player_article = wikipedia_next_link(player_article)
    link_counter += 1
    # print(f"Counter of Links: {link_counter}")

    new_player_guess = int(input(
        "Enter the number of the article you think leads to the Queen of England: ")) - 1
    player_article = links[new_player_guess]
    list_of_articles.append(player_article)
    queen_status = is_queen_article(player_article, queen_article_title)

    return queen_status, link_counter, list_of_articles, player_article


def game():
    # Defines the final destination
    queen_article = find_queen()
    queen_article_title = queen_article[0]

    # Starts the game, Vasanthy
    random_articles = get_initial_random_articles()

    # gets initial player guess
    player_guess = int(input(
        "Enter the number of the article you think leads to the Queen of England: ")) - 1
    player_article = random_articles[player_guess]

    print("")
    queen_status = is_queen_article(player_article, queen_article_title)

    list_of_articles = [player_article]
    link_counter = 0

    # This loop takes a lot of input but also gets a lot of tuples as an output, it overrides
    # itself with all the new values until true
    while not queen_status:
        queen_status, link_counter, list_of_articles, player_article = (
            while_answer_wrong_loop(player_article, list_of_articles,
                                    link_counter, queen_article_title))

    print("\nCongratulations! You found the Queen of England, Her Royal Highness Queen Elizabeth II!")

    articles = list_of_articles

    return articles


def main():
    # Introduction, gets the player Information
    player_count = int(input("\nHow many players try to rescue the queen?: "))
    print(f"\n{player_count} Hero(s) start the search! Their names are: ")

    get_user_names(player_count)

    # Gets Play Mode (Single Player, MultiplayerVS, Multiplayer Team)

    articles = game()

    track_and_print_route(articles)


if __name__ == '__main__':
    main()
