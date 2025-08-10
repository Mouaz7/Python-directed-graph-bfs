# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>. Modified by Johan Eliasson
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

"""
Datatypen Prioritetsk� enligt definitionen p� sidan 293 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7 

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar en prioritetsk� med hj�lp av DirectedList
"""
from DirectedList import DirectedList

class PrioQueueDirectedList:
    def __init__(self, cmpFcn):
        """
            Syfte: Skapar en tom prioritetsk�
            Pararmetrar: cmpFcn - en j�mf�relsefunktion som returnerar True/False
            Returv�rde: 
            Kommentarer: Ett tom prioritetsk�, funktionen heter Empty i specifikationen
        """   
        self._cmpFcn = cmpFcn
        self._queue = DirectedList()
        
    def insert(self, val):
        """
            Syfte: Stoppar in ett element med v�rde val i prioritetsk�n
            Pararmetrar: val - v�rdet som ska in i prioritetsk�n
            Returv�rde: 
            Kommentarer: 
        """      
        if self._queue.isempty():
            self._queue.insert(self._queue.first(), val)
        else:
            placed = False
            pos = self._queue.first()
            while not placed and not self._queue.isEnd(pos):
                if self._cmpFcn(val, self._queue.inspect(pos)):
                    placed = True;
                    self._queue.insert(pos, val)
                pos = self._queue.next(pos)   
            if not placed:
                self._queue.insert(pos, val)

    def isEmpty(self):
        """
            Syfte: Kollar om prioritetsk�n �r tom
            Pararmetrar: 
            Returv�rde: True om prioritetsk�n �r tom, annars False
            Kommentarer: 
        """  
        return self._queue.isempty()
    
    def inspectFirst(self):
        """
            Syfte: Ger v�rdet av f�rsta elementet i prioritetsk�n
            Pararmetrar: 
            Returv�rde: V�rdet som �r f�rst i k�n
            Kommentarer: 
        """  
        if not self._queue.isempty():
            return self._queue.inspect(self._queue.first())
        return None

    def deleteFirst(self):
        """
            Syfte: Tar bort f�rsta elementet ur prioritetsk�n
            Pararmetrar: 
            Returv�rde: 
            Kommentarer: 
        """  
        if not self._queue.isempty():
            self._queue.remove(self._queue.first())

    def update(self, val, newVal):
        """
            Syfte: Uppdaterar v�rdet val som antas finnas i prioritetsk�n till newwal
            Pararmetrar: val - det v�rde som ska f� ny prioritet
                         newVal - det nya v�rdet med ny prioritet
            Returv�rde: 
            Kommentarer: Odefinierat vad som h�nder om inte val finns i k�n. 
                         F�ruts�tter att v�rdena i k�n kan j�mf�ras med ==
        """         
        found = False
        pos = self._queue.first()
        while not found:
            if self._queue.inspect(pos) == val:
                self._queue.remove(pos)
                self.insert(newVal)
                found = True 
            pos = self._queue.next(pos)
                
