with open('rubber_duck.jpeg', 'rb') as fsrc:
    with open('rubber_duck_copy.jpeg', 'wb') as fdst:
        # 1st technique
        # for line in fsrc:
        #     fdst.write(line)

        # 2nd technique
        chunk_size = 4096
        rf_chunk = fsrc.read(chunk_size)
        while len(rf_chunk) > 0:
            fdst.write(rf_chunk)
            rf_chunk = fsrc.read(chunk_size)