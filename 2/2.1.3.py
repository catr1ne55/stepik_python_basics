class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super(PositiveList,self).append(x)

class NonPositiveError(Exception):
    pass

