#!/usr/bin/env python
import random


def randWord(wordFile):
	with open(wordFile) as f:
		return random.choice(f.read().splitlines())


def generateCodeName():
	return randWord('data/adj.txt') + ' ' + randWord('data/noun.txt')


if __name__ == '__main__':
	print generateCodeName()

