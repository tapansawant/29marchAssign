def CheckPrime(a):
    if a > 1:
        for j in range(2, int(a / 2) + 1):
            if (a % j) == 0:
                return False
        else:
            return True
    else:
        return False


def CheckPalindrome(a):
    # val = int(a)
    # if a == str(a)[::-1]:
    #     return True
    # else:
    #     return False
    temp = a
    rev = 0
    while a > 0:
        dig = a % 10
        rev = rev * 10 + dig
        a = a // 10
    if temp == rev:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter the number:"))
    print(CheckPrime(num))
    print(CheckPalindrome(num))
