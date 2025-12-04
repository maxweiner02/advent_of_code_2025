# Part One
with open('input.txt', 'r') as input:
    result = 0
    for line in input:
        ranges = line.split(',')
        for num_range in ranges:
            limits = num_range.split('-')
            min = limits[0]
            max = limits[1]
            for i in range(int(min), int(max)+1):
                i_as_string = str(i)
                # if the number is an odd length it can't be invalid
                if len(i_as_string) % 2 == 1:
                    continue
                mid = len(i_as_string) // 2
                first_half = i_as_string[:mid]
                last_half = i_as_string[mid:]
                if first_half == last_half:
                    result += i

    print(result)

# Part Two
def into_chunks(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

with open('input.txt', 'r') as input:
    result = 0
    for line in input:
        ranges = line.split(',')
        for num_range in ranges:
            limits = num_range.split('-')
            min = limits[0]
            max = limits[1]
            for i in range(int(min), int(max)+1):
                i_as_string = str(i)
                for j in range(1, (len(i_as_string) // 2)+1):
                    chunks = into_chunks(i_as_string, j)
                    if len(set(chunks)) == 1:
                        result += i
                        break
    print(result)

