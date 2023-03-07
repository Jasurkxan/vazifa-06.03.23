# 1-masala

# a=input().split() 
# if len(a)>0:
#   print([[],[a[0]],[a[1]],[a[2]],[a[0],a[1]],[a[1],a[2]],[a[0],a[2]],[a[0],a[1],a[2]]])
# else:
#   print([[]])


# 2-masala

# bal1=['A','E','I','O','U','L','N','S','T','R']
# bal2=['D','G']
# bal3=['B','C','M','P']
# bal4=['F','H','W','V','Y']
# bal5=['K']
# bal8=['J','X']
# bal10=['Q','Z']

# a=input().upper()
# bal=0
# for i in a:
#     if i in bal1:
#         bal+=1
#     elif i in bal2:
#         bal+=2
#     elif i in bal3:
#         bal+=3
#     elif i in bal4:
#         bal+=4
#     elif i in bal5:
#         bal+=5
#     elif i in bal10:
#         bal+=10
#     elif i in bal8:
#         bal+=8
# print(bal)

# 3-masala

# a=list(input())
# rt_lst=[]
# for i in range(len(a)):
#     if a[i] in rt_lst:
#         rt_lst.append(a[i])
#         a[i]=f'{a[i]}_{rt_lst.count(a[i])}'
#     else:
#         rt_lst.append(a[i])

# print(*a)

# 4-masala

with open("words.txt","r") as f:
    a=f.read().split()
    gap=input().split()
    for i in range(len(gap)):
        ab=0
        for j in range(len(a)):
            if a[j] in gap[i].lower():
                print('*'*len(gap[i]),end=" ")
                break
            ab+=1
            if ab==7:
                print(gap[i],end=" ")



# 6-masala
 
# count=int(input("Nechi marotaba IP manzil kiritmoqchisiz: "))
# lst=[]
# dict={}
# for i in range(count):
#     b=input()
#     a=b
#     a=a.split('.')

#     a1=int(a[0]);a2=int(a[1]);a3=int(a[2]);a4=int(a[3])
#     sum=a1*(256**3)+(a2*(256**2))+(a3*256)+(a4*(256**0))

#     lst.append(sum)
#     dict.update({str(b):sum})

# lst=sorted(lst)


# for j in range(count):
#     for i in dict:
#         if dict[i]==lst[j]:
#             print(i)



            

           
                
                


        


    

    



















