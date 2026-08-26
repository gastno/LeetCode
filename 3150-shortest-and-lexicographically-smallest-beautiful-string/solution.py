class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if(s.count("1")<k):
            return ""
        else:
            i=0
            pos=0
            btfSubstr=""
            while i <= ( s.count("1") - k ):
                substring=""
                if(s[pos]=="1"):
                    j=0
                    subPos=pos
                    while j<k:
                        substring+=s[subPos]
                        if(s[subPos]=="1"):
                            j+=1
                        subPos+=1
                    if(btfSubstr==""):
                        btfSubstr=substring
                    elif(len(substring)<len(btfSubstr)):
                        btfSubstr=substring
                    elif(len(substring)==len(btfSubstr)):
                        for x in range(0,len(substring)):
                            if(substring[x]<btfSubstr[x]):
                                btfSubstr=substring
                                break
                            elif(substring[x]>btfSubstr[x]):
                                break
                    pos+=1
                    i+=1
                else:
                    pos+=1
            return btfSubstr
