from inspect import getfile
try:
    getfile = open("myfile", "w")
    getfile.write("My file for exception handling")
except IOError:
    print("unable to open or read the data in file")
except: 
    print("Some other error occured")
else:
    print("The file was written successfully")
finally:
    if "getfile" in locals() and not getfile.close:
        getfile.close()
        print("File is now closed")
    print("Finally executed")