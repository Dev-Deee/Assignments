import java.util.Scanner;
public class Nokia{
    public static void main(String[]args){
    
     Scanner input = new Scanner(System.in);
     System.out.println("""

        NOKIA MENU
        ---------------------------
        1. Phonebook
        2. Messages
        3. Chats
        4. Call register
        5. Tones
        6. Settings
        7. Call divert
        8. Games
        9. Calculator
        10. Reminder
        11. Clock
        12. Profiles
        13. SIM services
        ----------------------------
    Enter a number to navigate 
"""); 
       

        int phoneBook = input.nextInt();

    switch (phoneBook){
    case 1-> {
    System.out.println("""

    1. Search
    2. Service Nos
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
    9. Speed dials
    10. Voice Tags

""");

 


    int optionEight = input.nextInt();

    switch (optionEight){
    case 8-> 
    System.out.println("""

    1. Type of view
    2. Memory Status
    

""");
        }
     }
}

    
    switch (phoneBook){
    case 2-> {
    System.out.println("""

    1. Write message
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
    8. info service
    9. Voice mailbox number
    10. Service command editor

""");


        int messageSettings = input.nextInt();

    switch (messageSettings){
    case 7-> {System.out.println("""

    1. Set
    2. Common

""");
     

        int set = input.nextInt();

    switch (set){
    case 1-> System.out.println("""

    1. Message centre number
    2. Message sent as
    3. Message validity

""");
     }


        int common = input.nextInt();

    switch (common){
    case 2-> System.out.println("""

    1. Delivery Reports
    2. Reply via same Centre
    3. Character Support

""");
       } 
    }
    }
  }
}


    switch (phoneBook){
    case 3-> System.out.println("""

    1. Chat

""");   
     }


    switch (phoneBook){
    case 4-> {System.out.println("""

    1. Missed calls
    2. Recieved calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call cost
    7. Call cost settings
    8. Prepaid credit

""");

        int missedCalls = input.nextInt();

    switch (missedCalls){
    case 1-> System.out.println("""
    1. Missed calls

""");
    }

        int recievedCalls = input.nextInt();

    switch (recievedCalls){
    case 2-> System.out.println("""
    1. Recieved calls

""");
    }

        int dialledNumber = input.nextInt();

    switch (dialledNumber){
    case 3-> System.out.println("""
    1. Dialled number

""");
    
    }

        int eraserecent = input.nextInt();

    switch (eraserecent){
    case 4-> System.out.println("""
    1. Erase recent

""");
    }


        int ShowCallDuration = input.nextInt();

    switch (ShowCallDuration){
    case 5-> System.out.println("""

    1. Last call duration
    2. All calls' duration
    3. Recieve calls' duration
    4. Dialled calls' duration
    5. Clear timers

""");
    }
     


        int ShowCallCost = input.nextInt();

    switch (ShowCallCost){
    case 6-> System.out.println("""

    1. Last call cost
    2. All call's cost
    3. clear counter

""");
    }
      

        int callCostSettings = input.nextInt();

    switch (callCostSettings){
    case 7-> System.out.println("""

    1. Call cost limit
    2. show costs in

""");
    }


        int prepaid = input.nextInt();

    switch (prepaid){
    case 8-> System.out.println("""
    1. Erase recent

""");
    }
    }
    }



    switch (phoneBook){
    case 5-> System.out.println("""

    1. Ringing tones
    2. Ringing Volumes
    3. Incoming call alert
    4. Composer
    5. Message alert tones
    6. Keypad tones
    7. Warning and game tones
    8. vibrating alert
    9. Screen saver

""");
    }



    switch (phoneBook){
    case 6-> {System.out.println("""

    1. Call Settings
    2. Phone Setting
    3. Security settings
    4. Restore Factory settings
    
""");


        int callSetting = input.nextInt();

    switch (callSetting){
    case 1-> System.out.println("""
    1. Automatic redial
    2. Speed dialling
    3. Call waiting options
    4. Own number sending
    5. Phone line in use
    6. Automatic answer

"""); 
    }


        int phoneSettings = input.nextInt();

    switch (phoneSettings){
    case 2-> System.out.println("""
    1. Language
    2. Cell info display
    3. Welcome note
    4. Network selection
    5. Lights
    6. Confirm SIM service actions


""");
    }


        int securitySettings = input.nextInt();

    switch (securitySettings){
    case 3-> System.out.println("""
    1. PIN code request
    2. call barring service
    3. Fixed dialling
    4. Closed user group
    5. Phone security
    6. Change access codes

""");
    }


         int restoreFactorySettings = input.nextInt();

    switch (restoreFactorySettings){
    case 4-> System.out.println("""
    1. Restore factory settings

""");
        }
       }
   }


    
    switch (phoneBook){
    case 7-> System.out.println("""
    1. Call divert

""");   
    }



    switch (phoneBook){
    case 8-> System.out.println("""
    1. Games
""");   
    
     }
    


    switch (phoneBook){
    case 9-> System.out.println("""
    1. Calculator
""");   
    }


    switch (phoneBook){
    case 10-> System.out.println("""
    1. reminder
""");   
    }


    switch (phoneBook){
    case 11-> System.out.println("""
    1. Alarm clock
    2. Clock settings
    3. Date setting
    4. Stopwatch
    5. Countdown time
    6. Auto update of date and time
""");   
    }


    switch (phoneBook){
    case 12-> System.out.println("""
    1. Profiles
""");   
    }

    switch (phoneBook){
    case 13-> System.out.println("""
    1. SIM services
""");   
    }

}

}
