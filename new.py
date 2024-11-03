print("hello from new file")
import sys

args = sys.argv
print(args)

second_arg = args[1]
#переписати виристовуючи словник
if second_arg == "1":
    print("Hello Dima")
elif second_arg == "2":
    print("Hello Artem") 
elif second_arg == "3":
    print("Hello Volodyas")
elif second_arg == "4":
    print("Hello Maks")
else:
    print("Hello mister Teacher")