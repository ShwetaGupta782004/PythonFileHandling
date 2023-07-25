import os
path=r'D:\Desktop\python_file_handling_practice'
while(True):
    operation=int(input('1.Create\n2.Read\n3.Write\n4.Overwrite\n5.List all files\n6.Remove the file\n7.Multiple files\n8.Rename\n9.Quit\nChoose:::'))
    if (operation==1):
        filename=input('Enter File Name :')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            print('This file is already created')
        else:
            f=open(fr'{path}\{filename}.txt','x')
            print(f'This {filename} is created')
    elif(operation==2):
        filename = input('Enter File Name :')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            f=open(fr'{path}\{filename}.txt','r')
            file_content=f.read()
            f.close()
            print(file_content)
        else:
            print('This file is not in our system')
    elif(operation==3):
        filename = input('Enter File Name :')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            message=input('Enter here :')
            f=open(fr'{path}\{filename}.txt','a')
            f.write(message)
            f.close()
        else:
            print('This file is not in our system')
    elif(operation==4):
        filename = input('Enter File Name :')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            message=input('Enter here :')
            f=open(fr'{path}\{filename}.txt','w')
            f.write(message)
            f.close()
        else:
            print('This file is not in our system')
    elif(operation==5):
        files=os.listdir(fr'{path}')
        print(files)
    elif(operation==6):
        filename=input('What do you want to delete ?')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            os.remove(fr'{path}\{filename}.txt')
            print(f'{filename} is removed from our system')
        else:
            print(f'{filename} does not exist')
    elif(operation==7):
        filenames=input('Enter the filenames seperated by comma:')
        filenames=filenames.split(',')
        for filename in filenames:
            if (os.path.exists(fr'{path}\{filename}.txt')):
                print('This file is already created')
            else:
                f = open(fr'{path}\{filename}.txt', 'x')
                print(f'This {filename} is created')
    elif(operation==8):
        filename=input('Which file do you want to rename ?')
        if(os.path.exists(fr'{path}\{filename}.txt')):
            new_filename=input('New file name')
            os.rename(fr'{path}\{filename}.txt',fr'{path}\{new_filename}.txt')
        else:
            print(f'{filename} is not exist in our system.')
    elif(operation==9):
        break
    else:
        print('Invalid operation')






