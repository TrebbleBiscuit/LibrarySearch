# TODO: Program breaks if there is only one shelf - not that this is really a big problem...

booklist = []
data = open('bookdata.txt')
for line in data:
    booklist.append(line.strip().split(" - "))

for x in range (0,len(booklist)):
    for y in range(0,2):
        try:
            if booklist[x][y].startswith("#"):
                booklist.remove(booklist[x])
        except IndexError:
            pass

index = 0
blankspaces = []
while index < len(booklist):
    try:
        index = booklist.index([''], index)
        if index == -1:
            break
        blankspaces.append(index)
        index += 1
    except ValueError:
        break

shelf = {}
shelf["0"] = booklist[0:blankspaces[0]]
for x in range(1, len(blankspaces)+1):
    try:
        shelf["{x}".format(x = x)] = booklist[blankspaces[x-1]:blankspaces[x]]
    except IndexError:
        shelf["{x}".format(x = x)] = booklist[blankspaces[x-1]:]


entry = raw_input("Input a Search Term: ")
print ("")
print "Searching for {entry}. . . ".format(entry = entry)
for x in range(0,len(booklist)):
    for y in range(0,2):
        try:
            if entry.lower() in booklist[x][y].lower():  # somehow this works
                print("")
                print 'Book number {entrynumber} in library'.format(entrynumber = x+1)
                print '{bookname} by {author}'.format(bookname = booklist[x][1], author = booklist[x][0])
                for y in range (0,len(shelf)):
                    if booklist[x] in shelf[str(y)]:
                        print "Shelf {y}".format(y = y+1)
        except IndexError:
            pass