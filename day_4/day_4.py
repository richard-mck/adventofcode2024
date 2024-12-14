import pprint
from common_functions import get_real_data, transpose_data

XMAS = "XMAS"
SAMX = "SAMX"


def rotate_list_45_degrees(m: int, n: int, data: list[str]) -> list:
    counter = 0
    rotated_data = []
    while counter < 2 * n - 1:
        row = []
        for i in range(m):
            for j in range(n):
                if i + j == counter:
                    row.append(data[i][j])
        row.reverse()
        rotated_data.append("".join(row))
        counter += 1
    return rotated_data


if __name__ == '__main__':
    rows = get_real_data(False)
    pprint.pprint(rows)
    columns = transpose_data(rows)
    pprint.pprint(columns)
    xmas_rows = [i.count(XMAS) for i in rows]
    xmas_cols = [i.count(XMAS) for i in columns]
    rev_rows = [i.count(SAMX) for i in rows]
    rev_cols = [i.count(SAMX) for i in columns]

    rotated_rows = rotate_list_45_degrees(len(rows[0]), len(rows), rows)
    rotated_columns = rotate_list_45_degrees(len(columns[0]), len(columns), columns)
    pprint.pprint(rotated_rows)
    pprint.pprint(rotated_columns)
    print(f"Len xmas_rows: {len(xmas_rows)}, Len xmas_cols: {len(xmas_cols)}")
    print(f"Len rotated_rows: {len(rotated_rows)}, len rotated_cols: {len(rotated_columns)}")
    xmas_rotated_rows = [i.count(XMAS) for i in rotated_rows]
    xmas_rotated_cols = [i.count(XMAS) for i in rotated_columns]
    xmas_rev_rot_rows = [i.count(SAMX) for i in rotated_rows]
    xmas_rev_rot_cols = [i.count(SAMX) for i in rotated_columns]

    print(f"xmas_rows: {xmas_rows}, xmas_cols: {xmas_cols}, rev_rows: {rev_rows}, rev_cols: {rev_cols} ")
    print(
        f"xmas_rows: {xmas_rotated_rows},\n xmas_cols: {xmas_rotated_cols},\n rev_rows: {xmas_rev_rot_rows},\n rev_cols: {xmas_rev_rot_cols} ")
    print(
        sum(xmas_cols) + sum(xmas_cols) + sum(rev_rows) + sum(rev_cols)
        + sum(xmas_rotated_rows) + sum(xmas_rotated_cols) + sum(xmas_rev_rot_rows) + sum(xmas_rev_rot_cols)
    )
    # For every point in the grid, we need to check if xmas is present horizontal, vertical, diagonal, written backwards, or even overlapping other words
    # The easiest way to do this would be a sweep around the compass points (including half intervals) for each point on the grid
    # At the edges we can discard any directions that take us off the grid
    # And we can discard any searches that take us off the grid generally
    # Alternately, we can count the occurences in each row, column, then rotate the data 45 degrees and repeat
