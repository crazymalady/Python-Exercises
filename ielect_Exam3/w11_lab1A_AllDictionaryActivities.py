#EXAMLAB1A
#Create a database in the following format
#Values: by Lacaste, Jennifer A.

def samp(values):
    database1 ={
        "Routers":
            {
                "keys":
                    {
                        values:
                        {
                            "name": "Router1",
                            "ip": "1.1.1.1",
                            "uname": "zframez",
                            "pword": "zframez"
                        }
                    }
            }
    }

    # Write a python program to check whether the given key is present,
    # if present print the value
    #check:
    holdVal = database1['Routers']['keys'][values]
    if values in holdVal:
        if values == "name":
            print(database1['Routers']['keys'][values]['name'])

        if values == "ip":
            print(database1['Routers']['keys'][values]['ip'])

        if values == "uname":
            print(database1['Routers']['keys'][values]['uname'])

        if values == "pword":
            print(database1['Routers']['keys'][values]['pword'])

    else: #else add a new key and value
        ans = input('You want to add?Y/N')
        print('Message: Sorry not found on dbase!', ans )

        if ans == 'Y' or 'y':
            newKey = input('Enter a new key: ')
            newVal = input('Enter a new key Value: ')

            #changing the name of the key from values to 'values' so that the first val of
            # the var value from the display() will not be displayed on output
            database1['Routers']['keys']['values'] = database1['Routers']['keys'][values] #dict[newvalue] = dict[oldval], old val is equiv to new
            del database1['Routers']['keys'][values] #deleting the oldvalue
            database1['Routers']['keys']['values'][newKey] = newVal #adding a new key
            print('Success!', database1)  #ouputprint

            #count = count + 1  # cnt num of the items inside
            # then append to
            #dir(addKey)

    return

def display():
    key = input('Input key to find: ')
    samp(key)

display()














"""values = ['Router1', '1.1.1.1', 'zframez', 'zframez']
keys = { name, IP, 		(username)	(pwd)}
"""



#val = ['Kelly', 'Emma', 'John']
#key = {"designation":'Application Dev', "salary":8000}

#resDict = dict.fromkeys(employees, defaults)
#print(resDict)



















#4. Initialize dictionary with default values
"""employees = ['Kelly', 'Emma', 'John']
defaults = {"designation":'Application Dev', "salary":8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)

# indiv data
print(resDict["Kelly"])
"""




















#3. Access the value of key ‘history’
#or can import it from other file e.g import sampleDict.py
"""sampleDict ={
 "class":
	{
	  "student":
	   {
	     "name": "Mike",
	     "marks":
	      {
                "physics": 70,
                "history": 80
	      }
	   }
	}

}

print(sampleDict['class']['student']['marks']['history'])

"""




#2.Merge following two Python dictionaries into one
"""dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourthy': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}

print(dict3)"""























"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

sampledic = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}"""

#print(sampledic)
