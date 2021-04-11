# PDFParanoa
it uses PyPDF2 module to encrypt and decrypt PDF Files

Algorithm for Encryption:

1. To traverse and store folder paths in a list.
2. To traverse list of folder paths and change directory by folder paths.
3. Check files present diretory and check if they are PDF or not.
4. If file is PDF then call PDFReaderobj that opens that file in read binary mode.
5. Create PDFwriter object.
6. Check  if file is encrypted or not.
7. If file is encrypted  then go back to step 3 for next file and if not then proceed to step 8.
8. Read the first page in PDF file and add that page to PDFWriter object.
9. Encrypt the PDFWriter obj and pass command line parameter as password for encrypted files.
10. Create the PDF file object in write binary  mode where name of encypted file is file_encrypted.pdf
11. write the PDF file object to PDFWriter object.
12. Close the PDF File object.


Algorithm for Decryption:
1. Traverse through files present in current folder path.
2. Check if the files present are encrypted.
3. If encrypted then decrypt the files with password as command line argument passed.
4. copy the decrypted  files to other folder.
5. If the password is wrong then exit the program with message "Wrong password!!".
