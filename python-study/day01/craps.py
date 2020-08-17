'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
'''

from random import randint


def main():
    money = 1000
    isFirst = True;
    last = 0;
    while money > 0:
        print("玩家当前余额： ",money)
        debt = int(input("输入赌注："))
        current = randint(1,6) + randint(1,6)
        print("玩家摇出%d点"%(current))
        if isFirst:
            if current == 7 or current == 11:
                print("玩家胜")
                money = money + debt
            elif current in (2,3,12):
                print("庄家胜")
                money = money - debt
            else:
                print("和")
                last = current
                isFirst = False
        else:
            if current == last:
                print("玩家胜")
                money = money + debt;

            elif current == 7:
                print("庄家胜")
                money = money - debt
            else:
                print("和")
                last = current
                isFirst = False
if __name__ == '__main__':
    main()