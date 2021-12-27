def sum_range(list, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += list[i]
    return sum

def part_one():
    with open('input') as f:
        increased = 0
        previous = None
        for line in f.readlines():
            depth = int(line)
            if previous is not None and previous < depth:
                increased += 1
            previous = depth
        print("Part 1:", increased)
        f.close()

def part_two():
    with open('input') as f:
        increased = 0
        window = []
        for line in f.readlines():
            depth = int(line)
            window.append(depth)
            if len(window) > 3:
                previous_sum = sum_range(window, 0, 2)
                new_sum = sum_range(window, 1, 3)
                if previous_sum < new_sum:
                    increased += 1
                window.pop(0)
    print("Part 2:", increased)



def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()