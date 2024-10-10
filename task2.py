

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
        print()                       # num = 4, 9, 2, 1
                                       # total = 4, 13, 15, 16
    return total

result = tally([4, 9, 2, 1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
                                       # idx = 0, 1, 2, 3
        print()                        # new_list = [4], [4, 9], [4, 9, 2], [4, 9, 2, 1]
    return new_list                    # How does this loop differ from that above?   It loops based on an index rather than elements in the list

result = copy([4, 9, 2, 1])



def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
        print()                        # value = 4, 9, 2, 1
                                       # new_list = [5], [5, 10], [5, 10, 3], [5, 10, 3, 2]
    return new_list

result = increment_all([4, 9, 2, 1])