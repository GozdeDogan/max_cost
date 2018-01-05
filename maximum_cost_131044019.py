################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 5
# Question 1
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# find_maximum_cost metodunun karmasikligi best ve worst case'de linear time'dir.
# Tasarlanan algoritmanin karmasikligi da best ve worst case'de linear time
# O(n) olarak bulunur.
#
################################################################################

import sys

def main():
    Y = [14,1,14,1,14]
    #print "\nlen(Y):", len(Y), "Y:", Y
    cost = find_maximum_cost(Y)
    #print "cost:", cost, "\n"
    print(cost)
    
    Y = [1,9,11,7,3]
    #print "\nlen(Y):", len(Y), "Y:", Y
    cost = find_maximum_cost(Y)
    #print "cost:", cost, "\n"
    print(cost)
    
    Y = [50,28,1,1,13,7]
    #print "\nlen(Y):", len(Y), "Y:", Y
    cost = find_maximum_cost(Y)
    #print "cost:", cost, "\n"
    print(cost)
    
    Y = [80, 22, 45, 11, 67, 67, 74, 91, 4, 35, 34, 65, 80, 21, 95, 1, 52, 25, 31, 2, 53]
    #print "\nlen(Y):", len(Y), "Y:", Y
    cost = find_maximum_cost(Y)
    #print "cost:", cost, "\n"
    print(cost)
    
    Y = [79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91]
    #print "\nlen(Y):", len(Y), "Y:", Y
    cost = find_maximum_cost(Y)
    #print "cost:", cost, "\n"
    print(cost)


################################################################################
#
# ilk elamanin ne olacagina Y arrayinin 1. ve 2. elamanina bakilarak karar verildi.
# Geri kalan elemanlara Y arrayinin i. indexsindeki eleman ile X arrayinin
# (i-1). indexindeki elemanin farkinin, X arrayinin (i-1). indexindeki eleman ile 
# 1'in farkindan buyuk olup olmamasi karsilastirildi.
# Eger Y arrayinin i. indexsindeki eleman ile X arrayinin (i-1). indexindeki 
# elemanin farki buyukse X'in i. indexine Y[i] elemani eklenir. 
# Buyuk degilse X'in i. indexine 1 elemani eklenir.
# Boylece max cost bulunmus olur.
# 
# Y arrayinin eleman sayisi n olarak kabul edilsin. 
# while dongusu best case'de de worst case'de de n-1 kadar doner.
# Metodun karmasikligi best case'de de worst case'de de linear time dir.
# complexity = O(n) olur.
#
################################################################################
def find_maximum_cost(Y):
    X = []

    if Y[0] <= 1:
        X.append(1)
    else:
        if abs(Y[1] - Y[0]) >= abs(Y[0] - 1):
            X.append(Y[0])
        else:
            X.append(1)

    for i in range(1, len(Y)):
        if Y[i] <= 1:
            X.append(1)
        else:
            #print "X[i-1]:", X[i-1], "Y[i]:", Y[i]
            if abs(Y[i] - X[i-1]) >= abs(X[i-1] - 1):
                X.append(Y[i])
            else:
                X.append(1) 

    
    #print "len(X):", len(X), "X:", X
    cost = 0

    for i in range(1, len(X)):
        cost = cost + abs(X[i] - X[i-1])

    return cost        
                    

if __name__ == "__main__":
    main() 
    
