# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:56:05 2020

@author: prath
"""

input = open("input2.txt", "r")
passwords = []
for row in input:
    passwords.append(row.split())
input.close();

valid_pass_count = 0

for password_rule  in passwords:
    min_count = int(password_rule[0].split('-')[0])
    max_count = int(password_rule[0].split('-')[1])
    letter = password_rule[1][0]
    pass_phrase = password_rule[2]
    
    if pass_phrase.count(letter) >= min_count and pass_phrase.count(letter) <= max_count:
        valid_pass_count = valid_pass_count + 1
        

print("Number of valid passwords: " + str(valid_pass_count))
       
valid_pass_count = 0 

for password_rule  in passwords:
    pos_a = int(password_rule[0].split('-')[0])
    pos_b = int(password_rule[0].split('-')[1])
    letter = password_rule[1][0]
    pass_phrase = password_rule[2]
    if (pass_phrase[pos_a - 1] == letter):
        if (pass_phrase[pos_b - 1] != letter):
            valid_pass_count = valid_pass_count + 1
    else:
        if (pass_phrase[pos_b - 1] == letter):
            valid_pass_count = valid_pass_count + 1
        
print("Number of valid passwords: " + str(valid_pass_count))