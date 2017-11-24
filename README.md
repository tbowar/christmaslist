# christmaslist

christmaslist reads a comm delimetd list of names in the following format for each line:
<name>, <name to avoid matching with>, <second name to avoid matching with>

There may be as many lines as needed for the group, minimum 3 lines.

The purpose is to take the list of names and randomly match them with others in the group for a "secret Santa" list.

On each line, the first name is a member of the group, and the 2nd and 3rd names (if present) are other names in the 
group to avoid matching with. Presumably, the 2nd and 3rd names would be the person with whom this member was matched 
last year, the member's spouse, or someone else with whom the member should not be matched. If the matching algorithm 
comes to an impasse (no matchable members left), it will start over.
