user = 'John', 'Snow'
user2 = 'John',  # A workaround for a tuple of one element
print(user[0], user[0:1])

scores = [15, 16, 97, 42]
print(scores[0], scores[1:2], scores[3:])

aliases = {
    'localhost': '127.0.0.1',
    'nas': '192.168.1.2',
}
print(aliases['nas'])
