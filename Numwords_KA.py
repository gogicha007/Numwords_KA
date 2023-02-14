class Numwords_KA(object):
    def __init__(self) -> None:
        self.hi_numwords = [
            "",
            "ოც",
            "ორმოც",
            "სამოც",
            "ოთხმოც",
        ]
        self.low_numwords = [
            "ი", 
            "ერთი","ორი","სამი","ოთხი","ხუთი",
            "ექვსი","შვიდი","რვა","ცხრა","ათი",
            "თერთმეტი","თორმეტი","ცამეტი","თოთხმეტი","თხუთმეტი",
            "თექვსმეტი","ჩვიდმეტი","თვრამეტი","ცხრამეტი"
        ]

    def get_words(self, n):
        if n < 100:
            return (f"{self.hi_numwords[n//20]}{'' if n%20 == 0 else 'და'}" if n > 19 else '') + f"{self.low_numwords[n%20]}"
        if n < 1_000:
            hundreds = self.low_numwords[n%1000 // 100].rstrip('ი') if n%1000 // 100!=1 else ''
            return f"{hundreds}ას{self.get_words(n%100)}"
        if n < 1_000_000_000:
            millions = n%10**9 // 10**6
            thousands = n%10**6 // 10**3
            result = ''
            result += f"{self.get_words(millions) if millions !=1 else ''}{' მილიონ ' if n%10**6 else ' მილიონი'}" if millions else ''
            result += f"{self.get_words(thousands) if thousands !=1 else ''}{' ათას ' if n%1000 else ' ათასი'}" if thousands else ''
            result += self.get_words(n%1000) if n%1000 else ''  
            return result
        return "ბევრი"

    def convert(self, n):
        return self.get_words(n) if n!=0 else 'ნული'

n2p = Numwords_KA()
print(n2p.convert(995_599_771))