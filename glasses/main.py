def glasses_problem(n, total_floors):
    def binary_search(glasses, floors, pairs):
        if glasses == 1 or floors == 0 or floors == 1:
            return floors
        if (glasses, floors) in pairs:
            return pairs[(glasses, floors)]

        low, high = 1, floors
        min_attempts = float('inf')

        while low <= high:
            mid = (low + high) // 2

            # recursively calculate the worst-case attempts if glass breaks
            breaks = binary_search(glasses - 1, mid - 1, pairs)

            # recursively calculate the worst-case attempts if glass does not break
            does_not_break = binary_search(glasses, floors - mid, pairs)

            # calculate the worst-case attempts for the current attempt
            worst_case_attempts = 1 + max(breaks, does_not_break)

            # calculate minimum number of attempts needed in the worst case for the given number of glasses and floors
            min_attempts = min(min_attempts, worst_case_attempts)

            # update search range based on the comparison of attempts
            if breaks > does_not_break:
                high = mid - 1
            else:
                low = mid + 1

        pairs[(glasses, floors)] = min_attempts
        return min_attempts

    pairs = {}
    return binary_search(n, total_floors, pairs)


def main():
    num_glasses = int(input("Number of glasses: "))
    num_floors = int(input("Total number of floors: "))
    result = glasses_problem(num_glasses, num_floors)
    print(f"Needed number of attempts: {result}")


if __name__ == '__main__':
    main()
