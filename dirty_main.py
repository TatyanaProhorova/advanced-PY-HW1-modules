import sys
from pprint import pprint
sys.path.insert(0, 'application/')

pprint(sys.path)

if __name__ == '__main__':
    from application.people import *
    from application.salary import *

    e = get_employees()
    print(e)
    c = calculate_salary()
    print(c)


def func_in_dirty_main():
    d = 'Function in dirty_main'
    return d


print(func_in_dirty_main())

