def part_one(f):
    horizontal = 0
    depth = 0
    for line in f.readlines():
        data = line.split()
        num = int(data[1])
        match data[0]:
            case "forward":
                horizontal += num
            case "down":
                depth += num
            case "up":
                depth -= num
    print("Part One:", horizontal * depth)

def part_two(f):
    horizonal = 0
    depth = 0
    aim = 0
    for line in f.readlines():
        data = line.split()
        num = int(data[1])
        match data[0]:
            case "forward":
                horizonal += num
                depth += num * aim
            case "down":
                aim += num
            case "up":
                aim -= num
    print("Part Two:", horizonal * depth)

def main():
    f = open('input')
    part_one(f)
    f.seek(0)
    part_two(f)
    f.close()

if __name__ == "__main__":
    main()