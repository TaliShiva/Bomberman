from sys import version_info
from webclient import WebClient
from dds import DirectionSolver

def main():

    assert version_info[0] == 3, "You should run me with Python 3.x"

    dds = DirectionSolver()
    wcl = WebClient(dds)
    wcl.run("ws://142.93.104.159/codenjoy-contest/ws", 'talishiva@mail.ru&code=6340739691534511755')

if __name__ == '__main__':
    main()
