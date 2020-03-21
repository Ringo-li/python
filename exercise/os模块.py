import os
 
print (os.sep)
print (os.name)
print (os.getenv('path'))
print (os.getcwd())

os.system('ls -l')
os.system('cat *.txt')
#os.system('ls -l | awk  -F '{print $2}'')