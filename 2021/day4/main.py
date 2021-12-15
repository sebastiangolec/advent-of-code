'''--- Day 4: Giant Squid ---'''
import bingo

bingo = bingo.Bingo(open("2021/day4/input", 'r').readlines())
print(bingo.playToWin())
print(bingo.playToLose())