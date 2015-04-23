d = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
a = [1,1,[2,2,[3]]]
def file_search(folder, filename):
    path = ''
    for item in folder:
        if item == filename:
            path += '/' + item
        elif isinstance(item, list):
            file_search(item, filename)
    return path
print file_search(d, 'hereiam.py')
