
def gcd(a,b):
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

def gcdString(s1,s2):
    if s1 + s2 != s2 + s1:
            return ""
    return s1[:gcd(len(s1), len(s2))]
    

if __name__=="__main__":
    print(gcdString("ABCABC","ABC"))
    print(gcdString("ABABAB","ABAB"))
    print(gcdString("LEET","CODE"))
    

    
