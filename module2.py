a=[int(b) for b in input("Введіть елементи масиву через пробіл:").split()]
print("Масив:")
print(a)

#1
def sort(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range (len(a)-1):
            if  a[i]> a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

sort(a)
print("Відсортирований масив:", a)

#2
h  = int(input("Введіть елемент для пошуку за значенням:"))
def poshuk1(a, h):
    for i in a:
        if a.index(i) == h:
           return  a[h]
print("Елемент за цим індексом:",poshuk1(a,h))

#3
k  = int(input("Введіть елемент для пошуку за індексом"))
def poshuk(a, k):
    for i in a:
        if i == k:
           return  a.index(i)
print("індекс цього елементу:", poshuk(a,k))

#4
add = a
def minimal(a, add):
    sort(a)
    return add[:5] 
print("5 перших мінімальних", minimal(a, add))

#5
add = a
def maximal(a, add):
    sort(a)
    a.reverse()
    return add[:5] 
print("5 перших максимальних", maximal(a, add))

#6
def ser(a):
    return (sum(a)/len(a))
print("Середнє значення елементів масиву:", ser(a))

#7
def povern(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
print("Масив без повторюваних елементів", povern(a))