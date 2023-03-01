from gadmoakartule import gadmoakartule


class NumwordsKA(object):
    def __init__(self, n: int) -> None:
        self.number = n

    def __str__(self) -> str:
        return gadmoakartule(self.number)


assert f'{NumwordsKA(995_599_771)}' == 'ცხრაას ოთხმოცდათხუთმეტი მილიონ ხუთას ოთხმოცდაცხრამეტი ათას შვიდას სამოცდათერთმეტი'
