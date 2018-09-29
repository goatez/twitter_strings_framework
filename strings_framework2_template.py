import os
os.chdir('C:\\Users\\goat\\Desktop\\309_data')
os.getcwd()

with open("data/20170405twitterdirty.txt", "r") as fin, open("data/cleaned_twitter.txt", "w") as fou:
    Dirty_Twitter_fields_list = []

    for line in fin:

        if line.startswith("#"):  # skip it if the line begins with a #
            continue
        if line == '\n': # passes blank line with no white space character
            continue
        if line == 'NA': # passes 'NA' entry
            continue
        if "," in line: # passes entry with "," - line 667,701
            #print(line)
            continue

        line = line.lower()     # convert to lower case
        line = line.strip()     # remove leading/trailing blanks

        # line 657 - has period

        if line.startswith("https://twitter.com/"):
            #print(line)
            Dirty_Twitter_fields_list.append(line+"\n")  # add the cleaned item to the list
        if line.startswith("http://www.twitter.com/"):
            #print(line)
            #print(line.replace("http://www.", "https://"))
            Dirty_Twitter_fields_list.append(line.replace("http://www.", "https://")+"\n") # add the cleaned item to the list
        if line.startswith("_"):
            #print("https://twitter.com/"+line)
            Dirty_Twitter_fields_list.append("https://twitter.com/"+line+"\n")

        if line.startswith("@") and line not in Dirty_Twitter_fields_list:
            #print(line)
            #print(line.replace("@", "https://twitter.com/"))
            Dirty_Twitter_fields_list.append(line.replace("@", "https://twitter.com/")+"\n")  # add the cleaned item to the list

    #print(Dirty_Twitter_fields_list)
    Dirty_Twitter_fields_list = list(set(Dirty_Twitter_fields_list)) #remove duplicates
    Dirty_Twitter_fields_list.sort() # sort alphabetically

    fou.writelines(Dirty_Twitter_fields_list) # write to text file
    fou.close() #close text file

Dirty_Twitter_fields_list
