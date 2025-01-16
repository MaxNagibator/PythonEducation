try:
    #a = int("a1")
    raise Exception('stherox goodman')
except ValueError:
    print('atata convert trouble bro')
except Exception as e:
    print(type(e))
    print(e)
