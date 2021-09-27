new_id = input()
new_id = new_id.lower()
# 65~90 대문자 97~122 소문자 
# list()로 배열로 바꿔서 해도됨
print(new_id)
for i in range(len(new_id)):
    if(not(97<=ord(new_id[i])<=122 or new_id[i] in ("-", "_", "." ))):
        new_id[i] = " "

new_id.split()

print(new_id)
    # ord로 아스키 코드로