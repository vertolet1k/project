from string import ascii_uppercase


def number_systems(x, y, z):

    if y == 10:

        if z < 10:
            remains1, s = [], ''
            while x >= z:
                remains1.append(x % z)
                x //= z
            remains1.append(x)
            remains1.reverse()
            for numb in remains1:
                s += str(numb)

        else:
            remains2, s, stroch = [], '', ''
            while x >= z:
                remains2.append(x % z)
                x //= z
            remains2.append(x)
            remains2.reverse()
            for rem in remains2:
                if rem >= 10:
                    ind = remains2.index(rem)
                    stroch += ascii_uppercase[rem - 10]
                    remains2[ind] = stroch[-1:]
            for numb in remains2:
                s += str(numb)

    return s


if __name__ == "__main__":
    try:
        x = int(input('переводимое число - '))
        y = int(input('СС этого числа - '))
        z = int(input('СС, в которую нужно перевести - '))
        print(number_systems(x, y, z))
    except ValueError:
        print("Error: Invalid data type entered! Enter a number")
