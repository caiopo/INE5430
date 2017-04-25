#! /usr/bin/env python3

from random import randint, shuffle
from argparse import ArgumentParser

DEFAULT_PICKS = 3
MAX_PLAYERS = 5


def vprint(*args, **kwargs):
    if getattr(vprint, 'verbose'):
        print(*args, **kwargs):


class GameFinished(Exception):
    pass


class Player:
    def __init__(self, name, picks):
        self.name = name
        self.picks = picks
        self.hand = None

    def remove_pick(self):
        self.picks -= 1

        if self.picks == 0:
            raise GameFinished()

    def __str__(self):
        return '<{}: name={}, picks={}>'.format(
            self.__class__.__name__, self.name, self.picks)

    def __repr__(self):
        return self.name


class RandomPlayer(Player):
    def __init__(self, number, picks):
        super().__init__('Random_{}'.format(number), picks)

    def choose_hand(self):
        self.hand = randint(0, self.picks)

    def guess(self, total_picks, guesses, player_picks):
        while True:
            g = randint(self.hand, total_picks - (self.picks - self.hand))

            if g not in guesses:
                return g


class ArtificialPlayer(Player):
    def __init__(self, number, picks):
        super().__init__('AI_{}'.format(number), picks)

    def choose_hand(self):
        self.hand = randint(0, self.picks)

        def guess(self, total_picks, guesses, player_picks):
        others_players_hands = []
        for i, j in enumerate(guesses):
            hand = ((j * player_picks[i]) / total_picks)

            others_players_hands.append(hand)

        guess = self.hand + sum(others_players_hands) + (
                sum([x/2 for x in player_picks[(len(guesses)+1):]]))

        guess = round(guess)
        a = guess
        b = guess

        while True:

            if guess not in guesses:
                return guess

            else:

                if a > 0:
                    a -= 1
                if b < total_picks:
                    b += 1

                guess = randint(a, b)
                

class HumanPlayer(Player):
    def choose_hand(self):
        print('Player {}: choose your hand (between 0 and {})'.format(
            self.name, self.picks))

        try:
            hand = int(input('Hand: '))
        except ValueError:
            print('Input is not a number')
            self.choose_hand()
            return

        if 0 <= hand <= self.picks:
            self.hand = hand
        else:
            self.choose_hand()

    def guess(self, total_picks, guesses, player_picks):
        print('Player {}: make your guess (between 0 and {})'.format(
            self.name, total_picks))

        if guesses:
            print('The number must not be one of the following:', guesses)

        try:
            guess = int(input('Guess: '))
        except ValueError:
            print('Input is not a number')
            return self.guess(total_picks, guesses, player_picks)

        if not (0 <= guess <= total_picks):
            print('Guess must be between 0 and {}'.format(total_picks))
            return self.guess(total_picks, guesses, player_picks)

        if guess in guesses:
            print('This number is already taken'.format(total_picks))
            return self.guess(total_picks, guesses, player_picks)

        return guess


class Match:
    def __init__(self, players, number):
        self.players = players
        self.number = number

    def setup(self):
        for player in self.players:
            player.choose_hand()

        self.total_picks = sum([p.picks for p in self.players])
        self.response = sum([p.hand for p in self.players])
        self.players_picks = [p.picks for p in self.players]
        self.guesses = []

        vprint('\nMatch #{}: total_picks={}, response={}\n\tplayers={}'.format(
            self.number, self.total_picks, self.response, self.players))

    def run(self):
        for player in self.players:
            guess = player.guess(self.total_picks, tuple(self.guesses),
                                 tuple(self.players_picks))

            self.guesses.append(guess)

            vprint('Player {} guessed {}'.format(player.name, guess))

            if guess == self.response:
                vprint('Player {} guessed correctly!'.format(
                    player.name, guess))

                return player

        vprint('No one guessed!')


class Game:
    def __init__(self, players):
        shuffle(players)

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

                index = self.players.index(winner)

                self.players = self.players[index:] + self.players[:index]


def simulate(n_ai, n_random, iterations, picks=DEFAULT_PICKS):
    from collections import defaultdict

    winners = defaultdict(int)

    for _ in range(iterations):
        players = ([ArtificialPlayer(n, picks) for n in range(n_ai)] +
                   [RandomPlayer(n, picks) for n in range(n_random)])

        game = Game(players)

        winner = game.run()

        winners[winner.name] += 1

    sorted_ranking = sorted(winners.items(), key=lambda x: x[1], reverse=True)

    for name, points in sorted_ranking:
        print('{}: {}'.format(name, points))


def main():
    parser = ArgumentParser(
        description='Play the brazilian popular game "Porrinha"',
        add_help=False)

    parser.add_argument('--help', action='store_true',
                        help='show this help message and exit')

    parser.add_argument('-a', '--ai', type=int, metavar='N', default=0,
                        help='set the number of AI players (default: 0)')

    parser.add_argument('-r', '--random', type=int, default=0, metavar='N',
                        help=('set the number of random players '
                              '(default: 0)'))

    parser.add_argument('-p', '--picks', type=int, default=3, metavar='P',
                        help='set initial number of picks (default: 3)')

    parser.add_argument('-h', '--human', action='store', type=str,
                        metavar='NAME', nargs='+', default=[],
                        help='add human players')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='raises level of verbose')

    parser.add_argument('-s', '--simulate', type=int, metavar='N',
                        help='simulate N games. can\'t be used with "-h"')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        exit()

    setattr(vprint, 'verbose', args.verbose)

    picks = args.picks

    humans = args.human
    ais = list(range(args.ai))
    randoms = list(range(args.random))

    if (len(humans) + len(ais) + len(randoms)) > MAX_PLAYERS:
        parser.error('maximum number of players is {}'.format(
            MAX_PLAYERS))

    if (len(humans) + len(ais) + len(randoms)) < 2:
        parser.error('minimum number of players is 2')

    players = (
        [HumanPlayer(name, picks) for name in humans] +
        [ArtificialPlayer(n, picks) for n in ais] +
        [RandomPlayer(n, picks) for n in randoms]
    )

    if args.simulate is not None:
        if humans != []:
            parser.error('can\'t use -s and --human together')

        simulate(args.ai, args.random, args.simulate, picks)

    else:
        print('Players:', players)

        game = Game(players)

        winner = game.run()

        print('Winner:', winner.name)


if __name__ == '__main__':
    main()
