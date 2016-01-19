curr_skills = {"Python": 7, "C": 2, "Java": 7, "Windows_OS_Experience": 5, "Apple_OS/X_Experience": 2, "MS_Office": 7}
needed_skills = {"C#": 3, "asp.net": 1, "Web_Development": 1, "C++": 2, "Linux": 11}

def load_skills(cfile = 'curr_skills.txt', nfile = 'needed_skills.txt'):
    print("Loading...")
    c = open(cfile, 'r')
    n = open(nfile, 'r')
    line_str = c.readline();
    while (line_str != ''):
        str_lst = line_str.strip().split(',')
        curr_skills[str_lst[0]] = int(str_lst[1])
        line_str = c.readline()
    line_str = n.readline()
    while (line_str != ''):
        str_lst = line_str.strip().split(',')
        needed_skills[str_lst[0]] = int(str_lst[1])
        line_str = n.readline()
    print("Loaded!")

def save_skills(cd, nd, cfile = 'curr_skills.txt', nfile = 'needed_skills.txt'):
    c = open(cfile, 'w')
    n = open(nfile, 'w')
    for k in cd:
        c.write(k + "," + str(cd[k]) + "\n")
    for k in nd:
        n.write(k + "," + str(nd[k]) + "\n")

def ord_strs(str1, str2):
    if str1.lower()==str2.lower():
        return 0
    else:
        return r_ord_strs(str1.lower(), str2.lower())

def r_ord_strs(str1, str2):
    if (str1 == ""):
        return 1
    elif (str2 == ""):
        return -1
    elif (ord(str1[0]) < ord(str2[0])):
        return 1
    elif (ord(str1[0]) > ord(str2[0])):
        return -1
    else:
        return r_ord_strs(str1[1:], str2[1:])

def order_dict(d):
    result = []
    print(d.keys())
    for k in d:
        print("key: "+ k)
        ip = [k, d[k]]
        if len(d) == 0:
            result = [ip]
        else:
            i = 0
            done = False
            while (i < len(result) and not done):
                if (ip[1] >= result[i][1]):
                #if (ord_strs(ip[0], result[i][0]) == 1):

                    #out_of_order = (r_ord_strs(ip[0], result[i+1][0]) == -1)
                    #identical = (r_ord_strs(ip[0], result[i+1][0]) == 0)
                    #if (r_ord_strs(ip[0], result[i][0]) == -1) or (r_ord_strs(ip[0], result[i][0]) == 0):
                    #if (ord_strs(ip[0], result[i][0]) == 1) or (ord_strs(ip[0], result[i][0]) == 0) or result[i][1]!=ip[1]:
                        result.insert(i, ip)
                        #print("inserted at " + str(i))
                        done = True
                i += 1
            if done == False:
                result.append(ip)
    return result

def print_skills(d):
    o_lst = order_dict(d)
    for entry in o_lst:
        print(entry[0] + ": " + str(entry[1]))

def add_skills(s, num = 1, d = needed_skills):
    if s not in d: d[s] = num
    else: d[s] += num

def main(first_time = True, c = curr_skills, n = needed_skills):
    if first_time:
       load_skills()
    cd = dict(c)
    nd = dict(n)
    in1 = input()
    print()
    if (in1 == ""):
        print("invalid command")
        main(False, cd, nd)
    if in1 == "close":
        print("CURRENT SKILLS")
        print_skills(cd)
        print("\nNEEDED SKILLS\n")
        print_skills(nd)
        try:
            save_skills(cd, nd)
        except:
            print("Save unsuccessful.\nAttempt 'close' operation again.")
            main(False)
        else:
            print("\nSave successful.")
        finally:
            print("\n\nEND OF SESSION")
    elif (in1[0] in ['c', 'n']):
        try:
            in2 = in1.split()[1]
            in3 = in1.split()[2]
            in1 = in1.split()[0]
        except:
            print("Follow help guidelines for input.")
        else:
            if in1 == "c":
                try:
                    if in2 not in cd:
                        cd[in2] = int(in3)
                    else:
                        cd[in2] += int(in3)
                except:
                    print("Ensure last component of input is an int, and ensure that the entire command is on a single line.")
            elif in1 == "n":
                try:
                    if in2 not in nd: nd[in2] = int(in3)
                    else: nd[in2] += int(in3)
                except:
                    print("Ensure last component of input is an int, and ensure that the entire command is on a single line.")
        main(False, cd, nd)
    elif (in1 == 'help'):
        print("LIST OF COMMANDS:\n\n" +
              "c - save skill to current_skills.\n" +
              "c skill_str num_of_mentions\n\n" +
              "...")
        main(False, cd, nd)
    elif (in1 == 'print'):
        print("CURRENT SKILLS")
        print_skills(cd)
        print("\nNEEDED SKILLS")
        print_skills(nd)
        main(False, cd, nd)
    else:
        if in1 in cd:
            cd[in1] += 1
        elif in1 in nd:
            nd[in1] += 1
        else:
            print("invalid command")
        main(False, cd, nd)

print(order_dict({"C": 1, "B": 2, "A": 3, "BSC": 2, "T": 4, "Rey": 0}))
#main()
