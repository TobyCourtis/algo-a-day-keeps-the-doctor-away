# Approach

My first approach (maybe not optimal)
1. Iterate through each cell
2. If block present += 2 for top and bottom face
3. Go through the other 4 faces
4. Check showing surface area (SA) by doing (current block SA - adjacent block SA)
   1. If no block adjacent, add all the current block SA
5. Return total

Second approach:
- Go through each face of the entire block
- Take largest block in each column to be the exposed SA for that face
- Add each of the larger face SA's 
- Return total

