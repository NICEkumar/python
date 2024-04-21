def three(n):
    if n <= 0 or not isinstance(n, int):
        return "Invalid input"

        # Iterate from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Find the difference of n and i squared
        diff = n - i ** 2
        # If the difference is a perfect square, return True
        if int(diff ** 0.5) ** 2 == diff:
            return True
        # If no such combination is found, return False
    return False

n = int(input())
print(three(n))
