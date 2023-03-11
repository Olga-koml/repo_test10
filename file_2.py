x = 10
y = 100
print(y/x)

def multiply(a, b):
    return a * b


def read_input():
    a = int(input())
    b = int(input())
    return a, b

def main():
    a, b = int(input())
    multiply(a, b)

if __name__ == '__main__':
    a, b = read_input()
    print(multiply(a, b))

def file_add():
    print('Add file')


