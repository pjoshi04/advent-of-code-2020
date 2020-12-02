# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:41:29 2020

@author: prath
"""

input = open("input1.txt", "r")
input_array = []
for row in input:
    input_array.append(int(row))
input.close();


for i in input_array:
    for j in input_array:
        if i + j == 2020:
            print("Answer: " + str(i*j))
            break;
    else:
        continue; 
    break;
    

for i in input_array:
    for j in input_array:
        for k in input_array:
            if i + j + k == 2020:
                print("Answer: " + str(i*j*k))
                break;
        else:
            continue; 
        break;
    else:
        continue; 
    break;