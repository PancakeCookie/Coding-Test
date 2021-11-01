id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k = 3
coupon = 0
result = 0
new_list = set()
for i in id_list:
    for j in list(i.split(" ")):
        new_list.add(j)
new_list = list(new_list)
print(new_list)


for i in range(0,len(id_list)):
    id_list[i] = set(id_list[i].split(" "))
    id_list[i] = list(id_list[i])
print(id_list)


for i in new_list:
    coupon = 0
    for j in id_list:
        coupon = coupon + j.count(i)
    if coupon>=k:
        coupon=k
    result = result + coupon

print(result) 
