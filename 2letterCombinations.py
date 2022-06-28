def letterCombinations(digits: str):
   num = {
      "2": ["a", "b", "c"],
      "3": ["d", "e", "f"],
      "4": ["g", "h", "i"],
      "5": ["j", "k", "l"],
      "6": ["m", "n", "o"],
      "7": ["p", "q", "r", "s"],
      "8": ["t", "u", "v"],
      "9": ["w", "x", "y", "z"]
   }
   ans = [""]
   for d in digits:
      if d in num:
         new = []
         for item in ans:
            for c in num[d]:
               new.append(item + c)
         ans = new
   return ans
