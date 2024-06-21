empty_bytes = bytes(4)
print(empty_bytes)
print(type(empty_bytes))

data_bytes = bytes(b'\xFF\xFF')
print(data_bytes) 

mutable_bytes = bytearray(b'\xDE\xAD\xBE\xEE')
mutable_bytes[0]=0
mutable_bytes.append(255)

print(mutable_bytes)
print(type(mutable_bytes))
print(mutable_bytes[0:2])
