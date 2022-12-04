#!/usr/bin/env python3

def part1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines();
        win_points: int = 6;
        draw_points: int = 3;

        # map of what move opponent and we are playing
        move_map: dict = {
            "A" : "Rock",
            "X" : "Rock",
            "B" : "Paper",
            "Y" : "Paper",
            "C" : "Scissors",
            "Z" : "Scissors"
        };

        # scores for hand sign
        scores: dict = {
            "Rock" : 1,
            "Paper" : 2,
            "Scissors" : 3
        };

        # what beats what
        battle_map: dict = {
            "Rock" : "Scissors",
            "Scissors" : "Paper",
            "Paper" : "Rock"
        };

        adviced_score: int = 0;
        for line in lines:
            opp, me = line.strip().split(' ');
            opp = move_map[opp];
            me = move_map[me];

            # draw
            if (opp == me):
                adviced_score += draw_points;
            # win
            elif (battle_map[me] == opp):
                adviced_score += win_points;
            # this will be added always
            adviced_score += scores[me];
        print(adviced_score)



def part2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines();
        win_points: int = 6;
        draw_points: int = 3;

        move_map: dict = {
            "A" : "Rock",
            "B" : "Paper",
            "C" : "Scissors",
        };

        scores: dict = {
            "Rock" : 1,
            "Paper" : 2,
            "Scissors" : 3
        };

        # opp-move : move we need to lose
        lose_map: dict = {
            "Rock" : "Scissors",
            "Scissors" : "Paper",
            "Paper" : "Rock"
        };

        # opp-move : move we need to win
        win_map: dict = {
            "Scissors" : "Rock",
            "Paper" : "Scissors",
            "Rock" : "Paper"
        };

        score: int = 0;
        for line in lines:
            opp, me = line.strip().split(' ');
            opp = move_map[opp];

            # lose if X
            if me == 'X':
                me = lose_map[opp]
                pass
            # draw if Y
            elif me == 'Y':
                me = opp
                score += draw_points;
            # win if Z
            elif me == 'Z':
                me = win_map[opp];
                score += win_points;
            # add anyways
            score += scores[me];

        print(score)

part2("input");
