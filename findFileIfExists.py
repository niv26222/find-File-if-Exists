import os

#Path IN which we have to search file
PATH = 'D:\DOC\Python\fileName' #Give your path here
def searchFile(fileName):
    for root, dirs, files in os.walk(PATH):
        print('Looking in:', root)
        for Files in files:
            try:
                #Returns -1 if NOT found else returns index
                found = Files.file(fileName)
                # print(found)
                if found != -1:
                    print(fileName, 'Found')
                    break
            except:
                exit()
if __name__ == '__main__':
    searchFile('someDoc.pdf') #File Name

# =========== End ==================                            