with open('./IBM/text_to_read.txt', 'r') as file_read:

    # showing another file to write
    with open('./IBM/to_write.txt', 'w') as file_write:
        for line in file_read:
            # This line copy both files
            file_write.write(line)