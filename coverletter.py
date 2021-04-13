import os
import sys
import fileinput

print ("Enter the company name : ")
newcompany = input( "> " )
print ("Wanna change the Program from Software Internship y/n? : ")
yn = input( "> " )
name = ''
if yn == 'y' or yn == 'Y' :
    print ("Enter new program name : ")
    name = input( "> " )
newfilename = "CoverLetter "+newcompany+".txt"


firstfile = open("CVgenerator.txt",'r')  #replace CVgenerator with the name of your letter
newfile = open( newfilename, 'a' )

for line in firstfile:
    r = line.replace( 'company_name', newcompany)  #replace this with what is TO BE replaced
    if yn == 'y' or yn == 'Y' :
         y = r.replace('Summer Internship', name)   #replace this with what is TO BE replaced for program
         newfile.write(y)
    else :
        newfile.write(r)

newfile.close()
firstfile.close()


