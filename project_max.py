from string import digits, ascii_uppercase


def convert_base(num: str, to_base: int = 10, from_base: int = 10) -> str:
    n = int(str(num), from_base)
    alphabet, res = digits + ascii_uppercase, ''
    print(alphabet)
    while n > 0:
        n, m = n // to_base, n % to_base
        res += alphabet[m]
    return res[::-1]

if __name__ == "__main__":
    try:
        num = input('Переводимое число (int) - ')
        from_base = int(input('СС этого числа (int) - '))
        to_base = int(input('СС, в которую нужно перевести (int) - '))
        print(convert_base(num, to_base, from_base))
    except ValueError:
        print("Error: Invalid data type entered! Enter a number")
