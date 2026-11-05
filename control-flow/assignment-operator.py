import subprocess
subprocess.run("clear", shell=True)

# assignment operators: =, +=, -=, *=, /=, %=, **=, //=
x = 10
print("x =", x)
x += 5  # equivalent to x = x + 5
print("x =", x)
x -= 3  # equivalent to x = x - 3
print("x =", x)
x *= 2  # equivalent to x = x * 2
print("x =", x)
x /= 4  # equivalent to x = x / 4
print("x =", x)
x %= 3  # equivalent to x = x % 3
print("x =", x)
x **= 2  # equivalent to x = x ** 2
print("x =", x)
x //= 2  # equivalent to x = x // 2