class All:
    def __init__(self):
        pass

    def test(self, player):
        if player is not None:
            return True
        return False


class QueryBuilder:
    def __init__(self, matcher=All()):
        self.matcher_object = matcher

    def build(self):
        return self.matcher_object
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher_object, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher_object, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher_object, HasFewerThan(value, attr)))
    


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class Not:
    def __init__(self, condition):
        self.condition = condition

    def test(self, player):
        if self.condition.test(player):
            return False
        return True
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False