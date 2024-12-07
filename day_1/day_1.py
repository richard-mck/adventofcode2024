from common_functions import get_real_data

if __name__ == '__main__':
    # Day 1, part 1
    data = get_real_data(False)
    print(data)
    left_list = [int(i[0]) for i in data]
    left_list.sort()
    print(left_list)
    right_list = [int(i[1]) for i in data]
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