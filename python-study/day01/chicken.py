'''
百鸡百钱
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
'''

money = 100;
cock = 5;
hen = 3;
baby_chichen = 1/3;

def exhaustion():
    for cockNum in range(0,money//cock):
        for henNum in range(0,(money - cockNum * cock)//hen):
            baby_chichen_num = 100 - cockNum - henNum;
            if((baby_chichen_num * baby_chichen) + (henNum * hen) + (cock * cockNum))==100:
                print("公鸡 %d 只，母鸡 %d 只，小鸡 %d 只"%(cockNum,henNum,baby_chichen_num))


if __name__ == '__main__':
    exhaustion()