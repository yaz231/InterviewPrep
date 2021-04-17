


def isUnique(str):
    str2 = "".join(sorted(str))
    for i in range(len(str2) - 1):
        if str2[i] == str2[i+1]:
            return False
    return True

def isPermutation(str1, str2):
    # str11 = "".join(sorted(str1))
    # str22 = "".join(sorted(str2))
    # return str11 == str22

    if len(str1) != len(str2):
        return False

    list = [0]*128

    for char in str1:
        list[ord(char)] += 1

    for char in str2:
        list[ord(char)] -= 1
        if list[ord(char)] < 0:
            return False
    return True

def URLify(str):
    str2 = ""
    # print(str)
    for char in str:
        # print(char)
        if char == " ":
            # print("YES")
            str2 = str2 + "%20"
        else:
            str2 = str2 + char
    return str2

def isPalindromPermutation(str):
    str = str.lower().replace(" ", "")
    is_even = len(str)%2 == 0
    str2 = "".join(sorted(str))
    return checkPalindrome(countLetterOccurance(str2), is_even)

def countLetterOccurance(str):
    list = [0]*26
    for char in str:
        list[ord(char) - ord("a")] += 1
    return list

def checkPalindrome(list, even):
    once = True
    if even:
        for num in list:
            if num%2 != 0:
                return False
        return True
    else:
        for num in list:
            if num%2 != 0:
                if once:
                    once = False
                    continue
                else:
                    return False
        return True

def isOneAway(str1, str2):
    res = 0
    for char in str1:
        if char in str2:
            res += 1
    minimum = min(len(str1), len(str2))
    if minimum == res:
        return True
    return False

def stringCompression(str1):
    str2 = ""
    count = 1
    for i in range(len(str1) - 1):
        if str1[i] == str1[i + 1]:
            count += 1
            if i == (len(str1) - 2):
                str2 = str2 + str1[i] + str(count)
            continue
        else:
            str2 = str2 + str1[i] + str(count)
            count = 1
    if len(str2) >= len(str1):
        return str1
    return str2

def zeroMatrix(matrix):

    rows = []
    cols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    # print(rows,cols)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for element in rows:
                if element == i:
                    matrix[i][j] = 0
            for element in cols:
                if element == j:
                    matrix[i][j] = 0
    return matrix

def main():
    # print(isUnique("abdfbgwrtgdfcdefg"))
    # print(isPermutation("gdo", "dog"))
    # print(URLify("Hello World  "))
    # print(isPalindromPermutation("raCe c   ar"))
    # print(isOneAway("pale", "pale"))
    # print(stringCompression("aabcccccaaa"))
    print(zeroMatrix([
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 0],
        [10, 11, 12]
    ]))

if __name__ == '__main__':
    main()