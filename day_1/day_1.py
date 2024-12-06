from common_functions import load_input

if __name__ == '__main__':
    real_data = False
    filename = "real_data.txt" if real_data else "example.txt"
    # Day 1, part 1
    data = load_input(filename)
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
    # Day 1, part 2
    similarity = []
    for item in left_list:
        item_count = right_list.count(item)
        print(f"{item}: {item_count}")
        similarity.append(item * item_count)
    print(sum(similarity))