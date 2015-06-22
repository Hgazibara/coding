def same_structure_as(original, other):
    check = (isinstance(original, list), isinstance(other, list))

    if all(not c == True for c in check):
        return True

    if any(check) and not all(check):
        return False

    if len(original) != len(other):
        return False

    for left, right in zip(original, other):
        if not same_structure_as(left, right):
            return False

    return True
