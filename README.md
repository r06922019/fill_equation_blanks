# fill_equation_blanks

This program is for solving questions in the following form.
```
    N A N G A N G
    H A I S H A N
  + H U I L O N G 
 ------------------
    Z H I S H A N
```
Each character represents a single digit (0~9) and it is assumed that different characters represent different digits.

The main utility function `solve` is called as follows.

```
solve(["NANGANG", "HUILONG", "HAISHAN"], [1, 1, 1], "ZHISHAN") 
# represents the equation: NANGANG + HUILONG + HAISHAN = ZHISHAN
```

The first parameter is a list of words.   
The second parameter is the sign of each word in the list.   
The third parameter is a word representing the result of the original equation.   
