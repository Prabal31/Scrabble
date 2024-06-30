letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Handle both uppercase and lowercase letters
letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points.update({letter.lower(): point for letter, point in zip(letters, points)})

letter_to_points[""] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

brownie_points = score_word("BROWNIE")
print(f"Points for 'BROWNIE': {brownie_points}")

player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}
player_to_points = {}

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]
    update_point_totals()  # Update points whenever a word is played

# Initial update of point totals
update_point_totals()

# Add new words and update points
play_word('player1', 'PYTHON')
play_word('newPlayer', 'scrabble')

print("Player to Words:", player_to_words)
print("Player to Points:", player_to_points)
