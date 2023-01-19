def permute(length, list):
   if length == 1:
      return list
   else:
      return [ 
         y + x
         for y in permute(1, list)
         for x in permute(length - 1, list)
      ]
print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))
