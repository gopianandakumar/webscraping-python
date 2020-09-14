import os

import shutil

#step1
try:
  os.mkdir('Images')

except:
    pass;

try:
  os.mkdir('Docs')

except:
    pass;

try:
  os.mkdir('Videos')

except:
    pass;


try:
  os.mkdir('Music')

except:
    pass;

try:
  os.mkdir('Zip')

except:
    pass;

try:
  os.mkdir('JavaPrograms')

except:
    pass;

try:
  os.mkdir('PythonPrograms')

except:
    pass;

try:
  os.mkdir('HTMLPrograms')

except:
    pass;

try:
  os.mkdir('JavaScriptsprograms')

except:
    pass;
#print(os.listdir())

for file in os.listdir():
    if '.jpg' in file or '.png' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'Images')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.pdf' in file or '.txt' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'Docs')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.mp4' in file or '.mkv' in file :
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'Videos')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.zip' in file or '.rar' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'Zip')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass
                             

for file in os.listdir():
    if '.mp3' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'Music')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.java' in file or '.class' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'JavaPrograms')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.py' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'PythonPrograms')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass

for file in os.listdir():
    if '.html' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'HTMLPrograms')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass
                      
for file in os.listdir():
    if '.js' in file:
       # print(file)

       current_path = os.path.join( os.getcwd(),file)
       print(current_path)
       dest_path= os.path.join(os.getcwd(),'JavaScriptsprograms')
       print(dest_path)
       try:
           shutil.move(current_path,dest_path)
       except:
           pass
                     
