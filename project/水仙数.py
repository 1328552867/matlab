
def main():
    A = list(range(100,1000))
    for B in A:
        a = int(B % 1000/100 ) # 百位
        b = int(B % 100/10 ) # 十位
        c = int(B % 10 )# 个位
        if a**3+b**3+c**3 == B:
            print('水仙数为',B)
if __name__ == '__main__':
    main()
