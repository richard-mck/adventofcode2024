if __name__ == '__main__':
    with open('example.txt') as f:
        data = f.readlines()
    print(data)
    data = data[0].split("mul")
