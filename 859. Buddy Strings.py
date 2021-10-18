def check(s,g):
    if len(s) != len(g):
        return False
    if s==g and len(set(s))<len(s):
        return True
    # x,y=-1,-1
    # for i in range(len(s)):
    #     if s[i]!=g[i]:
    #         if x==-1:
    #             x=i
    #         else:
    #             y=i
    #             t=s[:x]+s[y]+s[x+1:y]+s[x]+s[y+1:]
    #             print(t)
    #             if t==g:
    #                 return True
    #             return False
    # the whole above thing can be done like this
    
    dif =[(x,y) for x , y in zip(s,g) if x!=y]
    return  len(dif)==2 and dif[0] == dif[1][::-1]

    
print(check('ab', 'ba'))
                