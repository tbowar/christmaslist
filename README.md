# christmaslist

christmaslist reads a comma delimited list of names in the following format for each line:
<name>, <spouse or name to avoid matching with>, <last year's match>

There may be as many lines as needed for the group, minimum 3 lines.

The purpose is to take the list of names and randomly match them with others in the group for a "secret Santa" list.

On each line, the first name is a member of the group, and the 2nd and 3rd names (if present) are other names in the group to avoid matching with. Presumably, the 2nd name would be a spouse, and the 3rd name would be the person with whom this member was matched last year. If the matching algorithm comes to an impasse (no matchable members left), it will start over.

Rules used:
1. Do not match a member with a spouse (element 2 on the line).
2. Do not match a member with last year's match (element 3 on the line).
3. Randomly choose a match with another member. If there are no allowed matches at the end, start the process over.

At present, there must be 3 elements per line. If there is no spouse, a non-member word or character can be used, such as an x.

The comma delimited file can be specified on the command line, or, if not found, will be requested when the program starts.

From the menu, you may add names, delete names, print the list of names, or create a new list based on last year's file, which will take into account last year's gift receiver matches. There is also a help screen available from the menu.
