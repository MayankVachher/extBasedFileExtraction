import os
import shutil 

def extractor5000():
    # Set the directory you want to start from
    rootDir = './spark-master'
    # Set the directory you want to gather files to
    copyDir = './datacollection'
    # Set the file extension you want to search for
    ext = ".java"
    
    count = 1
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname.endswith(ext):
            	srcFile = os.path.join(dirName, fname)
            	if os.path.exists(os.path.join(copyDir, fname)):
            		fname = fname.rstrip(ext)+"(1)"+ext
            	dstFile = os.path.join(copyDir, fname)	
            	print str(count)+". Copying File "+srcFile+" as "+dstFile+" ..."
            	shutil.copy2(srcFile, dstFile)
            	count += 1

if __name__ == '__main__':
    extractor5000()
