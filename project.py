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

            # alphabet = ['A' ,'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            remains2, s = [], ''
            while x >= z:
                remains2.append(x % z)
                x //= z
            remains2.append(x)
            remains2.reverse()
            for rem in remains2:
                if rem >= 10:
                    stroch = ''
                    stroch += ascii_uppercase[rem - 10]
                    remains2.remove(rem)
            remains2.append(stroch)
            for numb in remains2:
                s += str(numb)

    return s


if __name__ == "__main__":
    x = int(input('переводимое число - '))
    y = int(input('СС этого числа - '))
    z = int(input('СС, в которую нужно перевести - '))
    print(number_systems(x, y, z))
