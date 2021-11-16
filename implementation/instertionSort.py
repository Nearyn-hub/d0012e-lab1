def insertionSort1(a, n):               # function
    for i in range(1,n):                # go through array/list of numbers from index 1
        temp = a[i]                     # save position index to temp
        j = i-1                         # set pointer to one position left to i
        while j >= 0 and a[j] > temp:   # if j is greater or equal to 0 and temp index 
            a[j+1] = a[j]               # add one to j  
            j -= 1                      # then move the position of j
        a[j+1] = temp                   # move the position of j up one position

#Måste nog anpassa comments lite eller ta bort de efter Stegbeskrivning.

#arr = ["insert list of int here"]
#insertionSort(arr)
#for i in range(len(arr)):
#    print ("% d" % arr[i])
