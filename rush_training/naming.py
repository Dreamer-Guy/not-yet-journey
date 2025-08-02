def naming(s):
    s=s.replace(". ","_")
    s=s.replace(" ","_")
    return s

s="974. Subarray Sums Divisible by K"
print(naming(s))