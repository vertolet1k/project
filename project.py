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

        ind, ind2, data, data2, s = [], [], [], [], 0

        for index1 in range(len(str(x))):
            ind.append(index1)
        ind.reverse()

        for index1 in range(len(str(x))):
            ind2.append(index1)

        for i in str(x):
            data.append(i)

        for num in ind:
            data2.append(y ** num)

        for num2 in ind2:
            s += data2[num2] * int(data[num2])

    else:

        index, index2, data, data2, s = [], [], [], [], 0

        for index1 in range(len(str(x))):
            index.append(index1)
        index.reverse()

        for index1 in range(len(str(x))):
            index2.append(index1)

        for i in str(x):
            data.append(i)

        for num in index:
            data2.append(y ** num)

        for num2 in index2:
            s += data2[num2] * int(data[num2])

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
