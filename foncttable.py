def affiche_une_table(n):
    for i in range(1,10):
      print(repr(n).rjust(1), 'x', repr(i).ljust(3),'=',repr(n*i).ljust(5))
    return
    
