def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


a, b = 10, 5

print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))


import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)
df = df.replace("Alice", "Alice Smith")
print(df)
