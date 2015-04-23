
class CombStr:
    string = None
    count = None
    def __init__(self, string):
        self.string = str(string)
    def count_substrings(self, length):
        self.count = 0
        if not isinstance(length, int) or \
                        length == 0 or \
                        length > len(self.string):
            return 0

        elif length == len(self.string):
            return 1
        res = []
        for i in range(0, len(self.string)):
            res.append(self.string[i:i + length])
        res = set(res)
        for i in res:
            if len(i) == length:
                self.count += 1
        return self.count
s0 = CombStr("A taste of honey. Tasting much sweeter than wine. I dream of your first kiss. And then I feel upon my lips"
             " again. A taste of honey. Tasting much sweeter than wine. I will return, yes I will return. I'll come back"
             " for the honey and you. Yours was the kiss that awoke my heart. There lingers still, though we're far "
             "apart. That taste of honey. Tasting much sweeter than wine. Oh I will return, yes I will return. I'll come"
             " back (He'll come back). for the honey (For the honey). and you")
print s0.count_substrings(21)
