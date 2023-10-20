def readfile(nameFile):
    myArray = []
    fo = open(nameFile, "r")
    for line in fo:
        for nbr in line.split():
            myArray.append(nbr)
    fo.close()
    return myArray


def writeToFile(arr):
    with open("output.txt", 'w') as file:
        for j in arr:
            file.write(str(j) + " ")
    file.close()


def write(label):
    with open("output.txt", "w") as text_file:
        text_file.write(label)


keywords = readfile('keywords.txt')

# program = readfile('empty.txt')
program = readfile('inputProgram.txt')
# program = readfile('inputSimpleProgram.txt')
# program = readfile('inputWithoutKeywords.txt')
# program = readfile('inputTwoKeywords.txt')


matches = [words for words in program if words in keywords]
if len(matches) != 0:
    writeToFile(matches)
else:
    write('no keywords in program')

