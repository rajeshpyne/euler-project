import time


def check_palindrom(num):
    orig_num = num
    reverse_num = 0
    while num > 0:
        rem = int(num / 10)
        quo = num % 10
        reverse_num = reverse_num * 10 + quo
        num = rem
    if orig_num == reverse_num:
        return True


def three_digit_mul_palin():
    start = 999
    end = 100
    largest_palindrom = 0
    for i in range(start,end,-1):
        for j in range(i ,end,-1):
            product = i * j
            if check_palindrom(product) == True:
                if product > largest_palindrom:
                    largest_palindrom = product
    return largest_palindrom


def compute(lower_limit, upper_limit):
    a = max(i*j
            for i in range(upper_limit, lower_limit, -1)
            for j in range(i, lower_limit, -1) if str(i*j) == str(i*j)[::-1])
    return a

if __name__ == '__main__':

    start_time = time.time()
    print("compute result =", three_digit_mul_palin(),
          ", time taken - ", (time.time() - start_time), " seconds")
    assert three_digit_mul_palin() == 906609
    print("Test passed")

    start_time = time.time()
    print("compute result =", compute(100, 999),
          ", time taken - ", (time.time() - start_time), " seconds")
    assert compute(100, 999) == 906609

    print("all test case passed")
