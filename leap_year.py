def is_leap(year):
    #just some conditions...
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            return False
        return True
    return False

year = int(input())
print(is_leap(year))
