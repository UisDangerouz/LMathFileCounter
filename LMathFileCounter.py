import glob, datetime

pageIndexes = []

def epochToDate(epoch):
    return datetime.datetime.fromtimestamp(int(epoch)).strftime('%d-%m-%Y %H:%M:%S')

print('Finding LMath Pages...')

for fileName in glob.glob('./*.lma'):
    fileName = fileName[2:]

    contents = ''

    with open(fileName, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            contents += str(byte)[2:-1]
            byte = f.read(1)

    pageCount = 0

    for page in contents.split('pages'):
        pageIndex = page[2:40]
        if(".json\\"  in pageIndex):
            pageCount += 1
            pageIndexes.append(pageIndex.split(".json\\")[0][:-3])

    print(str(pageCount) + ' pages found in file ' + fileName)

pageIndexes.sort()

firstPage = epochToDate(pageIndexes[0])
lastPage = epochToDate(pageIndexes[-1])

print(str(len(pageIndexes)) + ' Pages found in total. The first page was created at ' + str(firstPage) + ' and the last one at ' + str(lastPage) + '.')

