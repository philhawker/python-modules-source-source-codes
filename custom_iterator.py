class Lineup:
    def __init__(self, players):
        self.players = players
        
    def __iter__(self):    # iter always has to have a return 
        self.n = 0
        return self
    
    def __next__(self):    
        if self.n < (len(self.players) -1):  # This line is a great way to grab the last element of a list
            player = self.players[self.n]
            self.n += 1
            return player

            
astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick',
    'Gonzalez',
    'McCann',
    'Davis',
    'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))