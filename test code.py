import nump

def isZigzag(numbers):
    #create array & initiate to 0
    arr = list(len(numbers) - 2)
    i = 0
    while (i < len(arr) - 2):
        if (numbers[i] > numbers[i+1]) and (numbers[i+1] < numbers[i+2]) or (numbers[i] < numbers[i+1]) and (numbers[i+1] > numbers[i+2]):
            arr[i] = 1
        i = i + 1
    return arr


***
