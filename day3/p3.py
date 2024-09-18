def calc(first_num:int, second_num:int) -> int:
    sum = first_num + second_num
    differnece = first_num - second_num
    product = first_num * second_num
    quotient = first_num // second_num
    return sum, differnece, product, quotient
print(calc(10,5))

#python is dynamic so it returns tuple irrespective of the return type