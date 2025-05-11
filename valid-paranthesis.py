"""
this was a very fun problem to solve, essentially i have to rethink how i do things my thought process. i jump on the most optimal way to do things instead 
of first thinking of themost brute force solution how annotying. 

anyways i started with i knew u had to use a stack to solve this problm the how was the matter, i tried to visualize using stack for either equating or 
closing but it didnt really offer any convenicene or upgrade regardless its almost like i could usea list and get away with it. thats when i came up with hashmap
and a mix of adding every single closed bracket to the stack for each corresponding open bracket, so in other words when u reach a closed bracket it should 
by ordering be on the top of the tack cus last in first out, thats how nested paranthesis work and thats how stacks work.

lets get to the problem, the problem wants us to find isvalid paranthesis ordering, from my above explanation its pretty easy to gauge how to do this,
u use hashmaps to map ur open brackets to close brackets for ease of use and to not create if else monstrosities. 
once u have that u first iterature thru each element in our given string s if the string is an open bracket we append it but on th eelse case 
we basically pop from the stackadn compare it with our close bracket and if it doesnt match we return false if not we continue, pretty straightforward right nice

but there are twoedge cases 1. what if the stack is empty? i actually had to come across this edge case while submitting, so in other words i have to think more of edge cases.
the easy and obvious solution is just uh input and stack count validation thats it 
2. theres an edgecase what if theres only 1 open bracket in our inpu= string s???? thats annoying well itsvalid cus we do on;yone iteration so any closed brackets
are handled only in the second iteration in other weneeds atleast [] or [) two characters atleast to validate properly, so in this case we basically
have to validate the return statement thats why True if not stack else False, which means if theres something in the stack then its not valid
if there nothing its true cool. waow i hate myself but i did solve it pretty easily in like 30 secs so ill let it slide ig
"""

class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(': ')', '{' : '}', '[' : ']'
        }
        stack = []

        for c in s:
            if c in hashmap:
                stack.append(hashmap[c])
            else:
                closing_paran = None
                if len(stack) != 0:
                    closing_paran = stack.pop()
                if c != closing_paran:
                    return False
        
        return True if not stack else False

            
        