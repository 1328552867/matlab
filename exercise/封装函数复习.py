
def roll (a,b):
    out = a + b
    return out

def main ():
    a = int(input('请输入第一个数的值'))
    b = int(input('请输入第二个数的值'))
    c = roll(a,b)
    print('两数和为',c)

if __name__ == '__main__':
    main()
