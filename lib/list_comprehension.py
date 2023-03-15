#!/usr/bin/env python3

def return_evens(num_list):
    num_list2 = [n for n in num_list if n % 2 == 0]
    return num_list2

def make_exclamation(sentence_list):
    sentence_list2 = [str + "!" for str in sentence_list]
    return sentence_list2
