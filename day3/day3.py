def binary_to_decimal(bits):
    total = 0
    for i in range(len(bits)):
        total += bits[len(bits) - 1 - i] * 2 ** i
    
    return total

def convert_to_ints(bit_str):
    bits = []
    for char in bit_str:
        if char == "\n": continue
        bits.append(int(char))
    return bits

def part_one(f):
    data = [[]]
    result = []
    for line in f.readlines():
        for i in range(len(line)):
            bit = line[i]
            if bit == "\n":
                continue
            if len(data) <= i:
                data.append([bit])
            else:
                data[i].append(bit)
            
    for column in data:
        zeros = 0
        ones = 0
        for bit in column:
            if bit == "0":
                zeros += 1
            else:
                ones += 1
        result.append(0 if zeros > ones else 1)

    flipped_result = [1 if i == 0 else 0 for i in result]
    d_result = binary_to_decimal(result)
    d_flipped_result = binary_to_decimal(flipped_result)
    print("Part One:", d_result * d_flipped_result)

def find_most_common(data, index):
    new_data_0 = []
    new_data_1 = []
    for item in data:
        if item[index] == "\n": continue
        if item[index] == "0":
            new_data_0.append(item)
        else:
            new_data_1.append(item)
    selected_data = new_data_0 if len(new_data_0) > len(new_data_1) else new_data_1
    if len(selected_data) > 1:
        return find_most_common(selected_data, index + 1)
    else:
        return convert_to_ints(selected_data[0])       

def find_least_common(data, index):
    new_data_0 = []
    new_data_1 = []
    for item in data:
        if item[index] == "\n": continue
        if item[index] == "0":
            new_data_0.append(item)
        else:
            new_data_1.append(item)
    selected_data = new_data_1 if len(new_data_0) > len(new_data_1) else new_data_0
    if len(selected_data) > 1:
        return find_least_common(selected_data, index + 1)
    else:
        return convert_to_ints(selected_data[0])        

def part_two(f):
    lines = f.readlines()
    oxygen = find_most_common(lines, 0)
    co2 = find_least_common(lines, 0)
    d_oxygen = binary_to_decimal(oxygen)
    d_co2 = binary_to_decimal(co2)
    print("Part Two:",d_co2 * d_oxygen)



def main():
    f = open('input')
    part_one(f)
    f.seek(0)
    part_two(f)
    f.close()

if __name__ == "__main__":
    main()
