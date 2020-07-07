# Print "Hello, world!" to your terminal
print("Hello World")

# bytes_representation = 'abcdefghijklmnopqrstuvwxyz'.encode()

# for byte in bytes_representation:
#     print(byte)



def my_hashing_func(str, list_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % list_size


my_list = [None] * 5

my_list[my_hashing_func("black", len(my_list))] = "#000000" # put value in list
print('Color code: ' +  my_list[my_hashing_func("black", len(my_list))]) # get value from list

### Print Output
### #00FFFF

print(f'My List: {my_list}')
print(f'Color: {my_list[4]}')

arr = [] * 5
arr.insert(0, 'what')

# for i in arr:
	
