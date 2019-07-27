import time


def calculate(n,m):
    pow_result = pow(n, m)
    digit_count = len(str(pow_result))
    count = 0
    if digit_count == m:
        print("N :: "+str(n))
        print("M :: "+str(m))
        print("Result :: "+str(pow_result))
        return True


if __name__ == '__main__':
    start = time.time()
    count = 0
    for i in range(1,100):
        for j in range(1,100):
            t = calculate(i,j)
            if t == True:
                count += 1
    print(count)
    end = time.time()
    print(end - start)