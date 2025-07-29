class Media:
    def __init__(self,product):
        self.product = product

class Book(Media):
    def __init__(self, product, author, title, pages, isCheckedOut = False, ratings=[]):
        super().__init__(product)
        self.author = author
        self.title = title
        self.pages = pages
        self.isCheckedOut = isCheckedOut
        self.ratings = ratings
    
    def getProduct(self):
        return self.product
    
    def getAuthor(self):
        return self.author 
  
    def getTitle(self):
        return self.title
  
    def getPages(self):
        return self.pages
  
    def getIsCheckedOut(self):
        return self.isCheckedOut
  
    def getRatings(self):
        return self.ratings
    
    def getAverageRating(self):
        averageRating = 0
        sum = 0
        totalRatings = len(self.ratings)
        for i in range (totalRatings):
            sum += self.ratings[i]
        
        averageRating = sum / totalRatings
        return format(averageRating,'.2f')

    def toggleCheckedOutStatus(self):
        if self.isCheckedOut == False :
            self.isCheckedOut = True
        else:
            self.isCheckedOut = False
        
    def addRating(self,newRating):
        self.ratings.append(newRating)
    
class Movie(Media):
    def __init__(self, product, director, title, runTime, isCheckedOut=False, ratings=[]):
        super().__init__(product)
        self.director = director
        self.title = title
        self.runTime = runTime
        self.isCheckedOut = isCheckedOut
        self.ratings = ratings
    
    def getProduct(self):
        return self.product
    
    def getDirector(self):
        return self.director
    
    def getTitle(self):
        return self.title
    
    def getRunTime(self):
        return self.runTime
    
    def getIsCheckedOut(self):
        return self.isCheckedOut
    
    def getRatings(self):
        return self.ratings
    
    def getAverageRating(self):
        averageRating = 0
        sum = 0
        totalRatings = len(self.ratings)
        for i in range (totalRatings):
            sum += self.ratings[i]
        
        averageRating = sum / totalRatings
        return format(averageRating,'.2f')

    def toggleCheckedOutStatus(self):
        if self._isCheckedOut == False:
            self._isCheckedOut = True
        else:
            self._isCheckedOut = False

    def addRating(self,newRating):
        self.ratings.append(newRating)
    
class CD(Media):
    def __init__(self, product, artist, title, isCheckedOut=False, ratings=[], songs=[]):
        super().__init__(product)
        self.artist = artist
        self.title = title
        self.isCheckedOut = isCheckedOut
        self.ratings = ratings
        self.songs = songs
    
    def getProduct(self):
        return self.product
    
    def getArtist(self):
        return self.artist
    
    def getTitle(self):
        return self.title
    
    def getSongs(self):
        return self.songs
    
    def getIsCheckedOut(self):
        return self.isCheckedOut
    
    def getRatings(self):
        return self.ratings
    
    def getAverageRating(self):
        averageRating = 0
        sum = 0
        totalRatings = len(self.ratings)
        for i in range (totalRatings):
            sum += self.ratings[i]
        
        averageRating = sum / totalRatings
        return format(averageRating,'.2f')

    def toggleCheckedOutStatus(self):
        if self._isCheckedOut == False:
            self._isCheckedOut = True
        else:
            self._isCheckedOut = False

    def addRating(self,newRating):
        self.ratings.append(newRating)

atomicHabits = Book("Media", "James Clear", "Atomic Habits", 320, False, [9,7,9,8,8,10,8,9,7,10])
avatarWater = Movie("Media", "James Cameron", "Avatar 2: The Way of The Water", 192, False, [10,10,9,9,10,9,10,9,10,8])
damnKendrick = CD("Media", "Kendrick Lamar", "DAMN", False, [9,8,7,7,8,9,10,9,8,7],["BLOOD", "DNA", "YAH", "ELEMENT", "FEEL", "LOYALTY", "PRIDE", "HUMBLE", "LUST", "LOVE", "XXX", "FEAR", "GOD", "DUCKWORTH"])

atomicHabits.addRating(8)
atomicHabits.addRating(9)
avatarWater.addRating(10)
avatarWater.addRating(9)
damnKendrick.addRating(8)
damnKendrick.addRating(7)

print(f'''
Book Title      : {atomicHabits.title} 
Author          : {atomicHabits.author}
Pages           : {atomicHabits.pages}
Checked Out     : {atomicHabits.isCheckedOut}
Average Ratings : {atomicHabits.getAverageRating()}
''')

print(f'''
Movie Title       : {avatarWater.title} 
Director          : {avatarWater.director}
Time              : {avatarWater.runTime}
Checked Out       : {avatarWater.isCheckedOut}
Average Ratings   : {avatarWater.getAverageRating()}
''')

print(f'''
CD Title         : {damnKendrick.title} 
Artist           : {damnKendrick.artist}
Songs            : {damnKendrick.songs}
Checked Out      : {damnKendrick.isCheckedOut}
Average Ratings  : {damnKendrick.getAverageRating()}
''')