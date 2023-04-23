from shutil import copyfile
def files(fname):
    txt = open(fname)
    print(txt.read())
files('demo.txt')

def filed(fname):
    with open(fname) as f:
        content=f.readlines()
        print(content)
filed('demo.txt')

def filex(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i+1
print(filex('demo.txt'))


