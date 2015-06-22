class User(object):

    MAX_RANK = 8
    RANK_TRIGGER = 100

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, level):
        assert level != 0
        assert -8 <= level <= 8

        if level > self.rank:
            self.progress += 10 * self.__level_diff(level)**2

        elif level == self.rank:
            self.progress += 3

        elif self.__level_diff(level) == 1:
            self.progress += 1

        self.__refresh_rank()

    def __refresh_rank(self):
        if self.progress >= self.RANK_TRIGGER:
            self.rank = min(self.MAX_RANK, self.rank + self.progress/self.RANK_TRIGGER)
            self.rank += 1 if self.rank == 0 else 0

        self.progress %= 1 if self.rank == self.MAX_RANK else self.RANK_TRIGGER


    def __level_diff(self, level):
        if level >= self.rank:
            return level - self.rank -  1 * (self.rank < 0 and level > 0)
        else:
            return self.rank - level - 1 * (self.rank > 0 and level < 0)
