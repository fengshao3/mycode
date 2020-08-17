"""
水仙花数
153 = 1^3+5^3+3^3
"""
def printss():
    for i in range(100,1000):
        if isNarcissusNumber(i):
            print(i)

def isNarcissusNumber(number):
    bai = number // 100
    shi = number // 10 % 10
    ge = number % 10
    return bai ** 3 + shi ** 3 + ge ** 3 == number

if __name__ == '__main__':
    printss()