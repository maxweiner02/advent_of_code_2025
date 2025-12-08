# Part One
with open('input.txt', 'r') as input:
    result = 0
    for line in input:
        digit_one = 0
        digit_one_idx = 0
        digit_two = 0
        for idx, char in enumerate(line[:-2]):
            if int(char) > int(digit_one):
                digit_one = char
                digit_one_idx = idx
        for idx, char in enumerate(line[digit_one_idx+1:-1]):
            if int(char) > int(digit_two):
                digit_two = char
        print("highest number is", int(digit_one + digit_two), 'from', line)
        result += int(digit_one + digit_two)

    print(result)

# Part Two
with open('input.txt', 'r') as input:
    result = 0
    for line in input:
        desiredNumLength = 12
        # number of digits left is equal to length of line[cur_idx:] - 1
        numOfDigitsLeft = 0
        stack = []
        # chop off last char since it is '/n'
        for idx, char in enumerate(line[:-1]):
            # minus 2 because of '/n'
            numOfDigitsLeft = len(line[idx:]) - 2
            # baseline for idx 0
            if idx == 0:
                stack.append(char)
                continue
            # check if its greater than current end of stack
            while int(char) > int(stack[-1]):
                # if we have digits to spare, meaning that the length of the stack + the length left in the line is greater than the desiredNumLength
                # then we can pop off the end of the stack and go to the next end of the stack and check
                if (len(stack) + numOfDigitsLeft) >= desiredNumLength:
                    stack.pop()
                    # if we just emptied the stack, break immediately
                    if len(stack) == 0:
                        break
                # if not, we need to leave the while loop and add the digit to the stack and move on
                else:
                    break
            # this is an edge case where stack[-1] is equal to char, but we already have a full stack so we don't want to add it on
            if(len(stack) < desiredNumLength):
                stack.append(char)
        print("highest number is", int("".join(stack)), 'and is', len(stack), 'from', line)
        result += int("".join(stack))

    print(result)

