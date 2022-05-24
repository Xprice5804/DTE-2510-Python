import urllib.request

def main():
    url = input("Enter a URL: ").strip()
    crawler(url) # Traverse the Web from the a starting url

def crawler(startingURL):
    listOfPendingURLs = []
    listOfTraversedURLs = []
    
    listOfPendingURLs.append(startingURL)
    while len(listOfPendingURLs) > 0 and \
            len(listOfTraversedURLs) <= 100:
        urlString = listOfPendingURLs[0]
        del listOfPendingURLs[0]
        if urlString not in listOfTraversedURLs:
            listOfTraversedURLs.append(urlString)
            print("Craw", urlString)

            for s in getSubURLs(urlString):
                if s not in listOfTraversedURLs:
                    listOfPendingURLs.append(s)

def getSubURLs(urlString):
    list = []
    
    try:
        input = urllib.request.urlopen(urlString)
        text = input.read().decode() 
        current = 0
        current = text.find("http:", current)
        while current > 0:
            endIndex = text.find("\"", current)
            if endIndex > 0: # Ensure that a correct URL is found
                list.append(text[current : endIndex]) 
                current = text.find("http:", endIndex)
            else:
                current = -1
    except Exception as ex:
        print("Error:", ex)
    
    return list

main()