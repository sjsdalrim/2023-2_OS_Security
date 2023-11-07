def allocate_memory(_memory, _size):
    for idx in range(len(_memory) - _size + 1):
        
        #check if the current block of the required size is free
        if all(_memory[i] == 0 for i in range(idx, idx + _size)):
            
            #Allocate memory by setting the block to 1
            for i in range(idx, idx + _size):
                _memory[i] = 1

            #return the starting index of allocated block
            return idx
    return -1


memory = [1, 1, 1, 1]
temp = [0] * 100
[memory.append(t) for t in temp]
print(memory)
process_size = 10
index = allocate_memory(memory, process_size)

print(index)
