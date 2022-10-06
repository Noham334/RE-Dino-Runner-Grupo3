from dino_runner.components.game import Game


if __name__ == "__main__":
    game = Game()
    death_count = 0
    while game.running:
        if game.restart:
            death_count = death_count + 1
        if not game.playing:
            game.show_menu(death_count)
            #death_count = death_count + 1
