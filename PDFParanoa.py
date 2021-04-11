import sys
import os
import PyPDF2

foldername=[]
path='/home/kapil/Desktop/folder'

def encypt_Files():
	global foldername,path
	
	for folders,subfolders,files in os.walk(path):
		foldername.append(folders)   # storing folder paths in list
	

	for file_path in foldername:
	
		os.chdir(file_path)  # changing directory path from stored folder paths
		
		for files in os.listdir():
			
			if files.endswith('.pdf'):
				pdfReaderobj=PyPDF2.PdfFileReader(open(files,'rb'))
				pdfWriterobj=PyPDF2.PdfFileWriter()
				
				
				if pdfReaderobj.isEncrypted:
					continue
				else:
					pdfWriterobj.addPage(pdfReaderobj.getPage(0))
					pdfWriterobj.encrypt(sys.argv[1])
					
					resultPdf=open(files.strip('.pdf')+'_encrypted.pdf','wb')
					pdfWriterobj.write(resultPdf)
					resultPdf.close()
					



def decrypt_Files():
	
	for folder,subfolders,files in os.walk('/home/kapil/Desktop/folder'):

		for subfolder in subfolders:
				
			os.chdir(folder)
				
			for files in os.listdir():
				
				
				
				if files.endswith('.pdf'):
					PdfReaderobj=PyPDF2.PdfFileReader(open(files,'rb'))
					
					if PdfReaderobj.isEncrypted:
						if PdfReaderobj.decrypt(sys.argv[1]):
							
							PdfWriterobj=PyPDF2.PdfFileWriter()
							PdfWriterobj.addPage(PdfReaderobj.getPage(0))
							resultPdf=open(os.path.join('/home/kapil/Desktop/folder/decrypted',files.strip('_encrypted.pdf')+'_decrypted.pdf'),'wb')
						
							PdfWriterobj.write(resultPdf)
							resultPdf.close()
						else:
							print('wrong password!!')
							break
						
							
						
					
					
					
					
					
				
encypt_Files()
decrypt_Files()
