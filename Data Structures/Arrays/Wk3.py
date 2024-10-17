q = [] 
Outlet1Sales = [10, 12,15,10] 
Outlet2Sales = [5,8,3,6] 
Outlet3Sales = [10,12,15,10] 
for i in range(4): 
    q.append(Outlet1Sales[i] + Outlet2Sales[i] + Outlet3Sales[i]) 
#next i 
for j in range(4): 
    print("Total for quarter", j+1 , q[j] * 1000) 
#next j 