#!/usr/bin/env python3

def part1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines();
        win_points: int = 6;
        draw_points: int = 3;

        move_map: dict = {
            "A" : "Rock",
            "X" : "Rock",
            "B" : "Paper",
            "Y" : "Paper",
            "C" : "Scissors",
            "Z" : "Scissors"
        };

        scores: dict = {
            "Rock" : 1,
            "Paper" : 2,
            "Scissors" : 3
        };

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
            if (opp == me):
                adviced_score += draw_points;
            elif (battle_map[me] == opp):
                adviced_score += win_points;
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

        lose_map: dict = {
            "Rock" : "Scissors",
            "Scissors" : "Paper",
            "Paper" : "Rock"
        };

        win_map: dict = {
            "Scissors" : "Rock",
            "Paper" : "Scissors",
            "Rock" : "Paper"
        };

        score: int = 0;
        for line in lines:
            opp, me = line.strip().split(' ');
            opp = move_map[opp];

            if me == 'X':
                me = lose_map[opp]
                pass
            elif me == 'Y':
                me = opp
                score += draw_points;
            elif me == 'Z':
                me = win_map[opp];
                score += win_points;
            score += scores[me];

        print(score)

part2("input");
