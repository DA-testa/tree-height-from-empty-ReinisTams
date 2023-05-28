# python3

import sys
import threading
import numpy

#importē nepieciešamās bibliotēkas

def compute_height(n, parents):
    #Šī funkcija aprēķina koka augstumu, ņemot vērā mezglu skaitu (n) un katram mezglam pievienoto vecāko mezglu (parents).
    #Tā atgriež maksimālo koka augstumu.

    heights = [0] * n
    #Izveido sarakstu ar nosaukumu 'heights', kurā ir nulle katram mezglam, lai turētu katra mezgla augstumu.

    def calculate_height(node):
        #Šī iekšējā funkcija rekursīvi aprēķina dotā mezgla augstumu koka struktūrā.

        if heights[node] != 0:
            #Ja mezgla augstums jau ir aprēķināts, atgriež saglabāto vērtību.
            return heights[node]

        parent = parents[node]
        #Iegūst dotā mezgla parent mezglu.

        if parent == -1:
            #Ja "parent" ir -1, tas nozīmē, ka dotais mezgls ir koka sakne.
            heights[node] = 1
            #Iestata saknes mezgla augstumu uz 1.
        else:
            #Ja parent nav -1, tad aprēķina augstumu.
            heights[node] = calculate_height(parent) + 1
            #Dotā mezgla augstums = parent augstums + 1.

        return heights[node]
        #Atgriež aprēķināto mezgla augstumu.

    max_height = 0
    #Inicializē maksimālā augstuma mainīgo ar 0.

    for node in range(n):
        height = calculate_height(node)
        #Aprēķina dotā mezgla augstumu, izmantojot calculate_height funkciju.
        max_height = max(max_height, height)
        #Atjaunina maksimālo augstumu, ja pašreizējais augstums ir lielāks par iepriekšējo maksimālo augstumu.

    return max_height
    #Atgriež koka maksimālo augstumu.

#Lasa ievadi
n = int(input())
#Lasīt mezglu skaitu no ievades.
parents = list(map(int, input().split()))
#Lasīt katram mezglam pievienoto parent mezglu no ievades un pārvērš to par veselo skaitu sarakstu.

print(compute_height(n, parents))
#Izsauc compute_height funkciju, padodot tai ievades vērtības, un izdrukā koka maksimālo augstumu.

