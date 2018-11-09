#1.Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Алгоритм взят с задания урока№3

def few_values(n1,n2) :
    bitAnd = n1 & n2
    bitOr = n1 | n2
    bitLeft2Difits = n1 << 2
    bitRight2Difits = n1 >> 2 
    string_output = 'Bit AND between 5 and 6 is '+str(bitAnd)
    string_output+= '. Bit OR between 5 and 6 is '+str(bitOr)
    string_output+= '. Bit shift left for 2 digits for 5 is '+str(bitLeft2Difits)
    string_output+= '. Bit shift right for 2 digits for 5 is '+str(bitRight2Difits) 
    return string_output

s=few_values(5, 6) 
print(s)

#Сложность этого алгоритма метода few_values - O(1) константа и не зависит от величин n1 и n2, передаваемых в качестве параметров.
#Алгоритм довольно прост, поэтому нескольких реализаций алгоритма не просматривается