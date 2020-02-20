# filename = 'a_example.txt'
# filename = 'b_read_on.txt'
# filename = 'c_incunabula.txt'
# filename = 'd_tough_choices.txt'
# filename = 'e_so_many_books.txt'
filename = 'f_libraries_of_the_world.txt'
from operator import itemgetter

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

file.close()# of libraries

# Priority weights
score_weight = 0.01
signup_weight = 0.99

libraries = []

for i in range(len(libraryNumBooks)):
    library = {}
    library["signup"] = librarySignupDays[i]
    library["book_ids"] = libraryBookIDs[i]
    library["book_number"] = libraryNumBooks[i]
    library["capacity"] = libraryShipPerDay[i]
    libraries.append(library)
    print(library)
    
def book_id_function(book_id):
    return bookScores[book_id]

# Cleanse the libraries of their duplicates
totalBookIDs = set()

index = 0
# Calculate the priority for each library: score_weight * score + signup_weight * days
for library in libraries:
    signup = library["signup"]
    capacity = library["capacity"]
    book_ids = library["book_ids"]
    book_number = library["book_number"]
    library["library_number"] = index
    # Calculate the sum of the scores
    score = 0
    for i in range(len(book_ids)):
        score += bookScores[book_ids[i]]
    # Consider the # of days needed to scan all books for each library    
    library["priority"] = score_weight * score + signup_weight * (D / (signup + (book_number / capacity)))
    index += 1
    
    # Sort the book Ids by their scores
    book_ids.sort(key = book_id_function, reverse=True)
    library["book_ids"] = book_ids

sorted_libraries = sorted(libraries, key = itemgetter("priority"), reverse=True)

library_number = len(sorted_libraries)

f = open('output.txt', 'w+')
f.write("%d\n" % library_number)

# 2D array of library sendoffs
# First element of each array is Library #
# Second element of each array is # of books being sent
# All other elements are the book #'s being sent
library_arrays = []
for library in sorted_libraries:
    new_library_array = []
    new_library_array.append(library["library_number"])
    new_library_array.append(library["book_number"])
    for i in range(library["book_number"]):
        new_library_array.append(library["book_ids"][i])
    library_arrays.append(new_library_array)
    
for i in range(library_number):
    f.write("%d " % library_arrays[i][0])
    f.write("%d\n" % library_arrays[i][1])
    for j in range(2, len(library_arrays[i])):
        f.write("%d " % library_arrays[i][j])
    f.write("\n")
