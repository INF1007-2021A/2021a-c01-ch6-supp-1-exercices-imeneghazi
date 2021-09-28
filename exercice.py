#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	max_liste = []
	for i in range(len(numbers)):
		max_liste.append(max(numbers[i]))
	return max_liste

def join_integers(numbers):
	nombre = ""
	for i in range(len(numbers)):
		nombre += str(numbers[i])
	return int(nombre)

def generate_prime_numbers(limit):
	premiers = []
	nombres = []
	j = 0
	for i in range(2, limit+1):
		nombres.append(i)
	while nombres is not []:
		is_prime = True
		for d in range(2, nombres[j]//2):
			if nombres[j] % d == 0:
				is_prime = False
				break
		if is_prime:
			premiers.append(nombres[j])
		j += 1
		if j == len(nombres):
			break
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	Liste = []
	nombre_combi = []
	for k in range(1, num_combinations+1):
		nombre_combi.append(k)
	if excluded_multiples == None:
		for i in range(num_combinations):
			for j in range(len(strings)):
				Liste.append(strings[j]+str(nombre_combi[i]))
	else:
		for i in range(1, num_combinations+1):
			for j in range(len(strings)):
				if i % excluded_multiples != 0:
					Liste.append(strings[j]+str(nombre_combi[i-1]))
	return Liste

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
