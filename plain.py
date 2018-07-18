#@author Sourajit Karada
from sys import stdin as inp
from math import pow

def nextSmallestPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftSideNumber(num)
    middle=getMiddleNumber(num)
    if oddDigits:
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
    if newNum>num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextSmallestPalindrome(roundUp(num))
 
def getLeftSideNumber(num):
    return str(num)[:len(str(num))/2]
 
def getMiddleNumber(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment

def getResults(resultList):
    print '\nResults..... '
    for n in resultList:
        print int(n)


if __name__=='__main__':
    try:
        n = int(inp.readline())
    except ValueError:
        print "\nEntered value is a string. Kindly re-run and enter a number"
    allEnteredNum = []
    palinNums = []
    for _ in range(n):
        try:
            digit = int(inp.readline().strip('\n'))
            if(digit > 1000000):
                print "Please enter digits below 1000000"
                break
        except ValueError:
            print "\nEntered value is a string. Kindly re-run and enter a number"
            break
        allEnteredNum.append(digit)
        palinNums.append(nextSmallestPalindrome(digit))
    if(len(palinNums)):
        getResults(palinNums)

