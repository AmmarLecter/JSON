import os
import shutil


readFile = open(r"/Users/ammarsami/Desktop/ring/Ammar/"+ "data.txt", "r")
for line in readFile:
    line_array = line.split(".")
    del line_array[2]
    print(line_array)
    print(line_array[0])
    
    path_to = r"/Users/ammarsami/Desktop/Data/"+ str(line_array[0])           
  
    if not os.path.exists(path_to):
        
            os.makedirs(path_to)
            path_from = r"/Users/ammarsami/Data/folder_3/"+ str(line_array[0])+"/"+ str(line_array[1])
            shutil.move(path_from, path_to)
           
            path_yes = r"/Users/ammarsami/Desktop/Data" 
            file = open(path_yes +"/"+ "Found.txt", "a")
            file.write(str(line_array[0])+"."+str(line_array[1]) +"\n")
            file.close()
            
readFile.close()
