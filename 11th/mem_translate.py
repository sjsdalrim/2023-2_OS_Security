def translate_address(virtual_address, page_size, page_table):
    page_number, offset = divmod(virtual_address, page_size)
    print(page_number, offset)
    if page_number in page_table:
        physical_address = page_table[page_number] * page_size + offset
        return physical_address
    else:
        return None


page_size = 1024 # Assume 1 KB page size
page_table = {
    #page_num: frame_num
    0: 5,
    1: 6,
    2: 2,
    3: 7,
    4: 4,
}

virtual_address = 4096
physical_address = translate_address(virtual_address, page_size, page_table)
print(f"Physical Address: {physical_address}")
