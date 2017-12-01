class Dest(object):

    _i = 3

    def get_i(self):
        return self._i

    def set_i(self,val):
        self._i = val

    i = property(get_i, set_i)
x1 = Dest()
x2 = Dest()
# x1.i = 50
# assert x2.i == x1.i  # no error
# assert x2.i == 50  # the property is synced