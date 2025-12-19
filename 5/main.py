with open("input.txt", "r") as file:
    ranges = []
    ids = []
    reached_blank = False

    for line in file:
        stripped = line.rstrip("\n")
        if stripped == "":
            reached_blank = True
            continue
        if reached_blank:
            ids.append(int(stripped))
        else:
            range = line.split("-")
            start, end = int(range[0]), int(range[1])
            ranges.append((start, end))

    def simplify_ranges(ranges):
        # sort ranges in ascending order
        ranges.sort(key=lambda x: x[0])
        # start with the lowest range since we sorted them
        merged = [ranges[0]]
        # start looping with the second range in the array
        for range in ranges[1:]:
            last_start, last_end = merged[-1]
            curr_start, curr_end = range

            # if the end of the current range is less than or equal to current highest
            # (which will be the end of the last range in the merged array) then we
            # know that we can merge the range
            if curr_start <= last_end + 1:
                merged[-1] = (last_start, max(last_end, curr_end))
            else:
                # there is no overlap so make this the new highest range to compare against
                merged.append(range)

        return merged

    simpleRanges = simplify_ranges(ranges)
    resultOne = 0
    for id in ids:
        # if its less than the lowest number in the ranges just skip to the next one
        if id < simpleRanges[0][0]:
            continue
        # if its greater than the highest number in the ranges just skip to the next one
        elif id > simpleRanges[-1][1]:
            continue
        # now we need to go through the ranges and find if the id is inside any of the ranges (yikes)
        for range in simpleRanges:
            start, end = range
            if id >= start and id <= end:
                # print(id, "is within the range of", start, "-", end)
                resultOne += 1
                break

    resultTwo = 0
    for range in simpleRanges:
        start, end = range
        # need to add one to be inclusive
        resultTwo += end - start + 1

    print("Part 1:", resultOne)
    print("Part 2:", resultTwo)
