
def main():
    first = int(input("请输入第一个数"));
    second = int(input("请输入第二个数"));
    for i in range(1,20):
        first,second = second, first+second
        print(first)


if __name__ == '__main__':
  main()