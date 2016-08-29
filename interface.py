from game import Game


def main():
    game = Game()
    game.create_new_board()
    while True:
        game.display()
        print()
        command = input("{}'s move, Q to quit: ".format(game.determine_player))
        if command == 'Q':
            break
        validated = game.validate(command)
        if validated:
            game.rotate()



if __name__ == "__main__":
    main()