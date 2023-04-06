# PyFileString
For effortless and lightweight file string processing, developed using python's inbuilt libraries and PySimpleGUI, implemented python functions to process string inside a text file by getting inputs from a config file.

By - Santhosh T

Packages used: configparser, os, shutil, datetime, PySimpleGUI

1. Terminal execution:

   run fileOperationsTerminal.py --> Provide the path of both text file and config file
   
   Example:
   
   Enter the path to text file: 
   C:/Users/tsanthos/Desktop/fileOperations/files/sample_text.txt
   
   Enter the path to config file: 
   C:/Users/tsanthos/Desktop/fileOperations/projectconfigs/fsif_and_number_of_occurences_and_nth_line.ini

   Config files must be in ".ini" format.

2. GUI execution:

   Package used for GUI: PySimpleGUI

   run fileOperationsGUI.py --> Select the files through the explorer and click on "Start"


Additional functionality:

For operations that involves replacement of string, a backup functionality is implemented to prevent loss of information. The input text file will be copied to a folder named "Backup_<DateTime>" which will be created under the execution path.

Note : The functions are performed based on the config file's section header. The header must be any one of the following:

       1.  FSIF and print first n occurrences
       2.  FSIF and print last n occurrences
       3.  FSIF and its nth occurrence including all occurence and print the line number and contents
       4.  FSIF and number of occurrences
       5.  FSIF and print and store x lines above and y lines below
       6.  FSIF and replace only if n lines above matches
       7.  FSIF and replace all occurrences
       8.  FSIF and replace only if n lines below matches
       9.  FSIF and replace only if n lines above and m lines below matches
       10. FSIF and replace nth line with another string after the match
       11. FSIF and replace nth line with another string before the match
       12. FSIF and replace nth occurrence at a line number

