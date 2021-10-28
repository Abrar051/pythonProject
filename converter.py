def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(numbers=[]):
    max = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]

    return max
