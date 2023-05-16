# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()
    if input_type[0] == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        fileName = "tests/06"
        file1 = open(fileName)
        pattern = file1.readline().rstrip()
        text = file1.readline().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    patternHash = 0
    patternLength = len(pattern)
    textHash = 0
    Q = 101
    for i in range(patternLength):
        patternHash = (10*patternHash+ord(pattern[i])) % Q
        textHash = (10*textHash+ord(text[i])) % Q
    occurances = []
    for i in range(len(text) - patternLength+1):
        if patternHash == textHash and text[i:i+patternLength] == pattern:
            occurances.append(i)
        if i < len(text) - patternLength:
            textHash = (10*(textHash - ord(text[i]) * pow(10, patternLength-1, Q)) + ord(text[i+patternLength])) % Q
    # and return an iterable variable #[0]
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

