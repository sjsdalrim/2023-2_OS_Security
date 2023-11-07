
def worst_fit(_memory, _size):
    worst_index = -1
    max_size = 0
    
    for idx in range(len(_memory) - _size + 1):
        if all(_memory[i] == 0 for i in range(idx, idx + _size)):
            current_size = 0
            while idx + current_size < len(_memory) and _memory[idx + current_size] == 0:
                current_size += 1
            if current_size > max_size:
                max_size = current_size
                worst_index = idx

    return worst_index

Memory = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
process_Size = 1
index = worst_fit(Memory, process_Size)

print(index)
