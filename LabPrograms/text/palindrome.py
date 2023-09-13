class Palin:
    def __init__(self):
        self.isPali = False

    def check_pali(self, string):
        if string == string[::-1]:
            self.isPali = True
        return self.isPali


class PalliInt:

    def __init__(self):
        self.ispali = False

    def check_pali(self, value):
        temp = value
        r = 0
        while temp != 0:
            l = temp % 10
            r = (r * 10) + l
            temp //= 10
        if r == value:
            self.ispali = True
        return self.ispali


letter = input("Enter a string:")
k = Palin()

if k.check_pali(letter):
    print("palindrome")
else:
    print("Not palindrome")

number = int(input("Enter an Integer:"))
k = PalliInt()

if k.check_pali(number):
    print("palindrome")
else:
    print("Not palindrome")