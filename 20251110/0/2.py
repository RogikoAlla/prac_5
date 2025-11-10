 C = type('CC',(),{'a': 213,' __str__':lambda self:f'self.__class__.__name__'},{})
 D = type('DD',(C),{'Q-Q!':'Q-Qu!'})
 print(C.__dict__['Q-Q!'])
