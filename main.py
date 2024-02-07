def generate_islanders(position, heavier):
    islander_weights = [1] * 12
    if heavier:
        islander_weights[position] += 1
    else:
        islander_weights[position] -= 1
    return islander_weights


def find_outlier(islanders):
    # Divide people into two groups of people 0-3 and 4-8
    group_a = islanders[:4]
    group_b = islanders[4:8]
    result = weigh(group_a, group_b)
    if result == 0:
        # If weight is even, outlier must be in set C.
        return find_outlier_in_group_c(islanders)

    # Create new sets of people 1, 3, 5 and 2, 4, 6
    group_a = islanders[0:5:2]
    group_b = islanders[1:6:2]
    if result < 0:
        result = weigh(group_a, group_b)
        if result < 0:
            group_a = [islanders[0]]
            group_b = [islanders[2]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 1, "lighter"
            elif result == 0:
                return 6, "heavier"
            elif result > 0:
                return 3, "lighter"
            raise
        elif result == 0:
            group_a = [islanders[6]]
            group_b = [islanders[7]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 8, "heavier"
            elif result > 0:
                return 7, "heavier"
            raise
        elif result > 0:
            group_a = [islanders[1]]
            group_b = [islanders[3]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 2, "lighter"
            elif result == 0:
                return 5, "heavier"
            elif result > 0:
                return 4, "lighter"
            raise
        raise
    elif result > 0:
        result = weigh(group_a, group_b)
        if result < 0:
            group_a = [islanders[1]]
            group_b = [islanders[3]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 4, "heavier"
            elif result == 0:
                return 5, "lighter"
            elif result > 0:
                return 2, "heavier"
            raise
        elif result == 0:
            group_a = [islanders[6]]
            group_b = [islanders[7]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 7, "lighter"
            elif result > 0:
                return 8, "lighter"
            raise
        elif result > 0:
            group_a = [islanders[0]]
            group_b = [islanders[2]]
            result = weigh(group_a, group_b)
            if result < 0:
                return 3, "heavier"
            elif result == 0:
                return 6, "lighter"
            elif result > 0:
                return 1, "heavier"
            raise
        raise
    raise


def find_outlier_in_group_c(islanders):
    # Create set with person 9 and 10.
    group_a = islanders[8:10]
    # Create set with person known to have average weight and 11.
    group_b = islanders[0::11]
    result = weigh(group_a, group_b)
    if result < 0:
        # Group A is lighter
        group_a = [islanders[8]]
        group_b = [islanders[9]]
        result = weigh(group_a, group_b)
        if result < 0:
            return 9, "lighter"
        elif result == 0:
            return 12, "heavier"
        elif result > 0:
            return 10, "lighter"
        raise
    elif result == 0:
        group_a = [islanders[10]]
        group_b = [islanders[0]]
        result = weigh(group_a, group_b)
        if result > 0:
            return 11, "heavier"
        elif result < 0:
            return 11, "lighter"
        raise
    elif result > 0:
        group_a = [islanders[8]]
        group_b = [islanders[9]]
        result = weigh(group_a, group_b)
        if result < 0:
            return 10, "heavier"
        elif result == 0:
            return 12, "lighter"
        elif result > 0:
            return 9, "heavier"
        raise
    raise


def weigh(group_a, group_b):
    global count
    count += 1
    print("Weighed {} time(s)".format(count))
    if count > 3:
        raise
    return sum(group_a) - sum(group_b)


if __name__ == "__main__":
    for i in range(12):
        count = 0
        islanders = generate_islanders(i, False)
        outlier, weight = find_outlier(islanders)
        print("{} is {}".format(outlier, weight))

        count = 0
        islanders = generate_islanders(i, True)
        outlier, weight = find_outlier(islanders)
        print("{} is {}".format(outlier, weight))
