def main():
    # Open file for input
    input = open("C:\\liangcentral\\python2eREVEL\\x.txt", "r")
    text = input.read()
    input.close() # Close the input file

    output = open("C:\\idrive\\web\\AltTextPy\\x.xml", "w")
    
    i = text.index("<PD")
    
    while i > 0:
        j = text.index(">", i)
        pd = text[i : j + 1].lower()
        old = text
        text = text[j + 1 :]
        lines = text.split("\n")

        if "uml" in pd:
            pd = pd[pd.index("figure") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "uml">')
        elif "unnamedfigure" in pd:
            pd = pd[pd.index("unnamedfigure") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "unnamedfigure">')
        elif "figure" in pd:
            pd = pd[pd.index("figure") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "figure">')
        elif "wordmatch" in pd:
            pd = pd[pd.index("wordmatch") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "wordmatch">')
        elif "unnamedliveexampleresultonly" in pd:
            pd = pd[pd.index("unnamedliveexampleresultonly") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "unnamedliveexampleresultonly">')
        elif "unnamedliveexample" in pd:
            pd = pd[pd.index("unnamedliveexample") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "unnamedliveexample">')
        elif "liveexample" in pd:
            pd = pd[pd.index("liveexample") : ]
            title = pd.split()[1]
            if "Listing" in old[i - 40 : i]:
                print('    <interactive title = "' + title + '" type = "liveexamplelisting">')
            else:
                print('    <interactive title = "' + title + '" type = "liveexample">')
        elif "checkpoint" in pd:
            pd = pd[pd.index("checkpoint") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "checkpoint">')
        elif "quiz" in pd:
            pd = pd[pd.index("quiz") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "quiz">')
        elif "exercisecheck" in pd:
            pd = pd[pd.index("exercisec") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "checkexercise">')
        elif "exercise" in pd:
            pd = pd[pd.index("exercise") : ]
            title = pd.split()[1]

            print('    <interactive title = "' + title + '" type = "exercise">')
            output.write("exercise\n")
            output.write(lines[1] + "\n")
        elif "listing" in pd:
            pd = pd[pd.index("listing") : ]
            title = pd.split()[1]
            location = lines[1]
            if "RunTurtle" in location:
                print('    <interactive title = "' + title + '" type = "liveexampleguilisting">')
            elif "LiveRun" in location:
                print('    <interactive title = "' + title + '" type = "liveexamplelisting">')
            else:
                print('    <interactive title = "' + title + '" type = "listing">')
        elif "freestyle" in pd:
            pd = pd[pd.index("freestyle") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "freestyle">')
        elif "order" in pd:
            pd = pd[pd.index("order") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "order">')
        elif "unnamedcodeanimation" in pd:
            pd = pd[pd.index("unnamedcodeanimation") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "unnamedcodeanimation">')
        elif "table" in pd:
            pd = pd[pd.index("table") : ]
            title = pd.split()[1]
            print('    <interactive title = "' + title + '" type = "table">')
        elif "self" not in pd:
            print("?????????" + pd)
            print(lines[1])
                  
        if "self" not in pd:
            location = lines[1]
            if len(location.strip()) == 0 or "http" not in location:
                print("??????Empty location or no location: " + pd)
            location = location.replace('&', '&amp;')
            print('        <location>' + location + '</location>\n' +                
                  '        <shortdescription>vendor</shortdescription>\n'
                  '        <longdescription>vendor</longdescription>\n' +
                  '    </interactive>')
            
        i = text.index("<PD")
 
    output.close()
main() # Call the main function