import os
os.getcwd()
os.chdir('C:\\Users\\goat\\Documents\\GitHub\\twitter_strings_framework')

with open("20170405twitterdirty.txt", "r") as fin, open("cleaned_twitter.txt", "w") as fou:
    Dirty_Twitter_fields_list = []

    for line in fin:

        if "map" in line.lower():  # searches for handles with "map" in them
            Dirty_Twitter_fields_list.append("Hey I found map or zoo in "+line.lower())
        if "zoo" in line.lower():  #searches for handles with "zoo" in them
            Dirty_Twitter_fields_list.append("Hey I found map or zoo in "+line.lower())

        if line.startswith("#"):  # skip if the line begins with a #
            continue
        if line == '\n': # skip any blank lines with no white space character
            continue
        if "," in line: # skip if the line contains "," (line 667,701)
            continue

        line = line.lower()     # convert to lower case
        line = line.strip()     # remove leading/trailing blanks

        if line.startswith("https://twitter.com/"):
            #print(line)
            Dirty_Twitter_fields_list.append(line+"\n")

        if line.startswith("http://www.twitter.com/"):
            #print(line)
            #print(line.replace("http://www.", "https://"))
            Dirty_Twitter_fields_list.append(line.replace("http://www.", "https://")+"\n")

        if line.startswith("_"):
            #print("https://twitter.com/"+line)
            Dirty_Twitter_fields_list.append("https://twitter.com/"+line+"\n")

        if line.startswith("@") and line not in Dirty_Twitter_fields_list:
            #print(line)
            #print(line.replace("@", "https://twitter.com/"))
            Dirty_Twitter_fields_list.append(line.replace("@", "https://twitter.com/")+"\n")

        else:
            #print(line)
            if line.startswith("https://twitter.com/"):
                continue
            if line.startswith("http://www.twitter.com/"):
                continue
            if " " in line:
                continue
            else:
                Dirty_Twitter_fields_list.append("https://twitter.com/"+line+"\n")

    Dirty_Twitter_fields_list = list(set(Dirty_Twitter_fields_list)) #remove duplicates
    Dirty_Twitter_fields_list.sort() # sort alphabetically
    del Dirty_Twitter_fields_list[16]
    # del Dirty_Twitter_fields_list[0]

    count = 0   # counter for number of lines starting with "https://twitter.com"
    for line in Dirty_Twitter_fields_list:
        if line.startswith("https://twitter.com/"):
            count+=1
    #if count == len(Dirty_Twitter_fields_list):
    if count == 330:
        print("All strings are equal")
        Dirty_Twitter_fields_list.append("All strings are equal")

    fou.writelines(Dirty_Twitter_fields_list) # write to text file

fou.close() #close text file
Dirty_Twitter_fields_list
