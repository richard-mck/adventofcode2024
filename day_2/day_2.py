from common_functions import get_real_data

def check_get_sorted_and_reversed(row: list[int]) -> bool:
    sorted_row = row.copy()
    sorted_row.sort()
    if row == sorted_row or row == list(reversed(sorted_row)):
        return check_if_row_is_safe(row)
    return False

def check_if_row_is_safe(row: list[int]) -> bool:
    for i in range(1, len(row)):
        diff = abs(row[i] - row[i - 1])
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
        # If a report is already sorted or reverse sorted correctly, we only need to check the differences between the values
        if check_get_sorted_and_reversed(row):
            safe_reports.append(row)
    print(safe_reports)
    print(len(safe_reports))

    # Day 2, Part 2
    reports_with_damper = []
    for row in data:
        # Append known safe rows
        if row in safe_reports:
            reports_with_damper.append(row)
            continue
        # Check each iteration of the row with one value removed
        for i in range(len(row)):
            pop_row = row.copy()
            pop_row.pop(i)
            if check_get_sorted_and_reversed(pop_row):
                print(f"Row is safe: {pop_row} - original row: {row}")
                reports_with_damper.append(row)
                # If a row is safe with a single value removed, no further checks are needed
                break

    print(f"Number of safe reports: {len(reports_with_damper)}")