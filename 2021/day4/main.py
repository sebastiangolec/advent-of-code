'''--- Day 4: Giant Squid ---'''
import bingo

input = open("2021/day4/input", 'r').readlines()
winner = bingo.Bingo(input.copy())
loser = bingo.Bingo(input.copy())

print(winner.playToWin())
print(loser.playToLose())