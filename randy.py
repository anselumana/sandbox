import sys

def sayHello(message='GitHub'):
    print('Hello {}!'.format(message))

if __name__ == '__main__':
    sayHello(sys.argv[1])
