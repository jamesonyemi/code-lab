def recur_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recur_binary_search(list[midpoint + 1:], target)
            else:
                return recur_binary_search(list[:midpoint], target)
    return None          