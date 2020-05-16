class Player:
    def __init__(self, firstName, lastName, p1, p2, posGranted):
        self.firstName = firstName
        self.lastName = lastName
        self.p1 = p1
        self.p2 = p2
        self.posGranted = posGranted

    def getFirstName:
        return firstName
    def getLastName:
        return lastName
    def getPosOne:
        return p1
    def getPosTwo:
        return p2
    def getPosGranted:
        return posGranted

    def setName(player, name):
        player.name = name
    def setPosOne(player, p1):
        player.p1 = p1
    def setPosTwo(player, p2):
        player.p2 = p2

    def printStats:
        print("Name: " + firstName +  " " + lastName + "\n")
        print("Position: " + posGranted + "\n")

    def switchPositionGranted:
        if posGranted == p1:
            posGranted = p2
        elif posGranted == p2:
            posGranted = p1
        
    
        

    
        
