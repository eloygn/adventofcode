#!/usr/bin/env python3
cadena = list()

with open('input_08.txt') as f:
    cadena = f.read().splitlines()

#cadena.append("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe")
#cadena.append("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc")
#cadena.append("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg")
#cadena.append("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb")
#cadena.append("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea")
#cadena.append("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb")
#cadena.append("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe")
#cadena.append("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef")    
#cadena.append("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb")
#cadena.append("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce")

def count_dif_caract(cadena):
    s = set(cadena)
    return(len(s))

suma = 0

for i in cadena:
    subcadena = i.split("| ")
    subcadenanueva = list(subcadena[1].split(' '))
    for j in subcadenanueva:
        if (count_dif_caract(j) == 2 or count_dif_caract(j) == 3 or count_dif_caract(j) == 4 or count_dif_caract(j) == 7):
            suma = suma + 1
print(suma)
