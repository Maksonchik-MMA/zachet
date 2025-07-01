def read_lines(filename):
    with open(filename, 'r') as file:
        return file.readlines()
        for line in file:
            yield line
for line in read_lines("example.txt"):
    print(line.strip())
 