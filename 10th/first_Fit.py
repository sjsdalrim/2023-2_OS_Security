def first_fit(_memory, _size):
    for idx in range(len(_memory) - _size + 1):
        if all(_memory[i] == 0 for i in range(idx, idx + _size)):
            return idx
    return -1
