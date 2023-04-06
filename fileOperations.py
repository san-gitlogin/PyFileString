from cmath import e
from logging import exception
from sys import flags
import time
import re


class fileOperations:
    
    """
    FSIF - Find String Inside a File
    """

    def __init__(self):
        filePath = None
        searchString = None
    
    def fsif_and_number_of_occurences(self,filePath,searchString,caseSensitive):
        """
        This Object finds the total occurence of the provided string inside the file using builtin count() method.
        It returns a list containing dict items such as execution time and total occurence.
        
        Example usage:

        | fsif_and_number_of_occurences | filePath = <String><Path> | searchString = <String> | caseSensitive = <Boolean>
        """
        try:
            fsifList = []
            startTime = time.time()
            with open(filePath,"r",encoding="utf8") as file:
                fileRead = file.read()
                searchStringLower = searchString.lower()
                numOfOccurenceSensitive = fileRead.count(searchString)
                numOfOccurenceInsesitive = fileRead.lower().count(searchStringLower)
                if caseSensitive:
                    fsifList.insert(0,{f'Total Occurence of "{searchString}"':numOfOccurenceSensitive})
                else:
                    fsifList.insert(0,{f'Total Occurence of "{searchStringLower}"':numOfOccurenceInsesitive})
            
            file.close()
            endTime = time.time()
            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            return fsifList

        except Exception as e:
            return e
    
    def fsif_and_first_n_occurences(self,filePath,searchString,caseSensitive,n):
        """
        This Object finds first n occurence of the provided string inside the file using builtin count() method
        and by maintaining a counter based on input n. It returns a list containing dict items such as execution 
        time, total occurence and first n occurences.
        
        Example usage:

        | fsif_and_first_n_occurences | filePath = <String><Path> | searchString = <String> | caseSensitive = <Boolean> | n = <int>
        """
        try:
            fsifList = []
            startTime = time.time()
            with open(filePath,"r",encoding="utf8") as file:
                totalOccurence = 0
                lines = file.readlines()
                for line in lines:
                    count = 0
                    if caseSensitive:
                        if searchString in line:
                            count = line.count(searchString)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            if n > 0:
                                fsifList.append(fsifDict)
                                n = n - count
                    else:
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        if searchStringLower in lineLower:
                            count = lineLower.count(searchStringLower)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            if n > 0:
                                fsifList.append(fsifDict)
                                n = n - count
            file.close()
            endTime = time.time()
            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            fsifList.insert(1,{f'Total Occurence of "{searchString}"':totalOccurence})
            return fsifList

        except Exception as e:
            return e

    def fsif_and_last_n_occurences(self,filePath,searchString,caseSensitive,n):
        """
        This Object finds last n occurence of the provided string inside the file using builtin count() method
        and by maintaining a counter based on input n. It returns a list containing dict items such as execution 
        time, total occurence and last n occurences.
        
        Example usage:

        | fsif_and_last_n_occurences | filePath = <String><Path> | searchString = <String> | caseSensitive = <Boolean> | n = <int>
        """
        try:
            fsifList = []
            lastFsifList = []
            startTime = time.time()
            with open(filePath,"r",encoding="utf8") as file:
                totalOccurence = 0
                lines = file.readlines()
                for line in lines:
                    count = 0
                    if caseSensitive:
                        if searchString in line:
                            count = line.count(searchString)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            fsifList.append(fsifDict)
                            
                    else:
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        if searchStringLower in lineLower:
                            count = lineLower.count(searchStringLower)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            fsifList.append(fsifDict)
            
            for item in fsifList[::-1]:
                if n > 0:
                    lastFsifList.append(item)
                    n = n - item['Count']

            file.close()
            endTime = time.time()
            lastFsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            lastFsifList.insert(1,{f'Total Occurence of "{searchString}"':totalOccurence})
            return lastFsifList

        except Exception as e:
            return e

    
    def fsif_and_replace_all_occurences(self,filePath,searchString,replaceString,caseSensitive):
        """
        This Object finds all occurences of the provided string inside the file using re.sub() method.
        It returns a list containing dict items such as execution time and total occurence replacement.
        
        Example usage:

        | fsif_and_replace_all_occurences | filePath = <String><Path> | searchString = <String> | replaceString = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            with open(filePath,"r+",encoding="utf8") as file:
                fileContent = file.read()
                numOfOccurenceSensitive = fileContent.count(searchString)
                numOfOccurenceInsesitive = fileContent.lower().count(searchStringLower)
                if caseSensitive:
                    replacedFileContent = re.sub(searchString, replaceString, fileContent)
                    file.seek(0)
                    file.write(replacedFileContent)
                    file.truncate()
                    if replacedFileContent != fileContent:
                        fsifList.insert(0,{f"Found occurence of {searchString} and Replace of all {numOfOccurenceSensitive} occurence is success"})

                else:
                    searchStringLower = searchString.lower()
                    replacedFileContent = re.sub(searchStringLower, replaceString, fileContent.lower())
                    file.seek(0)
                    file.write(replacedFileContent)
                    file.truncate()
                    if replacedFileContent != fileContent:
                        fsifList.insert(0,{f"Found occurence of {searchString} and Replace of all {numOfOccurenceInsesitive} occurence is success"})
                        
            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file."})
            
            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            return fsifList

        except Exception as e:
            return e

    def fsif_and_replace_occurence_at_line(self,filePath,searchString,replaceString,occurenceNumber,lineNumber,caseSensitive):
        """
        This Object finds nth occurence of the provided string at a line inside the file using builtin split() and join() methods.
        It returns a list containing dict items such as execution time and occurence replacement.
        
        Example usage:

        | fsif_and_replace_occurence_at_line | filePath = <String><Path> | searchString = <String> | replaceString = <String> | occurenceNumber = <int> | lineNumber = <int> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                if lineNumber <= len(lines):
                    oldLineContent = lines[lineNumber-1]
                    if caseSensitive:
                        
                        arr=lines[lineNumber-1].split(searchString)
                        part1=searchString.join(arr[:occurenceNumber])
                        part2=searchString.join(arr[occurenceNumber:])
                        
                        lines[lineNumber-1] = part1 + replaceString + part2

                        with open(filePath,"w",encoding="utf8") as file:
                            for line in lines:
                                file.write(line)
                        file.close()
                        #Compare with old line, to confirm the replacement
                        with open(filePath,"r",encoding="utf8") as file:
                            if file.readlines()[lineNumber-1] != oldLineContent:
                                fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})

                    else:

                        arr=re.split(searchString,lines[lineNumber-1],flags=re.IGNORECASE)
                        part1=searchString.join(arr[:occurenceNumber])
                        part2=searchString.join(arr[occurenceNumber:])
                        
                        lines[lineNumber-1] = part1 + replaceString + part2
                        
                        with open(filePath,"w",encoding="utf8") as file:
                            for line in lines:
                                file.write(line)
                        file.close()

                        #Compare with old line, to confirm the replacement
                        with open(filePath,"r",encoding="utf8") as file:
                            if file.readlines()[lineNumber-1] != oldLineContent:
                                fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})
                else:
                    return f"File has only {len(lines)} lines. Please check the line number." 
                        
            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file or nth occurence does not exist"})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            return fsifList

        except Exception as e:
            return e


    def fsif_and_number_of_occurences_and_nth_line(self,filePath,searchString,occurenceNumber,caseSensitive):
        """
        This Object finds the nth occurence of the provided string inside the file using builtin count() methods.
        It returns a list containing dict items such as execution time, line number of nth occurence, the corresponding line contents
        and total occurence.
        
        Example usage:

        | fsif_and_number_of_occurences_and_nth_line | filePath = <String><Path> | searchString = <String> | occurenceNumber = <int> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()

            with open(filePath,"r",encoding="utf8") as fileForTotalCount:
                fileRead = fileForTotalCount.read()
                searchStringLower = searchString.lower()
                numOfOccurenceSensitive = fileRead.count(searchString)
                numOfOccurenceInsesitive = fileRead.lower().count(searchStringLower)
                if caseSensitive:
                    fsifList.insert(0,{f'Total Occurence of "{searchString}"':numOfOccurenceSensitive})
                else:
                    fsifList.insert(0,{f'Total Occurence of "{searchStringLower}"':numOfOccurenceInsesitive})
            
            with open(filePath,"r",encoding="utf8") as file:
                
                
                lines = file.readlines()
                totalOccurence = 0
                
                for line in lines:
                    count = 0
                    if caseSensitive:
                        if searchString in line:
                            count = line.count(searchString)
                            
                            if (count+totalOccurence) >= occurenceNumber:
                                fsifList.insert(0,{f"Found nth occurence of {searchString} at line number {lines.index(line)+1}"})
                                fsifList.insert(1,{f"Content : {line}"})
                                break
                            else:
                                totalOccurence = totalOccurence + count
                            
                    else:
                        
                        searchStringLower = searchString.lower()

                        lineLower = line.lower()
                        if searchStringLower in lineLower:
                            count = lineLower.count(searchStringLower)
                            
                            if (count+totalOccurence) >= occurenceNumber:
                                fsifList.insert(0,{f"Found nth occurence of {searchString} at line number {lines.index(line)+1}"})
                                fsifList.insert(1,{f"Content : {line}"})
                                break
                            else:
                                totalOccurence = totalOccurence + count

            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file or nth occurence does not exist"})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            
            return fsifList

        except Exception as e:
            return e
  
    
    def fsif_and_print_store_xy_lines(self,filePath,searchString,xLinesCount,yLinesCount,caseSensitive):
        """
        This Object finds the occurence of the provided string inside the file using builtin methods. Each line is iterated
        through readlines() mehtod and when string is found, x<int> lines above and y<int> lines below the occurence are stored
        in a list. It then returns a list containing dict items such as execution time, line number of nth occurence, contents of
        x lines above and contents of y lines below.
        
        Example usage:

        | fsif_and_print_store_xy_lines | filePath = <String><Path> | searchString = <String> | xLinesCount = <int> | yLinesCount = <int> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            xLines = []
            yLines = []
            startTime = time.time()

            with open(filePath,"r",encoding="utf8") as file:
                
                lines = file.readlines()
                
                for line in lines:

                    if caseSensitive:
                        if searchString in line:
                            lineOfOccurence = lines.index(line)+1
                            #String[:start before which index][start index][upto index]
                            xLines.append(lines[:lineOfOccurence][(lineOfOccurence-xLinesCount)-1:lineOfOccurence-1])
                            yLines.append(lines[lineOfOccurence:][(yLinesCount-1)::-1][::-1])

                            fsifList.insert(0,{f"Found occurence of {searchString} at line number {lines.index(line)+1}"})
                            fsifList.insert(1,{f"x lines above: {xLines}"})
                            fsifList.insert(2,{f"y lines below: {yLines}"})
                            break

                    else:
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        if searchStringLower in lineLower:
                            lineOfOccurence = lines.index(line)+1
                            #String[:start before which index][start index][upto index]
                            xLines.append(lines[:lineOfOccurence][(lineOfOccurence-xLinesCount)-1:lineOfOccurence-1])
                            yLines.append(lines[lineOfOccurence:][(yLinesCount-1)::-1][::-1])

                            fsifList.insert(0,{f"Found occurence of {searchString} at line number {lines.index(line)+1}"})
                            fsifList.insert(1,{f"x lines above: {xLines}"})
                            fsifList.insert(2,{f"y lines below: {yLines}"})
                            break

            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file."})
            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            
            return fsifList

        except Exception as e:
            return e
  

    def fsif_and_replace_above_line_match(self,filePath,searchString,replaceString,aboveLineContent,caseSensitive):
        """
        This Object finds the occurence of the provided string inside the file using builtin methods and replaces the search string
        only if the contents of the line above the occurence contains the aboveLineContent<String>. It then returns a list containing
        dict items such as execution time and replace status. 
        
        Example usage:

        | fsif_and_replace_above_line_match | filePath = <String><Path> | searchString = <String> | replaceString = <String> | aboveLineContent = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            #occurenceNumber is 1 since we are replacing the first occurence of search element that we find in the line
            occurenceNumber = 1
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                
                for line in lines:

                    if caseSensitive:
                        if searchString in line:
                            if aboveLineContent in lines[lines.index(line)-1]:
                                arr=lines[lines.index(line)].split(searchString)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()

                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break
                            
                    else:
                        
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        aboveLineContentLower = aboveLineContent.lower()
                        if searchStringLower in lineLower:
                            if aboveLineContentLower in lines[lines.index(line)-1].lower():
                                arr=re.split(searchString,lines[lines.index(line)],flags=re.IGNORECASE)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()
                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break                    

            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file or the line above does not match the given data."})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})

            return fsifList

        except Exception as e:
            return e


    def fsif_and_replace_below_line_match(self,filePath,searchString,replaceString,belowLineContent,caseSensitive):
        """
        This Object finds the occurence of the provided string inside the file using builtin methods and replaces the search string
        only if the contents of the line below the occurence contains the belowLineContent<String>. It then returns a list containing
        dict items such as execution time and replace status. 
        
        Example usage:

        | fsif_and_replace_below_line_match | filePath = <String><Path> | searchString = <String> | replaceString = <String> | belowLineContent = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            #occurenceNumber is 1 since we are replacing the first occurence of search element that we find in the line
            occurenceNumber = 1
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                
                for line in lines:

                    if caseSensitive:
                        if searchString in line:
                            if belowLineContent in lines[lines.index(line)+1]:
                                arr=lines[lines.index(line)].split(searchString)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()

                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break
                            
                    else:
                        
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        belowLineContentLower = belowLineContent.lower()
                        if searchStringLower in lineLower:
                            if belowLineContentLower in lines[lines.index(line)+1].lower():
                                arr=re.split(searchString,lines[lines.index(line)],flags=re.IGNORECASE)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()
                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break                    

            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file or the line below does not match the given data."})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})

            return fsifList

        except Exception as e:
            return e

    def fsif_and_replace_n_and_m_line_match(self,filePath,searchString,replaceString,aboveLineContent,belowLineContent,caseSensitive):
        """
        This Object finds the occurence of the provided string inside the file using builtin methods and replaces the search string
        only if the contents of the line above and below the occurence contains the aboveLineContent<String> and belowLineContent<String>.
        It then returns a list containing dict items such as execution time and replace status. 
        
        Example usage:

        | fsif_and_replace_n_and_m_line_match | filePath = <String><Path> | searchString = <String> | replaceString = <String> | aboveLineContent = <String> | belowLineContent = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            #occurenceNumber is 1 since we are replacing the first occurence of search element that we find in the line
            occurenceNumber = 1
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                
                for line in lines:

                    if caseSensitive:
                        if searchString in line:
                            if aboveLineContent in lines[lines.index(line)-1] and belowLineContent in lines[lines.index(line)+1]:
                                arr=lines[lines.index(line)].split(searchString)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()

                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break
                            
                    else:
                        
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        belowLineContentLower = belowLineContent.lower()
                        aboveLineContentLower = aboveLineContent.lower()
                        if searchStringLower in lineLower:
                            if aboveLineContentLower in lines[lines.index(line)-1].lower() and belowLineContentLower in lines[lines.index(line)+1].lower():
                                arr=re.split(searchString,lines[lines.index(line)],flags=re.IGNORECASE)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lines.index(line)] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()
                                fsifList.insert(0,{f"Found occurence of {searchString} and Replace Success"})
                                break                    

            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in file or the line above or below does not match the given data."})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})

            return fsifList

        except Exception as e:
            return e

    def fsif_and_replace_nth_above_line_match(self,filePath,lineNumber,searchString,replaceString,aboveLineContent,caseSensitive):
        """
        This Object finds the occurence of the provided string at a line number inside the file using builtin methods and replaces the occurence
        only if the contents of the line above contains the aboveLineContent<String>. It then returns a list containing dict items such as execution
        time, occurence line number and replace status. 
        
        Example usage:

        | fsif_and_replace_nth_above_line_match | filePath = <String><Path> | lineNumber = <int> | searchString = <String> | replaceString = <String> | aboveLineContent = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            #occurenceNumber is 1 since we are replacing the first occurence of search element that we find in the line
            occurenceNumber = 1
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                if lineNumber <= len(lines):
                    oldLineContent = lines[lineNumber-1]
                    if caseSensitive:
                        if aboveLineContent in lines[lineNumber-2]:
                            if searchString in lines[lineNumber-1]:
                                arr=lines[lineNumber-1].split(searchString)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lineNumber-1] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()
                                #Compare with old line, to confirm the replacement
                                with open(filePath,"r",encoding="utf8") as file:
                                    if file.readlines()[lineNumber-1] != oldLineContent:
                                        fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})

                    else:
                        if aboveLineContent.lower() in lines[lineNumber-2].lower():
                            if searchString.lower() in lines[lineNumber-1].lower():
                                arr=re.split(searchString,lines[lineNumber-1],flags=re.IGNORECASE)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lineNumber-1] = part1 + replaceString + part2
                        
                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()

                                #Compare with old line, to confirm the replacement
                                with open(filePath,"r",encoding="utf8") as file:
                                    if file.readlines()[lineNumber-1] != oldLineContent:
                                        fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})
                else:
                    return f"File has only {len(lines)} lines. Please check the line number." 
                        
            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in line or above line content does not match"})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            return fsifList

        except Exception as e:
            return e


    def fsif_and_replace_nth_below_line_match(self,filePath,lineNumber,searchString,replaceString,belowLineContent,caseSensitive):
        """
        This Object finds the occurence of the provided string at a line number inside the file using builtin methods and replaces the occurence
        only if the contents of the line below contains the belowLineContent<String>. It then returns a list containing dict items such as execution
        time, occurence line number and replace status. 
        
        Example usage:

        | fsif_and_replace_nth_below_line_match | filePath = <String><Path> | lineNumber = <int> | searchString = <String> | replaceString = <String> | belowLineContent = <String> | caseSensitive = <Boolean> |
        """
        try:
            fsifList = []
            startTime = time.time()
            #occurenceNumber is 1 since we are replacing the first occurence of search element that we find in the line
            occurenceNumber = 1
            with open(filePath,"r",encoding="utf8") as file:
                lines = file.readlines()
                if lineNumber <= len(lines):
                    oldLineContent = lines[lineNumber-1]
                    if caseSensitive:
                        if belowLineContent in lines[lineNumber]:
                            if searchString in lines[lineNumber-1]:
                                arr=lines[lineNumber-1].split(searchString)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lineNumber-1] = part1 + replaceString + part2

                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()
                                #Compare with old line, to confirm the replacement
                                with open(filePath,"r",encoding="utf8") as file:
                                    if file.readlines()[lineNumber-1] != oldLineContent:
                                        fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})

                    else:
                        if belowLineContent.lower() in lines[lineNumber].lower():
                            if searchString.lower() in lines[lineNumber-1].lower():
                                arr=re.split(searchString,lines[lineNumber-1],flags=re.IGNORECASE)
                                part1=searchString.join(arr[:occurenceNumber])
                                part2=searchString.join(arr[occurenceNumber:])
                        
                                lines[lineNumber-1] = part1 + replaceString + part2
                        
                                with open(filePath,"w",encoding="utf8") as file:
                                    for line in lines:
                                        file.write(line)
                                file.close()

                                #Compare with old line, to confirm the replacement
                                with open(filePath,"r",encoding="utf8") as file:
                                    if file.readlines()[lineNumber-1] != oldLineContent:
                                        fsifList.insert(0,{f"Found occurence of {searchString} at line number {lineNumber} and Replace of nth occurence is success"})
                else:
                    return f"File has only {len(lines)} lines. Please check the line number." 
                        
            file.close()
            endTime = time.time()
            if len(fsifList)==0:
                fsifList.insert(0,{f"{searchString} - not found in line or below line content does not match"})

            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            return fsifList

        except Exception as e:
            return e


    def fsif_and_number_of_occurences_extended(self,filePath,searchString,caseSensitive):

        try:
            fsifList = []
            startTime = time.time()
            with open(filePath,"r",encoding="utf8") as file:
                totalOccurence = 0
                lines = file.readlines()
                for line in lines:
                    count = 0
                    if caseSensitive:
                        if searchString in line:
                            count = line.count(searchString)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            fsifList.append(fsifDict)
                    else:
                        searchStringLower = searchString.lower()
                        lineLower = line.lower()
                        if searchStringLower in lineLower:
                            count = lineLower.count(searchStringLower)
                            totalOccurence = totalOccurence + count
                            fsifDict = {'Line number':lines.index(line),'Line':line,'Count':count}
                            fsifList.append(fsifDict)
            file.close()
            endTime = time.time()
            fsifList.insert(0,{'Execution Time in seconds' : "{:.2f}".format(endTime - startTime)})
            fsifList.insert(1,{f'Total Occurence of "{searchString}"':totalOccurence})
            return fsifList

        except Exception as e:
            return e

        
