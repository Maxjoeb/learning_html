
#File input that uses readline to parse file lines, splits the keys
#into numbers and words for sorting, uses sorted method to sort, and returns sorted entries
def read_words_from_file(file_name):
    entries = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            num, word = line.split()
            entries.append((int(num), word))
    sorted_entries = sorted(entries, key=lambda x: x[0]) 
    return sorted_entries

#To emulate the pyramid shape, sort the entries into a staircase and
#store the last entry of each step
def generate_staircase_pattern(entries):
    sorted_entries = sorted(entries, key=lambda x: x[0])
    step = 1
    last_numbers = []
    while len(sorted_entries) != 0:
        if len(sorted_entries) >= step:
            stair = sorted_entries[0:step]
            last_numbers.append(stair[-1])
            sorted_entries = sorted_entries[step:]
            step += 1
        else:
            return false
    return last_numbers    

#Main function that calls the "sorting" functions and iterates through
#the final items in last_
def main():
    file_name = "example_tab.txt"  
    sorted_entries = read_words_from_file(file_name)
    last_numbers = generate_staircase_pattern(sorted_entries)
    for step in last_numbers:
        print(step)

if __name__ == "__main__":
    main()
