def message_by_chuncks(message:str, chunk_size):
    for i in range(0, len(message), chunk_size):
        yield message[i:i + chunk_size]



x=message_by_chuncks("Hello, World!", 5)

for message in x:
    print(message)