import os
os.chdir('C:\\Users\\goat\\Desktop\\309_data')
os.getcwd()

with open("data/20170405twitterdirty.txt", "r") as fin, open("data/cleaned_twitter.txt", "w") as fou:
    Dirty_Twitter_fields_list = []

    for line in fin:

        if line.startswith("#"):  # skip it if the line begins with a #
            continue

        line = line.lower()     # convert to lower case
        line = line.strip()     # remove leading/trailing blanks

        print(line)

        Dirty_Twitter_fields_list.append(line)  # add the cleaned item to the list

print(Dirty_Twitter_fields_list)
