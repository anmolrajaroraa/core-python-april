'''import io
# open fn is used to create a stream from txt file to py file
fileStream = open("file-handling.txt", "r")
# data = fileStream.read()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
# data = fileStream.readline()
# print(data)
data = fileStream.read(100)
print(data)
# fileStream.write("hello")
fileStream.close()

# except io.UnsupportedOperation as e:
#     print(e)'''


# fileStream = open("file-handling2.txt", "w")
# # fileStream.write(
# # "This data will be written in the first line, but before that existing data, if any, will be truncated")
# fileStream.write("Some new data")
# fileStream.close()

# fileStream = open("file-handling.txt", "a")
# fileStream.write("\nThis text will be written at the end of the file")
# fileStream.close()

# fileStream = open("file-handling.txt", "r+")
# data = fileStream.read()
# print(data)
# fileStream.write("Some new data added by using r+ mode")
# fileStream.close()

# fileStream = open("file-handling2.txt", "w+")
# fileStream.write("Some new data added by using w+ mode")
# fileStream.seek(0)
# data = fileStream.read()
# print("Data is ", data)
# fileStream.close()


# fileStream = open("file-handling.txt", "a+")
# fileStream.write("Some new data added by using a+ mode")
# fileStream.seek(0)
# data = fileStream.read()
# print("Data is ", data)
# fileStream.close()


fileStream = open("watch.jpeg", "rb")
data = fileStream.read(5000)
fileStream.close()
# print(data)
fileStream = open("watch2.jpeg", "wb")
fileStream.write(data)
fileStream.close()
