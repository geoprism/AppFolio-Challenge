#Brian Wong 9/28/16 Appfolio Interview

import os
from pathlib import Path

def handle_commands():
    """Responds to inputs, execute proper commands."""

    print("Usage: copy SOURCE DESTINATIONS..(followed by a space)")
    print("Type \"quit\" to exit")

    while True:
        response = input().strip().split()

        if response[0].lower() == "quit":
           break;

        if len(response) > 2:
            source = Path(response[1])
            if response[0].lower() != "copy":
                print(response[0] + " is not a valid command")
            if source.is_file() != True:
               print(response[1] +" is not a source file")
            else:
                print("")
                copy_to_des(source, response[2:])
        else:
            print("Not enough input")



def copy_to_des(source: Path, destinations: list):
    """Copies source file to multiple destinations"""
    for destination in destinations:
        if os.path.isdir(destination):
            create_copy(source, destination)
        elif os.access(os.path.dirname(destination), os.W_OK):  #if path does not exist,
            try:                                                #but is valid, make the directory & create a copy
                os.makedirs(destination)
                create_copy(source, destination)
            except:
                print("Unable to access " + destination)
        else:
            print(destination + " is not a valid path")

def create_copy(source: Path, destination: str):
    """Creates copy to destination, handles errors"""
    try:
        des = destination + "/" + str(source).strip().split("/")[-1]
        if os.path.isfile(des):
           raise ValueError 
        with open(str(source),'rb') as sfile:
            source_content = sfile.read()
            with open(des,'wb') as dfile:
                dfile.write(source_content)
                sfile.close()
                dfile.close()
    
        print(str(source).strip().split("/")[-1] + " successfully copied to " + str(destination))

    except ValueError:
           print(str(source).strip().split("/")[-1] + " already exist in " + str(destination))
    except:
        print("Permission Denied")




if __name__ == '__main__':
    handle_commands()
