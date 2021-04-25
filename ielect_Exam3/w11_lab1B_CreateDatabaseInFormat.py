# Developed by: Jennifer Lacaste -- Personal Code
# CreatedOn   : 20201208
# Class and Dictionaries, personalized switch statement

class Dictionaries:
    def __init__(self):
        self.dict_Interfaces = {
            "Interfaces":
            {
                # to put multiple values in single key enclosed with square bracket
                "Interface": ['Ethernet0', 'Ethernet1', 'Serial0', 'Serial1'],
                "IP": ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4'],
                "Status": ['up', 'down', 'up', 'up']
            }
        }

class Main:
    def showAll(self):
        DICT1 = Dictionaries().dict_Interfaces["Interfaces"]  # doesn't want outside, only put on local function

        print('Displaying Successful!')

        count = 0  # count the items inside interface
        for interfaceVal in DICT1["Interface"]:
            if count == 0:
                print("\n", "Interface   | ", "IP      | ", "Status")
            if count >= 2:
                print((count+1), interfaceVal, "   | ", DICT1["IP"][count], "| ", DICT1["Status"][count])
            else:
                print((count + 1), interfaceVal, " | ", DICT1["IP"][count], "| ", DICT1["Status"][count])
            count = count + 1

    # Find status of a given interface
    def findStatus(self):
        DICT1_Interfaces = Dictionaries().dict_Interfaces["Interfaces"]

        # display the available interface first
        print('Option Selected: FIND STATUS')
        print('List of Interfaces: ')
        count = 0
        for interfaces in DICT1_Interfaces["Interface"]:
            print("  ", (count + 1), "  ", interfaces)
            count = count + 1

        try:
            # ask for interface input
            interface = int(input('Enter Interface: '))
            if interface >= 5:
                print('Sorry Out of range!, Please run again the program.')
            else:
                print(DICT1_Interfaces["Interface"][interface-1], "'s Status: ", end=" ")
                print(DICT1_Interfaces["Status"][interface-1])  # -1 becoz index starts at '0'
        except:
            print('\nERROR OCCURED: Please Input the Interface ID; e.g 1 -> Ethernet0')
            print('Kindly run again the program.')

    # Find Interface and IP of a given status "up" BUT I MAKE IT USER INPUT
    def findInterfaceAndIP(self):
        DICT1_Interfaces = Dictionaries().dict_Interfaces["Interfaces"]

        # ask for status
        status = input('Enter Status (up or down): ').lower()

        count = 0
        print('Showing Interfaces and IP with [', status, "] status")
        print("   ", "Interface   ", "   IP   ")
        print("   ", "------------", "--------")
        for stat in DICT1_Interfaces["Interface"]:
            if DICT1_Interfaces["Status"][count].__contains__(status):
                if DICT1_Interfaces["Interface"][count].__contains__('Ethernet'):
                    print("   ", DICT1_Interfaces["Interface"][count], "|  ", DICT1_Interfaces["IP"][count])

                if DICT1_Interfaces["Interface"][count].__contains__('Serial'):
                    print("   ", DICT1_Interfaces["Interface"][count], "  |  ", DICT1_Interfaces["IP"][count])
            count = count + 1

    # Count Ethernet Interfaces, BUT I DID USER INPUT TO WHAT INTERFACE TO COUNT
    def countInterfaces(self):
        DICT1_Interfaces = Dictionaries().dict_Interfaces["Interfaces"]

        print('Available Interfaces: Ethernet & Serial')

        # ask for what interface to count
        interface2Count = input('Enter Interface to Count: ')

        ctr = 0
        store = 0
        for interface in DICT1_Interfaces["Interface"]:
            if DICT1_Interfaces["Interface"][ctr].lower().__contains__(interface2Count.lower()):
                store = store + 1
            ctr = ctr + 1
        print('Result: \nThere are ', store, " [", interface2Count.upper(), "] interfaces")

    # Add New Entry to dbase/dictionary
    def newEntry(self):
        DICT1_Interfaces = Dictionaries().dict_Interfaces["Interfaces"]

        # ask for new interfacename, ip, and status
        name = input('New Interface: ')
        ip = input('IP: ')
        status = input('Status: ')

        # insert the inputs to the database
        DICT1_Interfaces["Interface"].append(name)
        DICT1_Interfaces["IP"].append(ip)
        DICT1_Interfaces["Status"].append(status)

        # display the database
        print('Showing all data with new entry')
        print("   ", "Interface   ", "   IP   ", "   Status   ")
        print("   ", "------------", "--------", "------------")
        count = 0
        for newInterface in DICT1_Interfaces["Interface"]:
            if DICT1_Interfaces["Interface"][count].__contains__('Serial'):
                print("   ", newInterface, "  |  ", DICT1_Interfaces["IP"][count], "|  ", DICT1_Interfaces["Status"][count])
            if DICT1_Interfaces["Interface"][count].__contains__('Ethernet'):
                print("   ", newInterface, "|  ", DICT1_Interfaces["IP"][count], "|  ", DICT1_Interfaces["Status"][count])
            count = count + 1

    # Main function
    # Function to display options of user to what to do in the information in the dict or database
    def display(self): #self is needed always when calling the method from a class
        print('Created by: Jennifer A.  Lacaste, 20201208\n')

        option = input('Choose an option: small caps allowed. \nFind [S]tatus, Show [A]ll, Find [I]nterface & IP, [C]ount Interfaces, [N]ew Entry:\n"_"')
        class switchOption:
            def switch(self, option):
                default = 'Invalid Option'
                return getattr(self, 'case_' + str(option).lower(), lambda: default)()

            # Write a python program to find [status] of a given interface
            def case_s(self):
                return Main.findStatus(self)

            # [Showing All] the data inside the dictionary or list of Interfaces
            def case_a(self):
                return Main.showAll(self)

            # Write a python program to find [interface] and [IP] of all interfaces which are up
            def case_i(self):
                return Main.findInterfaceAndIP(self)

            # Write a python program to [count] how many ethernet interfaces are there
            def case_c(self):
                return Main.countInterfaces(self)

            # Write a python program to [add a new entry] to above database
            def case_n(self):
                return Main.newEntry(self)

        # create an object
        s = switchOption()  # object s
        s.switch(option)  # call or display the content of the case entered

# MAIN-----------------------------------------------------------------------------------------------------------------------
Main().display()