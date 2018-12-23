# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:17:46 2018

@author: Admin
"""

Created on Sun Dec 23 19:45:12 2018

@author: 刘莹莹
"""

start='hit' 


 
end='cog' 


 
adict=['hot','dot','dog','lot','log'] 


 
def find_(start,end,path): 


 
    if start==end: 


 
        return 'start=end' 


 
    else: 


 
        visited=[] 


 
        visited.append(start) 


 
        for word in visited: 


 
            for i in range(len(word)): 


 
                for j in range(26): 


 
                    n=chr(ord('a')+j) 


 
                    newst=word[:i]+n+word[i+1:] 

 
                    if newst in path and newst not in visited: 


 
                        visited.append(newst) 


 
                        print(newst) 


 
                    if newst==end: 


 
                        print("find: "+newst) 
                        
                        print("The path is: ")
                        print(visited)


 
                        return  


 
find_(start,end,adict)
              
