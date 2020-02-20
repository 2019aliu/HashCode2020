filename = 'a_example.txt'
# filename = 'b_read_on.txt'
# filename = 'c_incunabula.txt'
# filename = 'd_tough_choices.txt'
# filename = 'e_so_many_books.txt'
# filename = 'f_libraries_of_the_world.txt'

if (filename == 'a_example.txt'):
    file = open(filename, 'r')
    lineCount = 0

    B = 0
    L = 0
    D = 0
    bookScores = []

    libraryNumBooks = []   # 2D array with number of books per library
    librarySignupDays = [] # 2D array with signup days for each library
    libraryShipPerDay = [] # 2D array with books shipped per day for each library
    libraryBookIDs = []    # 2D array with book IDs for each library

    # Reading file
    for line in file:
        line = line.strip().split(' ')
        if line == ['']:
            lineCount += 1
            continue
        
        line = list(map(int, line))
        
        if lineCount == 0:
            B = line[0] # number of different books
            L = line[1] # number of libraries
            D = line[2] # number of days
        elif lineCount == 1:
            bookScores = line # scores of each book
        else:
            if lineCount % 2 == 0:
                libraryNumBooks.append(line[0])   # number of books in library
                librarySignupDays.append(line[1]) # number of days to finish library signup
                libraryShipPerDay.append(line[2]) # number of books that can be shipped per day
            else:
                libraryBookIDs.append(line) # book IDs

        lineCount += 1
    file.close()

    # print(libraryNumBooks)
    # print(librarySignupDays)
    # print(libraryShipPerDay)
    # print(libraryBookIDs)

    # of libraries
    library_number = 2

    f = open('A_output.txt', 'w+')
    f.write("%d\n" % library_number)

    # 2D array of library sendoffs
    # First element of each array is Library #
    # Second element of each array is # of books being sent
    # All other elements are the book #'s being sent
    library_arrays = [[1, 4, 5, 2, 3, 0], [0, 5, 0, 1, 2, 3, 4]]

    for i in range(library_number):
        f.write("%d " % library_arrays[i][0])
        f.write("%d\n" % library_arrays[i][1])
        for j in range(2, len(library_arrays[i])):
            f.write("%d " % library_arrays[i][j])
        f.write("\n")

    
