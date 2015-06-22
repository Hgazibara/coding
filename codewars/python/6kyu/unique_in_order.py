def unique_in_order(iterable):
    if not iterable:
        return []

    result = []
    # not acceptable if iterable can be iterator/generator and can contain None
    last_seen = None

    for element in iterable:
        if element != last_seen:
            result.append(element)
            last_seen = element

    return result
