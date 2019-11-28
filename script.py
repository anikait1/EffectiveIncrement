import sys

base_num = None
increment_value = None

try:
    base_num = int(sys.argv[1])
    increment_value = int(sys.argv[2])
except (IndexError, ValueError) as err:
    print("Either a base number or increment value was not passed")
    while True:
        try:
            base_num = int(input("Enter base number: "))
            increment_value = int(input("Enter increment value: "))
            break
        except ValueError:
            print("Enter a valid number for both the values")

with open("effective.py", "w") as f:
    f.write(f"def effective_increment():\n\tnum = {base_num}\n\n")
    
    for _ in range(increment_value):
        f.write(f"\tif num == {base_num}:\n\t\tnum = {base_num + 1}\n")
        base_num += 1
    
    f.write(f"\n\treturn num")
