def outer():
    x = 10
    def inner():
        y = x + 1
        x = x + 1
    inner()
    return x

print(outer())  # 15
