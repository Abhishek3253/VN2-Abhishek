def pack(*nums):
    print(f'packed : {nums}')
    for x in nums:
        print(f'packed : {x}')
pack(1,2,3)
def unpack(a,b,c):
    print("unpack")
    print(f'a= {a}')
    print(f'b= {b}')
    print(f'c= {c}')
num= [1,2,3]
unpack(*num)

