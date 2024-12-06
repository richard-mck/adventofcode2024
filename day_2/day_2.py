from common_functions import get_real_data

def get_sorted_and_reversed(row: list[int]) -> (list[int], list[int]):
    sorted_row = row.copy()
    sorted_row.sort()
    return sorted_row, list(reversed(sorted_row))

def check_if_row_is_safe(row: list[int]) -> bool:
    for i in range(1, len(row)):
        diff = abs(row[i] - row[i - 1])
        print(f"{diff} = {row[i]} - {row[i - 1]}")
        # If the values are within 1-3 AND not the same, we're safe
        if diff <= 3 and diff != 0:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    # Day 2, part 1
    data = get_real_data(False)
    # Convert input to ints
    for i, row in enumerate(data):
        data[i] = [int(i) for i in row]
    print(data)
    safe_reports = []
    for row in data:
        sorted_row, reverse_row = get_sorted_and_reversed(row)
        print(f"Sorted row: {sorted_row}, reverse row: {reverse_row}")
        # If a report is already sorted or reverse sorted correctly, we only need to check the differences between the values
        if row == sorted_row or row == reverse_row:
            safe_reports.append(row)
            if not check_if_row_is_safe(row):
               safe_reports.pop()
    print(safe_reports)
    print(len(safe_reports))