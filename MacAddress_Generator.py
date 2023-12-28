import random

"""
For the code to work you must choose a text file path to generate the addresses at line 13.
You can also adjust the number of addresses at line 9.
"""

elem = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "A", "B", "C", "D", "E", "F",]

count = 0
while count != 100:    # <-- Adjust here
 mac = random.sample(elem , 12)
 address = "".join(mac)
 mac_address = ":".join(address[i:i+2] for i in range(0, len(address), 2))
 
 with open(r"<Please enter the text file path here>", "+a") as file:
     file.write(mac_address + "\n")
     file.close()

 count += 1
