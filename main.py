import datetime

if __name__ == '__main__':
    from application.people import get_employees
    from application.salary import calculate_salary

    e = get_employees()
    print(e)
    c = calculate_salary()
    print(c)


def func_in_main():
    a = datetime.date.today()
    print(a)
    d = 'function in main'
    return d


print(func_in_main())
