import zipfile  #Library used for password encrpted zipped folder/file
import time

folderpath = input('Path to the file: ') #Get the target file path and name from the user
zipf = zipfile.zipFile(folderpath) #Initialize a PdfFileReader object

if not zipf:  #Checks if  the file is password encrypted
    prit('The zipped file/folder is not password! You can successfully open it!') #Notifies if the password is not protected

else:
    starttime = time.time() #save the start time
    result = 0 #Initialize a variable result with zero/ 'o' will indicate Failure, while '1' will indicate Success
    c = 0 #Initialize a variable c to keep the count of passwords tried

#Build a character array including all the numbers,lowercase letter, uppercase letters, and special characters.
characters =['0','1','2','3','4','5','6','7','8','9',
            'a','b','c','d','e','f','g','h','i','j','l','k', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z'
            'A','B','C','D','E','F','G','H','I','J','L','K', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

print("Brute Force Started...")

#Finally, if the password is not found even after applying all possible combination of characters upto 4 characters, notify the user as below else 
if (result == 0):
    print("Sorry, password not found. A  total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters."))
else:
    duration = endtime - starttime
    print('Congratulations!!! Password found after trying '+str(c)' combinations in '+str(durations)+' seconds')