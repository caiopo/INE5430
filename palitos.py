#! /usr/bin/env python3

from random import randint
from getpass import getpass
from argparse import ArgumentParser

DEFAULT_PICKS = 3
MAX_PLAYERS = 5


def vprint(*args, **kwargs):
    if getattr(vprint, 'verbose'):
        print(*args, **kwargs)


class GameFinished(Exception):
    pass


class Player:
    def __init__(self, name, picks):
        self.name = name
        self.picks = picks
        self.hand = None

    def remove_pick(self):
        if self.picks > 1:
            self.picks -= 1
        else:
            raise GameFinished()

    def __str__(self):
        return '<{}: name={}, picks={}>'.format(
            self.__class__.__name__, self.name, self.picks)

    def __repr__(self):
        return self.name


class ArtificialPlayer(Player):
    def choose_hand(self):
        self.hand = randint(0, self.picks)

    def guess(self, total_picks, guesses, player_picks):
        return randint(self.picks, total_picks)

class PoorBot(Player):
    def choose_hand(self):
        self.hand = randint(0, self.picks)

    def guess(self, total_picks, guesses, player_picks):
        if guesses == []:
            return randint(self.picks, (total_picks-(self.picks-self.hand)))
        else:
            others_players_hands = []
            for i, j in enumerate(guesses):
                hand = round((j*player_picks[i])/total_picks)

                others_players_hands.append(hand)

            #test print  
            print(others_players_hands)

            #needs improvement to the outter possibilities, such as one player
            #hand 3 and the bot hand 0
            a = self.hand+sum([h for h in others_players_hands])
            b = total_picks - ((self.picks-self.hand) + 
                               (sum(p for p in player_picks) - 
                                sum(h for h in others_players_hands)))

            #quick fix
            if b < total_picks:
                b += 1

            if a > self.hand:
                a -=1

            while True:
                guess = randint(a, b)
                if guess not in guesses:
                    return guess
                else:
                    if a > 0:
                        a -= 1
                    if b < total_picks:
                        b += 1


class HumanPlayer(Player):
    def choose_hand(self):
        print('Player {}: choose your hand'.format(self.name))

        try:
            hand = int(input('Hand: '))
        except ValueError:
            print('Input is not a number')
            self.choose_hand()
            return

        if 0 <= hand <= self.picks:
            self.hand = hand

        else:
            print('Input must be between 0 and the number of '
                  'picks you have.')

            if input('Show your number of picks [Y/n] ') != 'n':
                print(self.picks)

            self.choose_hand()

    def guess(self, total_picks, guesses, player_picks):
        print('Player {}: make your guess (between 0 and {})'.format(
            self.name, total_picks))
        if guesses:
            print('The number must not be one of the following: {}'.format(
                sorted(guesses)))

        try:
            guess = int(input('Guess: '))
        except ValueError:
            print('Input is not a number')
            return self.guess(total_picks, guesses)

        if not (0 <= guess <= total_picks):
            print('Guess must be between 0 and {}'.format(total_picks))
            return self.guess(total_picks, guesses)

        if guess in guesses:
            print('This number is already taken'.format(total_picks))
            return self.guess(total_picks, guesses)

        return guess


class Match:
    def __init__(self, players, number):
        self.players = players
        self.number = number

    def setup(self):
        for player in self.players:
            player.choose_hand()

        self.total_picks = sum([p.picks for p in players])
        self.response = sum([p.hand for p in players])
        self.players_picks = []
        self.guesses = []

        vprint('\nMatch #{}: total_picks={}, response={}\n\tplayers={}'.format(
            self.number, self.total_picks, self.response, self.players))

    def run(self):
        for player in self.players:
            guess = player.guess(self.total_picks, self.guesses, 
                                 self.players_picks)

            self.guesses.append(guess)
            self.players_picks.append(player.picks)

            vprint('Player {} guessed {}'.format(player.name, guess))

            if guess == self.response:
                vprint('Player {} guessed correctly!'.format(
                    player.name, guess))

                return player

        vprint('No one guessed!')


class Game:
    def __init__(self, players):
        self.players = players

    def run(self):
        nmatches = 0

        while True:
            match = Match(self.players, nmatches)

            nmatches += 1

            match.setup()

            winner = match.run()

            if winner is not None:
                try:
                    winner.remove_pick()
                except GameFinished:
                    return winner

                self.players.remove(winner)

                self.players.insert(0, winner)


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Play the brazilian popular game "Porrinha"')

    parser.add_argument('-a', '--ai', type=int, default=None, metavar='N',
                        help=('set the number of AI players '
                              '(default: 5 - (n of humans))'))

    parser.add_argument('-p', '--picks', type=int, default=3, metavar='P',
                        help='set initial number of picks (default: 3)')

    parser.add_argument('--human', action='store', type=str, metavar='NAME',
                        nargs='+', default=[], help='add human players')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='raises level of verbose')

    args = parser.parse_args()

    setattr(vprint, 'verbose', args.verbose)

    picks = args.picks
    humans = args.human

    if args.ai is None:
        ais = list(range(MAX_PLAYERS - len(humans)-1))
    else:
        ais = list(range(args.ai-1))

    if (len(humans) + len(ais)) > MAX_PLAYERS:
        print('error: maximum number of players is {}'.format(MAX_PLAYERS))
        exit()

    players = ([HumanPlayer(name, picks) for name in humans] +
               [ArtificialPlayer('AI_{}'.format(name), picks) for name in ais] +
               [PoorBot('PoorBot', picks)])

    game = Game(players)

    print([(p.name, p.picks, p.hand) for p in players])

    print(game.run())

    print([(p.name, p.picks, p.hand) for p in players])
