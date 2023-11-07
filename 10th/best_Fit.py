
def best_fit(_memory, _size):
    best_index = -1
    min_size = float('inf')
    
    for idx in range(len(_memory) - _size + 1):
        if all(_memory[i] == 0 for i in range(idx, idx + _size)):
            current_size = 0
            while idx + current_size < len(_memory) and _memory[idx + current_size] == 0:
                current_size += 1
            if current_size < min_size:
                min_size = current_size
                best_index = idx

    return best_index

Memory = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1]
process_Size = 3
index = best_fit(Memory, process_Size)

print(index)
