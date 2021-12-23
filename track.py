import csv;

## welcome screen + prompt admin for # of participants
in_register = True;
participant_slots=[];
csv_slots = [];

def register_tournament(num_participants):
    for i in range(0,int(num_participants)):
        participant_slots.append(None);
        csv_slots.append(None);
    print("\nGreat! There are %s participant slots ready for sign-ups." % (num_participants));

while in_register == True:
    print("Welcome to Tournaments R Us\n==========================");
    admin_input = input("Enter the number of participants: ");
    if admin_input.isnumeric() == True:
        register_tournament(admin_input);
        in_register = False;
    else:
        print("\nPlease enter a valid number.\n")

## direct user to participant menu

in_menu = True;

while in_menu == True:
    print("\nParticipant Menu\n================\n1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit");
    menu_select = input("Enter number of desired option: ");
    
    if menu_select == '1':
        #valid_name = False;
        valid_numstart = False;

        """
        while valid_name == False:
            print("\nParticipant Sign Up\n===================");
            user_name = input("Participant Name: ");
            if user_name.replace(" ","").isalpha() == True:
                user_name = user_name.title();
                valid_name = True;
            else:
                print("Invalid input. Please try again\n"); 
        """
        print("\nParticipant Sign Up\n===================");
        user_name = input("Participant Name: ");
    
        while valid_numstart == False:
            user_numstart = input("Desired starting slot #[1-%s]: " % (admin_input));
            if user_numstart.isnumeric() == True and int(user_numstart) > 0 and int(user_numstart) <= int(admin_input) and participant_slots[int(user_numstart)-1]== None:
                participant_slots[int(user_numstart)-1] = user_name;
                csv_slots[int(user_numstart)-1] = [user_numstart, user_name];
                print("\nSuccess:\n%s is signed up in starting slot #%s." % (user_name,user_numstart))
                #print(participant_slots);
                valid_numstart = True;
            elif user_numstart.isnumeric() == True and int(user_numstart) > 0 and int(user_numstart) <= int(admin_input) and participant_slots[int(user_numstart)-1] != None:
                print("\nError:\nSlot #%s is filled. Please try again\n" % (user_numstart))
            else:
                print("Invalid input. Please try again.\n")
    
    elif menu_select == '2':
        in_cancel = True;
        print("\nParticipant Cancellation\n========================")
        while in_cancel == True:
            user_numstart = input("\nDesired starting slot #[1-%s]: " % (admin_input));
            user_name = input("Participant Name: ");
            if user_name == participant_slots[int(user_numstart)-1]:
                participant_slots[int(user_numstart)-1] = None;
                csv_slots[int(user_numstart)-1] = None;
                print("\nSuccess:\n%s has been cancelled from starting slot #%s." % (user_name, user_numstart));
                in_cancel = False;
            else:
                print("\nError:\n%s is not in that starting slot." % (user_name));

    elif menu_select == '3':
        print("\nView Participants\n================");
        valid_numstart = False;
        while valid_numstart == False:
            user_numstart = input("Starting slot #[1-%s]: " % (admin_input));
            if user_numstart.isnumeric() == True and int(user_numstart) > 0 and int(user_numstart) <= int(admin_input):
                print("\nStarting Slot: Participant")
                slot_start = int(user_numstart) - 5;
                slot_stop = int(user_numstart) + 5;
                if (int(user_numstart)-5) < 1:
                    slot_start = 1;
                elif (int(user_numstart)+5) > int(admin_input):
                    slot_stop = int(admin_input);
                for i in range(slot_start,slot_stop+1):
                    print("%i: %s" % (i,participant_slots[i-1]));
                valid_numstart = True;
            else:
                print("Invalid input. Please try again.");

    elif menu_select == '4':
        in_save = True;
        while in_save:
            print("\nSave Changes\n============");
            user_save = input("Save your changes to CSV? [y/n]: ")
            if user_save.lower() == 'y':
                #print("This feature has not yet been configured. Please try again later.")
                fields = ['Starting Slot', 'Participant name'];
                for i in range(0,len(csv_slots)):
                    if csv_slots[i] == None:
                        csv_slots[i] = [(i + 1),""];
                rows = csv_slots;
                with open('tournament_status','w') as f:
                    write = csv.writer(f);
                    write.writerow(fields);
                    write.writerows(rows);
                in_save = False;
            elif user_save.lower() == 'n':
                in_save = False;
            else:
                print("Invalid input. Please try again.");               
    
    elif menu_select == '5':
        in_exit = True;
        while in_exit == True:
            print("\nExit\n====\nAny unsaved changes will be lost.");
            user_exit = input("Are you sure you want to exit? [y/n] ");
            if user_exit.lower() == 'y':
                in_exit = False;
                in_menu = False;
            elif user_exit.lower() == 'n':
                in_exit = False;
            else:
                print("\nInvalid input. Please respond with 'y' or 'n'.")
    else:
        print("\nInvalid input. Please respond with number 1-5.");
