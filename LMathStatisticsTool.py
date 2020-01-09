import glob, zipfile, json

def extractData(zipArchive):
    formula = 0
    pageTitles = []

    with zipArchive.open('pages.json') as IndexFile:
        pageIndexes = json.loads(IndexFile.read())
        
    for pageIndex in pageIndexes:
        with zipArchive.open('pages/' + pageIndex + '.json') as pageFile:
            page = json.loads(pageFile.read())
            
            formula += page['content'].count('img')
            pageTitles.append(page['title'])

    return [pageTitles, formula]

print('Finding LMath files...')

pagesTotal = 0
formulasTotal = 0

for fileName in glob.glob('./*.lma'):
    fileName = fileName[2:]

    with zipfile.ZipFile(fileName, 'r') as archive:  
        data = extractData(archive)
        pagesTotal += len(data[0])
        formulasTotal += data[1]

        print('File ' + fileName + ' contains ' + str(data[1]) + ' formulas and has ' + str(len(data[0])) + ' pages:\n' + ', '.join(data[0]) + '.')

print('Scan complete! Found ' + str(formulasTotal) + ' formulas and ' + str(pagesTotal) + ' pages in total.')