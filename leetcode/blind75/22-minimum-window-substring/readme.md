attempt (neetcode solution):

1. create a map "need_map" consisting of all the characters in t and their occurrence counts
   1. `e.g {a: 1, b: 2}`
2. create an empty map "have_map"
3. create a left and right pointer
4. if have_map != need_map we increment "r" pointer
   1. if s[r] is in need_map, then it's a character we care about and should increment the have_map
5. while have_map == need_map we increase l 
   6. if s[l] is in need_map, it's a character we care about and should decrement the have_map
   7. iff (right - left) is the shortest substring we have encountered then save the right/left position
7. After loop is completed and r is at the end of the string s, return s[minimum_left:minimum_right]

NB:
- To speed up the have_map == need_map check, we keep a 'have' and 'need' integer.
- have = 0, need = len(need_map.keys())
- now, when incrementing r, we check if have_map[s[r]] == need_map[s[r]] THEN have += 1
- equally, when incrementing l, if have_map[s[l]] < need_map[s[l]] THEN have -= 1
- This means that our `have == need` check is O(1), so are inserts in the map and equality checks between have/need map.


Runtime = O(n), we only pass through the input string once. All other operations are O(1).


Runtime beat 94% runtime, 82% memory



<br>
<br>

NB 2.0 - first submission used len(output string) which is not O(1), only beating 40% runtime.