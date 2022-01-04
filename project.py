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

    elif z == 10:

        s = 0
        # index1 = [index for index in range(len(str(x)))]
        index1 = list(map(lambda index: index, len(str(x))))
        index1.reverse()
        # index2 = [index for index in range(len(str(x)))]
        index2 = list(map(lambda index: index, len(str(x))))
        # data1 = [i for i in str(x)]
        data1 = list(map(lambda i: i, str(x)))
        # data2 = [y ** num for num in index1]
        data2 = list(map(lambda num: y ** num, index1))
        for num2 in index2:
            s += data2[num2] * int(data1[num2])

    else:

        s = 0
        # index1 = [index for index in range(len(str(x)))]
        index1 = list(map(lambda index: index, len(str(x))))
        index1.reverse()
        # index2 = [index for index in range(len(str(x)))]
        index2 = list(map(lambda index: index, len(str(x))))
        # data1 = [i for i in str(x)]
        data1 = list(map(lambda i: i, str(x)))
        # data2 = [y ** num for num in index1]
        data2 = list(map(lambda num: y ** num, index1))
        for num2 in index2:
            s += data2[num2] * int(data1[num2])

        x = s
        y = 10

        if z < 10:
            remains1, s = [], ''
            while x >= z:
                remains1.append(x % z)
                x //= z
            remains1.append(x)
            remains1.reverse()
            for numb in remains1:
                s = s + str(numb)

        else:
            remains2, stroch, s = [], '', ''
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
