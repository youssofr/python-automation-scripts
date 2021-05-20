"""
This script counts the number of pages in all pdf files contained in the directory in which the script is run.
And outputs the file names, respective page counts, and total page count to the terminal as well as to a .txt file.
"""
import glob
import PyPDF2 as pdf

file_names = glob.glob('*.pdf')

output_file = open('Pages Count.txt', 'w')
total_num_pages = 0
for i,file in enumerate(file_names):
    n = pdf.PdfFileReader(file).getNumPages() - 2
    line = str(i+1) + ': ' + file + ' : ' + str(n)
    print(line)
    output_file.write(line+'\n')
    total_num_pages += n
    
print(total_num_pages)
output_file.write(str(total_num_pages))
output_file.close()