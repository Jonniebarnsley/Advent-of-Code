with open('day7.txt', 'r') as f:
    input = f.read().splitlines()

class tree():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0
    def addnode(self,obj):
        self.children.append(obj)

class dir():
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def addnode(self, obj):
        self.children.append(obj)

class file():
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

home = tree('/')
pwd = home

def cd(name):
    global pwd
    if name == '..':
        pwd = pwd.parent
        return
    for child in pwd.children:
        if child.name == name:
            pwd = child
            return

for line in input[1:]:
    if line[0] != '$':
        type, name = line.split()
        if type == 'dir':
            pwd.addnode(dir(name, pwd))
        else:
            pwd.addnode(file(name, type))
    elif 'cd' in line:
        folder = line[5:]
        cd(folder)
    else:
        continue

#part 1
p1 = 0
dir_sizes = []
def do_sizes(folder):
    global p1
    global p2
    for child in folder.children:
        if isinstance(child, file):
            folder.size += child.size
        elif isinstance(child, dir):
            folder.size += do_sizes(child)
    if folder.size < 100000:
        p1 += folder.size
    dir_sizes.append(folder.size)
    return folder.size

do_sizes(home)

print(p1)

#part 2
dir_sizes.sort()
for size in dir_sizes:
    if size > home.size-40000000:
        print(size)
        break