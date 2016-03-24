#!/usr/bin/env python


import os, sys
import re

# Open a file
path = "./data/plainmessages"

len(dirs)

# this regular expression fill match with strings that have only digits followed by a dot and 'msg'
only_msg = re.compile('(\d+).msg')

## function to extract data from message file
def parsemessage(filename):
    ph0 = re.compile("^\(Message")
    ph1 = re.compile("^([\w\-]+):\s+(.*)")
    ph2 = re.compile("^\s(.*)")
    ph3 = re.compile("^part\s+(\d+)\s+text/plain")
    ##ph4 = re.compile("^(\w+) (\w+) from ([\w\s]+)said:")
    ph4 = re.compile("^(\w+) (\w+) from (.+)")
    ph5 = re.compile("^Shared to (\d+) neighborhood")
    ##Shared to your neighborhood
    ph5a = re.compile("^Shared to your neighborhood")
    ph6 = re.compile("^To view")
    
    resdict = {}
    content = ""
    currentkey = ""
    state = "begin"
    blanklines = 0
    error_message = ""
    for line in open(filename):
        
        ##print("'%s' (%s)" % (line.rstrip(), state))
        res0 = ph0.match(line)
        res1 = ph1.match(line)
        res2 = ph2.match(line)
        res3 = ph3.match(line)
        res4 = ph4.match(line)
        res5 = ph5.match(line)
        res5a = ph5a.match(line)
        res6 = ph6.match(line)
        
        if state == "begin":
            if res0:
                state = "inheader"
                continue
            else:
                error_message = "problems in state %s" % state
                state = "error"
       
        if state == "inheader":
            if res1:
                currentkey = res1.group(1)
                resdict[currentkey] = res1.group(2)
                continue
            elif line[0]=='\n':
                continue
            elif line[0]=='\t':
                resdict[currentkey] += line
                continue
            elif res3:
                state = "part"
                continue
            else:
                error_message = "problems in state %s" % state
                state = "error"

        elif state=="part":
            if line[0]=="\n":
                continue
            elif res4:
                resdict["sender_firstname"] = res4.group(1)
                resdict["sender_lastname"] = res4.group(2)
                resdict["sender_neighborhood"] = res4.group(3)
                state = "body"
                continue
            else:
                error_message = "problems in state %s" % state
                state = "error"

        elif state=="body":
            if res5:
                resdict["Num_neighborhoods"] = res5.group(1)
                state = "last"
                continue
            elif res5a:
                resdict["Num_neighborhoods"] = 1
                state = "last"
                continue
            else:
                if "body" in resdict.keys():
                    resdict["body"] += line
                else:
                    resdict["body"] = line
                continue
        elif state=="last":
            if res6:
                state = "done"
                continue
            else:
                if "category" in resdict.keys():
                    resdict["category"] += line.rstrip()
                else:
                    resdict["category"] = line.rstrip()
                continue
        
        elif state=="done":
            break;
            
        else:
            ##print(error_message)
            return resdict
                
    return resdict

# This would print all the files and directories
dirs = os.listdir( path )
for file in dirs[1000:1100]:
    if only_msg.match(file):
        filepath = "%s/%s" % (path, file)
        print(filepath, end="\t")
        res = parsemessage(filepath)
        if ('category' in res.keys()) and (len(res['category']) > 0):
            print(res['category'])
        else:
            print('unknown')
        # print("%s -> %s" % (file, res['category'])


