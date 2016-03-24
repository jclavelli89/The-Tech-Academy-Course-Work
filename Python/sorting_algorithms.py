# Bubblesort
'''
def bubblesort(alist):
    for passnum in range(len(alist) -1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [67, 45, 2, 13, 1, 998]
bubblesort(alist)
print(alist)

# I want to explain this so I can prove that I understand it:
'''
'''

In the global framework are alist and bubblesort(alist).

Inside of bubblesort you have a for loop where passnum iterates through the length
of alist, which goes from 0 - 5, as there are 6 elements in alist. There is n - 1
pairs of items that need to be compared in order to sort the list since one of these
elements will be comparing and it will not compare to itself, it will compare n - 1 times
until the largest number in the list is sorted into its proper place.

So, you take passnum in range(len(alist) -1, 0, 01): This means that the list begins at -1
of its total, which is 5 elements, because it will sort through 5/6 of the elements to sort the largest out.
This will step at -1, because each time an element is properly sorted you will no longer need to
sort through that element and there is one less pair to compare.

It stops at 0 when there are no longer comparisons needed to be made.

Then, for i in range(passnum): i represents the number being compared to the next number
In this case the first number is 67 and it is being compared to 45. If in this scenario
i is greater than i + 1 (+ 1 meaning + 1 position) which is 45 in this list, then the 67 moves on to compare itself to
the next element.

Then temp is equal to alist[i]
, in this case during the first pass through, is 67.
alist[i] becomes equal to alist[i + 1] and moves into that position, while alist[i+1]
which in this case is 45 becomes equal to temp which is i and thus the first element
in the list, effectively moving 67 into position 1 and 45 into position 0. The nested for loop
then continues and i 

'''
'''
# Selection Sort

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [67, 45, 2, 13, 1, 998]
selectionSort(alist)
print(alist)

# I want to explain this so I can prove that I understand it:
'''
'''
In the global framework is alist and selectionsort(alist).

Next a For Loop is created so that we can begin checking each position in alist.

Then we define positionofMax and set it to position 0.

Then we create a nested For Loop that begins with location at position 1 and is always
just ahead of postionofMax, then a conditional expression states that if alist[location]
is > than alist[positionOfMax] than positionOfMax becomes equal to location, which puts positionOfMax
into the next position in the list. If this is true:

Then a temp variable is created that is equal to alist[fillslot] which is set equal to
alist[positionofmax], this puts alist[filsslot] into temp and alist[positionofmax]
into the fillslot position], ultimately switching to the next position in the list.

If false it moves to the next postion to then compare positionOfMax to fillslot+1. 

This Nested For Loop continues until the largest number is moved to the end of the list,
triggering the next move in the original for loop which continues until all numebrs are sorted.

This differs from a bubbleSort because bubbleSort only passes through two positions then starts
again, continually restarting after two positions are switched. The Selectsion Sort moves the
largest number to the end on the first pass through, and then on and on until the list
is properly sorted. 

'''
'''

# The insertion Sort

def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position - 1

        alist[position]=currentvalue

alist = [67, 45, 2, 13, 1, 998]
insertionSort(alist)
print(alist)

# I want to explain this so I can prove that I understand it:
'''
'''
We begin by putting alist and insertionSort(alist) in the global framework below the insertionSort
function.

Defining inserionSort(alist):

For index in range(1, len(alist)): means index begins at position 1, as position 0 is assumed to equal itself.

currentvalue = alist[index] so begins the loop at the value of position 1, 45. Currentvalue is 45.

position is then set equal to index, which is 1 for position 1.

Then a nested while loop states that while this condition is met, postion>0 and alist[position-1] > currentValue
alist[position] alist[position-1] making position = position -1 which then when the loop runs again
the condition is no longer met, thus you go to the next code which sets postion (now 0) to currentvalue, 26, putting
45 which is less than 67 making them swap positions and you move on to the next position in index in the for
loop.

Anytime the next index is greater than the preceding one the For Loop continues, once it does not it kicks in the while
loop again which, when position dwindles down and finds the proper place for the element. 
'''
'''
# The shell sort

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
                              
alist = [67, 45, 2, 13, 1, 998]
shellSort(alist)
print(alist)

# I want to explain this so I can prove that I understand it:
'''
'''
You start off by writing alist and shellSort(alist) in your global framework. Eventually gapInsertionSort
will also be global.

You define a variable within shellSort called sublistcount = len(alist)//2 which divides the length by 2
but doesn't leave a float, only an int. The while loop kicks in as long as
sublist count is > 0.

Your range is now 3, you utliize the gapInsertionSort function which is: for i in range(start+gap which is
the step, then len(alist) and the gap which is = to sublistcount).

Then they are compared again to one another in the nested while loop, swapping their positions based on
the conditions in the loop. 

'''
'''
# The Merge Sort

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [67, 45, 2, 13, 1, 998]
mergeSort(alist)
print(alist)

# I want to explain this so I can prove that I understand it:
'''
'''
alist and mergeSort(alist) are in the global framewotk.

mergeSort starts by printing "Splitting " and interpolating alist. Then it splits the halves in two
and continues until all values are seperated. They all become split into individual elements and
then as they merge they sort into proper size order. 

'''

# The Quick Sort 

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [67, 45, 2, 13, 1, 998]
quickSort(alist)
print(alist)




