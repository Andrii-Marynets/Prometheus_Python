
class SuperStr(str):
    def is_repeatance(self, key):
        if isinstance(key, str):
            s = self
            if key == '' or s == '':
                return False
            res = ''
            for i in range(0, len(s), len(key)):
                res += key
            if res == s:
                return True
            else:
                return False
        else:
            return False
    def is_palindrom(self):
        s = self.lower()
        if s[0:len(s) / 2] == s[len(s):len(s) / 2:-1]:
            return True
        else:
            return False
s = SuperStr('')
print s.is_repeatance('q')
