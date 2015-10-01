#Jesse Fitzjarrell 9-30-15
#Blatent copying of Django Girls blog with some minor modifications. 
#I did this to learn Django and prove that I can follow a code example 
# I added a jQuery hide show on the comment section and changed the CSS 
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Capstone.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
