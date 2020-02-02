####################################################
#### Delete all files but the last one on a ########
#### given dropbox path.                    ########
#### Uses dropbox.conf json file for        ########
#### configuration.                         ########
#### Version 1.0 by Javier Roques           ########
####################################################
# Requirements:
# 1. Dropbox -  pip install dropbox
# 2. Create a Dropbox App to get access token
# 3. Configuration file should be om the same working directory
# 4. Prooperties needed: TOKEN, PATH
####################################################
##Import modules
import sys
import dropbox
import os 
import json

# Declare global variables
TOKEN = ""
PATH  = ""

# Check if the configuration file exits and extract values.
# Throw an error and exit if parameters are missing
if os.path.exists('./dropbox.conf'):
    with open('./dropbox.conf') as config_file:
        config = json.load(config_file)
        print(config)
        TOKEN = config['token']
        PATH = config['path']
        if (len(TOKEN)<1 or len(PATH)<1):
            sys.exit("ERROR: Check configuration file.  Some parameters are missing")
else:
    sys.exit("Error: Configuration file not found") 

     
dbx = dropbox.Dropbox(TOKEN)

# Print files list to terminal - Not in use for deletion
def printFiles(fpath =""):
    response = dbx.files_list_folder(fpath)
    files = response.entries
    filescount = len(files)
    if filescount > 1:
        for i in range (0, filescount-1):
            print(files[i].path_display)

    print("done")

# Delete all file but one
def deleteFiles(fpath =""):
    try:
        response = dbx.files_list_folder(fpath)
        files = response.entries
        filescount = len(files)
        if filescount > 1:
            for i in range (0, filescount-1):
                print(files[i].path_display)
                print(dbx.files_delete(files[i].path_display))
        print("done")
    
    except dropbox.exceptions.ApiError as err:
        print(("Dropbox API error: {0}".format(err)))

def main():
    deleteFiles(PATH)

if __name__ == "__main__":
    main()



