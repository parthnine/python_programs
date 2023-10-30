# Create a 5x5 matrix using a secret key
def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    # add the key to the matrix
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    #Add the rest of the alphabet to the matrix
    # A=65 ... Z=90
    for letter in range(65,91):
        if letter==74: # I/J are in the same position
                continue
        if chr(letter) not in letters_added: # Do not add repeated letters
            letters_added.append(chr(letter))
            
    #print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix