import glob
#glob.glob("c:\FOLDER\*.log")
list_of_files = glob.glob("c:\\FOLDER\*.log")
#print(list_of_files)

for file_name in list_of_files:
    #print(file_name)
    with open(file_name) as file_n:
        for line1 in file_n:
            #line1 = str.strip(line1)
            if "ip address" in line1:
                if "no" not in line1:
                    #line2 = str.strip(line1)
                    #print(line2)
                    line3 = line1.replace("ip address", "")
                    line4 = str.strip(line3)
                    print (line4)

#import os
#os.listdir("c:\FOLDER")



