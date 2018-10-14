# coding=utf-8
# This code cleans up dirty twitter fields and drops any with whitespace within the string or if a comma is present
# with open("20170405twitterdirty.txt", "r") as thefile: # You can ignore this, but this opens the file to read.
with open("20170405twitterdirty.txt", "r") as thefile: # You can ignore this, but this opens the file to read.
    # Initializing all variables used in the program at this sub block for easy identification
    Dirty_Twitter_fields_list = [] # List used to keep track of clean URLs after preprocessing from the file.
    removed_strings = [] # List used to track what items were removed.
    no_duplicate_dictionary = {} # Dictionary used to store only one copy of a URL as a key and then converted to a non_duplicated list.
    count_of_added_entries = 0
    count_of_removed_entries = 0
    idx = 0 # Counter used in helping iterate over every other word's every other character.
    length_over_twenty = 0
    error_check = True # Holds true unless the list contains an error in the format.

# This for loop performs checks of each line of the file and either cleans it up or does not add the line to the new list which effectivly removes it.

    for line in thefile: # Answer to number 5 falls withon all the if statement below.
        line = line.strip()  # This removes whitespace before and after the line being brought in as a string.
        line = line.lower()  # This converts all the incoming line to lowercase text.
        if "map" in line or "zoo" in line:
            print("Hey I found map or zoo in", line)
        if not line.strip():  # This ignores the blank lines in the file so they are not appended.
            count_of_removed_entries += 1
            removed_strings.append(line)
            continue  # We continue to the next line as nothing is here to save.
        else:
            if ' ' in line: # This statement looks for a single whitespace within the string. Since strings are like a list of characters. See use of the in operator PY4E 6.7
                count_of_removed_entries += 1
                removed_strings.append(line)
                continue
#                print("OMG I Found a Space!", line)    #TODO on for fun - figure out how to split on comma and add the additional entries for the values split and cleaned. name, @something, another name In this program we just drop these.
            # The following block checks if the url is https://twitter.com not http://www.twitter.com
            elif line.startswith("http://www."):
                Dirty_Twitter_fields_list.append('https://'+line[11:])  # This adds a string to the Dirty_Twitter_fields_list list.
            # The following block checks if the url is https://twitter.com not https://www.twitter.com.
            elif line.startswith("https://www."):
                Dirty_Twitter_fields_list.append('https://'+line[12:])  # This adds a string to the Dirty_Twitter_fields_list list.
            # The following block checks if the url exists.
            elif line.startswith("http"):
                Dirty_Twitter_fields_list.append(line)  # This adds a string to thelist.
            # The following block remove hashtags.
            elif line.startswith("#"):  # Answer to number 3
                count_of_removed_entries += 1
                removed_strings.append(line)
                continue  # This continue skips adding the line to the Dirty_Twitter_fields_list list.
            # The following block remove @ symbols.
            elif line.startswith("@"):
                Dirty_Twitter_fields_list.append('https://twitter.com/'+line[1:])  # This adds a string to the Dirty_Twitter_fields_list list without the @ since it is the first charcter.
            #ensure text not starting with http is converted to url
            else:
                Dirty_Twitter_fields_list.append('https://twitter.com/'+line)  # This adds a string to the Dirty_Twitter_fields_list list.

    Dirty_Twitter_fields_list.sort()

    # This for look looks through the list to create a non duplicate dictionary.
    for entries in Dirty_Twitter_fields_list:
        if (entries in no_duplicate_dictionary) != entries:
            no_duplicate_dictionary[entries] = "added"
            count_of_added_entries += 1

    no_duplicate_list = list(no_duplicate_dictionary)
    no_duplicate_list.sort()


    for word in no_duplicate_list:
#        print(word, "these are clean")  # Answer to number 7 with text
        print(word)  # Answer to number 7 without text
        if not word.startswith("https://twitter.com/"):
            error_check = False
        if len(word) > 20:
            length_over_twenty += 1
    if error_check == True:
        print("All strings are correct")  # Answer to number 6
    else:
        print("Houston we have a problem!")

    print("The number of urls over 20 characters is", length_over_twenty) # This is the answer to number 8

    # Iterates through the no_duplcate_list to find every other word and of that word every other character.
    for word in no_duplicate_list:
        if idx == 0:
            charater_key = 0
            for letter in word:  # Loops through the characters in the string stored in the value of nodup. Answer to numbre 11 part 1
                if charater_key == 0:
                    print(letter)
                charater_key += 1
        elif idx > 0 and idx%2 == 1:  # Looks for odd entries in the list.
            charater_key = 0
            for letter in word:  # Loops through the characters in the string stored in the value of nodup. Answer to numbre 11 part 2
                if charater_key == 0:
                    print(letter)
                elif charater_key > 0 and charater_key%2 == 0:
                    print(letter)
                charater_key += 1
            print(word)


        idx += 1
    print("number of removed entries are", count_of_removed_entries) # Answer to number 10
    print("the removed strings were", removed_strings)