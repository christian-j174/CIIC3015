def file_names(file_name, times_names):
    fh = open(file_name, 'w')
    for names in range(times_names):
        user_input = str(input("Name: ")) + '\n'
        fh.write(user_input)
    fh.close()


file_names('chris.txt', 4)
