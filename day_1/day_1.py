from common_functions import load_input

if __name__ == '__main__':
    # Day 1, part 1
    #data = load_input('example.txt')
    data = load_input('real_data.txt')
    print(data)
    left_list = [int(i.split()[0]) for i in data]
    left_list.sort()
    print(left_list)
    right_list = [int(i.split()[1]) for i in data]
    right_list.sort()
    print(right_list)
    distance = []
    for i, item in enumerate(left_list):
        distance.append(abs(item - right_list[i]))
    print(distance)
    print(sum(distance))