#######################
#####  LIBRARIES  #####
from graphics import* #
from math import*     #
#######################


def main():

    
#################### G A T H E R   I N P U T S ##############################################
    
    # Asking for valid window size option.

    winSizes = ['5', '7', '9']

    winSize = input("Give window size: ")  
    while winSize not in winSizes:
        winSize = input("Try again! Valid values are 5, 7 and 9. Give window size: ")

    # Receiving colour by it's first letter.

    coloursToChooseFrom = ["r", "g", "b", "m", "o", "c"]
    print ("Available colours to choose from are: red, green, blue, magenta, orange, cyan. Choose by typing the first letter")

    # Converting letters into colour strings.

    colourX = input("Select colour: ")
    if colourX in coloursToChooseFrom:
        if colourX == "r":
            colour1 = "red"
        elif colourX == "g":
            colour1 = "green"
        elif colourX == "b":
            colour1 = "blue"
        elif colourX == "m":
            colour1 = "magenta"
        elif colourX == "o":
            colour1 = "orange"
        elif colourX == "c":
            colour1 = "cyan"
    else :
        while colourX not in coloursToChooseFrom:
            print("Try again!")
            colourX = input("Select colour: ")
            if colourX == "r":
                colour1 = "red"
            elif colourX == "g":
                colour1 = "green"
            elif colourX == "b":
                colour1 = "blue"
            elif colourX == "m":
                colour1 = "magenta"
            elif colourX == "o":
                colour1 = "orange"
            elif colourX == "c":
                colour1 = "cyan"

    colourY = input("Select colour: ")
    if colourY in coloursToChooseFrom:
        if colourY == "r":
            colour2 = "red"
        elif colourY == "g":
            colour2 = "green"
        elif colourY == "b":
            colour2 = "blue"
        elif colourY == "m":
            colour2 = "magenta"
        elif colourY == "o":
            colour2 = "orange"
        elif colourY == "c":
            colour2 = "cyan"
    else :
        while colourY not in coloursToChooseFrom:
            print("Try again!")
            colourY = input("Select colour: ")
            if colourY == "r":
                colour2 = "red"
            elif colourY == "g":
                colour2 = "green"
            elif colourY == "b":
                colour2 = "blue"
            elif colourY == "m":
                colour2 = "magenta"
            elif colourY == "o":
                colour2 = "orange"
            elif colourY == "c":
                colour2 = "cyan"

    colourZ = input("Select colour: ")
    if colourZ in coloursToChooseFrom:
        if colourZ == "r":
            colour3 = "red"
        elif colourZ == "g":
            colour3 = "green"
        elif colourZ == "b":
            colour3 = "blue"
        elif colourZ == "m":
            colour3 = "magenta"
        elif colourZ == "o":
            colour3 = "orange"
        elif colourZ == "c":
            colour3 = "cyan"
    else :
        while colourZ not in coloursToChooseFrom:
            print("Try again!")
            colourZ = input("Select colour: ")
            if colourZ == "r":
                colour3 = "red"
            elif colourZ == "g":
                colour3 = "green"
            elif colourZ == "b":
                colour3 = "blue"
            elif colourZ == "m":
                colour3 = "magenta"
            elif colourZ == "o":
                colour3 = "orange"
            elif colourZ == "c":
                colour3 = "cyan"
   

    #############################################################################################

    # Converting winSize from String to Integer in order to be used in for statements.

    winSize = int(winSize)
    window = GraphWin("A Patchwork Sampler", winSize*100, winSize*100)

    ############################# P E N U L T I M A T E   P A T C H #############################


    #draw first small square
    g = 0
    h = 0
    j = 20
    k = 20

    z = 5
    x = 5
    c = 5
    v = 15
    r = 5

    # creating first square with it's circles

    p1 = Point(g,h)
    p2 = Point(j, k)
    sS = Rectangle(p1,p2)
    sS.setFill(colour1)
    sS.setOutline(colour1)
    sS.draw(window)

    c1c = Point(z,x)
    c2c = Point(c,v)
    c3c = Point(z + 10, x)
    c4c = Point(c + 10, v)

    c1 = Circle(c1c, r)
    c1.setFill("white")
    c1.setOutline("white")
    c1.draw(window)
    c2 = Circle(c2c, r)
    c2.setFill("white")
    c2.setOutline("white")
    c2.draw(window)
    c3 = Circle(c3c, r)
    c3.setFill("white")
    c3.setOutline("white")
    c3.draw(window)
    c4 = Circle(c4c, r)
    c4.setFill("white")
    c4.setOutline("white")
    c4.draw(window)

    # creating first column

    count = 1

    for i in range(4):
        count = count + 1

        h = h + 20
        k = k + 20

        x = x + 20
        v = v + 20

        p1 = Point(g,h)
        p2 = Point(j, k)
        sS = Rectangle(p1,p2)
        if count%2==0:
            sS.setFill("white")
            sS.setOutline("white")
        elif count%2!=0:
            sS.setFill(colour1)
            sS.setOutline(colour1)
        sS.draw(window)

        c1c = Point(z,x)
        c2c = Point(c,v)
        c3c = Point(z + 10, x)
        c4c = Point(c + 10, v)
        
        c1 = Circle(c1c, r)
        if count%2==0:
            c1.setFill(colour1)
            c1.setOutline(colour1)
        elif count%2!=0:
            c1.setFill("white")
            c1.setOutline("white")
        c1.draw(window)
        c2 = Circle(c2c, r)
        if count%2==0:
            c2.setFill(colour1)
            c2.setOutline(colour1)
        elif count%2!=0:
            c2.setFill("white")
            c2.setOutline("white")
        c2.draw(window)
        c3 = Circle(c3c, r)
        if count%2==0:
            c3.setFill(colour1)
            c3.setOutline(colour1)
        elif count%2!=0:
            c3.setFill("white")
            c3.setOutline("white")
        c3.draw(window)
        c4 = Circle(c4c, r)
        if count%2==0:
            c4.setFill(colour1)
            c4.setOutline(colour1)
        elif count%2!=0:
            c4.setFill("white")
            c4.setOutline("white")
        c4.draw(window)

        




    #creating next square horizontally    
    hCount = 1

    for i in range(4):
        hCount = hCount + 1

        h = h - 80
        k = k - 80

        x = x - 80
        v = v - 80

        g = g + 20
        j = j + 20

        z = z + 20
        c = c + 20

        p1 = Point(g,h)
        p2 = Point(j, k)
        sS = Rectangle(p1,p2)
        if hCount%2==0:
            sS.setFill("white")
            sS.setOutline("white")
        elif hCount%2!=0:
            sS.setFill(colour1)
            sS.setOutline(colour1)
        sS.draw(window)

        c1c = Point(z,x)
        c2c = Point(c,v)
        c3c = Point(z + 10, x)
        c4c = Point(c + 10, v)
        
        c1 = Circle(c1c, r)
        if hCount%2==0:
            c1.setFill(colour1)
            c1.setOutline(colour1)
        elif hCount%2!=0:
            c1.setFill("white")
            c1.setOutline("white")
        c1.draw(window)
        c2 = Circle(c2c, r)
        if hCount%2==0:
            c2.setFill(colour1)
            c2.setOutline(colour1)
        elif hCount%2!=0:
            c2.setFill("white")
            c2.setOutline("white")
        c2.draw(window)
        c3 = Circle(c3c, r)
        if hCount%2==0:
            c3.setFill(colour1)
            c3.setOutline(colour1)
        elif hCount%2!=0:
            c3.setFill("white")
            c3.setOutline("white")
        c3.draw(window)
        c4 = Circle(c4c, r)
        if hCount%2==0:
            c4.setFill(colour1)
            c4.setOutline(colour1)
        elif hCount%2!=0:
            c4.setFill("white")
            c4.setOutline("white")
        c4.draw(window)

        # creating a column of 4 under the top line square 
        vCount = 1

        for i in range(4):
            vCount = vCount + 1

            h = h + 20
            k = k + 20

            x = x + 20
            v = v + 20

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if (hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0):
                sS.setFill("white")
                sS.setOutline("white")
            elif (hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0):
                sS.setFill(colour1)
                sS.setOutline(colour1)
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            if (hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0):
                c1.setFill(colour1)
                c1.setOutline(colour1)
            elif (hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0):
                c1.setFill("white")
                c1.setOutline("white")
            c1.draw(window)
            c2 = Circle(c2c, r)
            if (hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0):
                c2.setFill(colour1)
                c2.setOutline(colour1)
            elif (hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0):
                c2.setFill("white")
                c2.setOutline("white")
            c2.draw(window)
            c3 = Circle(c3c, r)
            if (hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0):
                c3.setFill(colour1)
                c3.setOutline(colour1)
            elif (hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0):
                c3.setFill("white")
                c3.setOutline("white")
            c3.draw(window)
            c4 = Circle(c4c, r)
            if (hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0):
                c4.setFill(colour1)
                c4.setOutline(colour1)
            elif (hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0):
                c4.setFill("white")
                c4.setOutline("white")
            c4.draw(window)

    #######################################################################################################################

    g = 0
    h = 0
    j = 20
    k = 20

    z = 5
    x = 5
    c = 5
    v = 15
    r = 5

    verticalColourCount = 1

    for i in range(winSize - 1):

        verticalColourCount = verticalColourCount + 1

        

        # creating first column

        h = h + 100
        k = k + 100
        x = x + 100
        v = v + 100


        # creating first square with it's circles

        p1 = Point(g,h)
        p2 = Point(j, k)
        sS = Rectangle(p1,p2)
        if verticalColourCount%2==0:
            sS.setFill(colour2)
            sS.setOutline(colour2)
        elif verticalColourCount%2!=0:
            sS.setFill(colour1)
            sS.setOutline(colour1)
        sS.draw(window)

        c1c = Point(z,x)
        c2c = Point(c,v)
        c3c = Point(z + 10, x)
        c4c = Point(c + 10, v)
        
        c1 = Circle(c1c, r)
        c1.setFill("white")
        c1.setOutline("white")
        c1.draw(window)
        c2 = Circle(c2c, r)
        c2.setFill("white")
        c2.setOutline("white")
        c2.draw(window)
        c3 = Circle(c3c, r)
        c3.setFill("white")
        c3.setOutline("white")
        c3.draw(window)
        c4 = Circle(c4c, r)
        c4.setFill("white")
        c4.setOutline("white")
        c4.draw(window)



        #creating vertical small square columns

        count = 1

        for i in range(4):
            count = count + 1

            h = h + 20
            k = k + 20

            x = x + 20
            v = v + 20

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if verticalColourCount%2==0 and count%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            elif verticalColourCount%2==0 and count%2!=0:
                sS.setFill(colour2)
                sS.setOutline(colour2)

            if verticalColourCount%2!=0 and count%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            elif verticalColourCount%2!=0 and count%2!=0:
                sS.setFill(colour1)
                sS.setOutline(colour1)
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            if verticalColourCount%2==0 and count%2==0:
                c1.setFill(colour2)
                c1.setOutline(colour2)
            elif verticalColourCount%2==0 and count%2!=0:
                c1.setFill("white")
                c1.setOutline("white")

            if verticalColourCount%2!=0 and count%2==0:
                c1.setFill(colour1)
                c1.setOutline(colour1)
            elif verticalColourCount%2!=0 and count%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            c1.draw(window)

            c2 = Circle(c2c, r)
            if verticalColourCount%2==0 and count%2==0:
                c2.setFill(colour2)
                c2.setOutline(colour2)
            elif verticalColourCount%2==0 and count%2!=0:
                c2.setFill("white")
                c2.setOutline("white")

            if verticalColourCount%2!=0 and count%2==0:
                c2.setFill(colour1)
                c2.setOutline(colour1)
            elif verticalColourCount%2!=0 and count%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            c2.draw(window)

            c3 = Circle(c3c, r)
            if verticalColourCount%2==0 and count%2==0:
                c3.setFill(colour2)
                c3.setOutline(colour2)
            elif verticalColourCount%2==0 and count%2!=0:
                c3.setFill("white")
                c3.setOutline("white")

            if verticalColourCount%2!=0 and count%2==0:
                c3.setFill(colour1)
                c3.setOutline(colour1)
            elif verticalColourCount%2!=0 and count%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            c3.draw(window)

            c4 = Circle(c4c, r)
            if verticalColourCount%2==0 and count%2==0:
                c4.setFill(colour2)
                c4.setOutline(colour2)
            elif verticalColourCount%2==0 and count%2!=0:
                c4.setFill("white")
                c4.setOutline("white")

            if verticalColourCount%2!=0 and count%2==0:
                c4.setFill(colour1)
                c4.setOutline(colour1)
            elif verticalColourCount%2!=0 and count%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            c4.draw(window)

            

        #creating horizontal small square rows

        smallhorizontalColourCount = verticalColourCount

        hCount = 1

        for i in range(4):

            hCount = hCount + 1
            
            h = h - 80
            k = k - 80

            x = x - 80
            v = v - 80

            g = g + 20
            j = j + 20

            z = z + 20
            c = c + 20

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if smallhorizontalColourCount%2==0 and hCount%2!=0:
                sS.setFill(colour2)
                sS.setOutline(colour2)
            elif smallhorizontalColourCount%2==0 and hCount%2==0:
                sS.setFill("white")
                sS.setOutline("white")

            if smallhorizontalColourCount%2!=0 and hCount%2!=0:
                sS.setFill(colour1)
                sS.setOutline(colour1)
            elif smallhorizontalColourCount%2!=0 and hCount%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            if smallhorizontalColourCount%2==0 and hCount%2==0:
                c1.setFill(colour2)
                c1.setOutline(colour2)
            elif smallhorizontalColourCount%2==0 and hCount%2!=0:
                c1.setFill("white")
                c1.setOutline("white")

            if smallhorizontalColourCount%2!=0 and hCount%2==0:
                c1.setFill(colour1)
                c1.setOutline(colour1)
            elif smallhorizontalColourCount%2!=0 and hCount%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            c1.draw(window)

            c2 = Circle(c2c, r)
            if smallhorizontalColourCount%2==0 and hCount%2==0:
                c2.setFill(colour2)
                c2.setOutline(colour2)
            elif smallhorizontalColourCount%2==0 and hCount%2!=0:
                c2.setFill("white")
                c2.setOutline("white")

            if smallhorizontalColourCount%2!=0 and hCount%2==0:
                c2.setFill(colour1)
                c2.setOutline(colour1)
            elif smallhorizontalColourCount%2!=0 and hCount%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            c2.draw(window)

            c3 = Circle(c3c, r)
            if smallhorizontalColourCount%2==0 and hCount%2==0:
                c3.setFill(colour2)
                c3.setOutline(colour2)
            elif smallhorizontalColourCount%2==0 and hCount%2!=0:
                c3.setFill("white")
                c3.setOutline("white")

            if smallhorizontalColourCount%2!=0 and hCount%2==0:
                c3.setFill(colour1)
                c3.setOutline(colour1)
            elif smallhorizontalColourCount%2!=0 and hCount%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            c3.draw(window)

            c4 = Circle(c4c, r)
            if smallhorizontalColourCount%2==0 and hCount%2==0:
                c4.setFill(colour2)
                c4.setOutline(colour2)
            elif smallhorizontalColourCount%2==0 and hCount%2!=0:
                c4.setFill("white")
                c4.setOutline("white")

            if smallhorizontalColourCount%2!=0 and hCount%2==0:
                c4.setFill(colour1)
                c4.setOutline(colour1)
            elif smallhorizontalColourCount%2!=0 and hCount%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            c4.draw(window)

            # creating a column of 4 under the top line square 
            vCount = 1

            for i in range(4):
                vCount = vCount + 1

                h = h + 20
                k = k + 20

                x = x + 20
                v = v + 20

                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    sS.setFill(colour2)
                    sS.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2!=0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2==0:
                    sS.setFill(colour2)
                    sS.setOutline(colour2)

                if smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    sS.setFill(colour1)
                    sS.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2==0:
                    sS.setFill(colour1)
                    sS.setOutline(colour1)
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c1.setFill(colour2)
                    c1.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c1.setFill(colour2)
                    c1.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2==0:
                    c1.setFill("white")
                    c1.setOutline("white")

                if smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c1.setFill(colour1)
                    c1.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c1.setFill(colour1)
                    c1.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c1.setFill("white")
                    c1.setOutline("white")
                c1.draw(window)
                c2 = Circle(c2c, r)
                if smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c2.setFill(colour2)
                    c2.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c2.setFill(colour2)
                    c2.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2==0:
                    c2.setFill("white")
                    c2.setOutline("white")

                if smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c2.setFill(colour1)
                    c2.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c2.setFill(colour1)
                    c2.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c2.setFill("white")
                    c2.setOutline("white")
                c2.draw(window)
                c3 = Circle(c3c, r)
                if smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c3.setFill(colour2)
                    c3.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c3.setFill(colour2)
                    c3.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2==0:
                    c3.setFill("white")
                    c3.setOutline("white")

                if smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c3.setFill(colour1)
                    c3.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c3.setFill(colour1)
                    c3.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c3.setFill("white")
                    c3.setOutline("white")
                c3.draw(window)
                c4 = Circle(c4c, r)
                if smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif smallhorizontalColourCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c4.setFill(colour2)
                    c4.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c4.setFill(colour2)
                    c4.setOutline(colour2)
                elif smallhorizontalColourCount%2==0 and hCount%2==0 and vCount%2==0:
                    c4.setFill("white")
                    c4.setOutline("white")

                if smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif smallhorizontalColourCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c4.setFill(colour1)
                    c4.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c4.setFill(colour1)
                    c4.setOutline(colour1)
                elif smallhorizontalColourCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c4.setFill("white")
                    c4.setOutline("white")
                c4.draw(window)


    ##################################################################
        g = g - 80
        j = j - 80
        z = z - 80
        c = c - 80

        h = h - 80
        k = k - 80
        x = x - 80
        v = v - 80


        


    #!#!#!#!#!#!#!#!#!!#!#!#!#!!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

    #  H O R I Z O N T A L   P A T C H   A S  A   G R O U P  #####################

    ################################################################################


    g = 0
    h = 0
    j = 20
    k = 20

    z = 5
    x = 5
    c = 5
    v = 15
    r = 5



    rowColumnCount = 1
    
        
    for i in range(winSize - 1):

        

        rowColumnCount = rowColumnCount + 1

        # creaoting first column

        g = g + 100
        j = j + 100
        z = z + 100
        c = c + 100

        #!#!#!#!#!#!#!#!#!!#!#!#!#!!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

        # creating first square with it's circles

        p1 = Point(g,h)
        p2 = Point(j, k)
        sS = Rectangle(p1,p2)
        if rowColumnCount%2==0:
            sS.setFill(colour2)
            sS.setOutline(colour2)
        elif rowColumnCount%2!=0:
            sS.setFill(colour1)
            sS.setOutline(colour1)
        sS.draw(window)

        c1c = Point(z,x)
        c2c = Point(c,v)
        c3c = Point(z + 10, x)
        c4c = Point(c + 10, v)
        
        c1 = Circle(c1c, r)
        c1.setFill("white")
        c1.setOutline("white")
        c1.draw(window)
        c2 = Circle(c2c, r)
        c2.setFill("white")
        c2.setOutline("white")
        c2.draw(window)
        c3 = Circle(c3c, r)
        c3.setFill("white")
        c3.setOutline("white")
        c3.draw(window)
        c4 = Circle(c4c, r)
        c4.setFill("white")
        c4.setOutline("white")
        c4.draw(window)



        square = 1
        columnColour = 1
        count = 1

        for i in range(4):
            square = square + 1
            columnColour = columnColour + 1
            count = count + 1

            h = h + 20
            k = k + 20

            x = x + 20
            v = v + 20



            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if rowColumnCount%2==0 and columnColour%2!=0:
                sS.setFill(colour2)
                sS.setOutline(colour2)
            elif rowColumnCount%2==0 and columnColour%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            
            if rowColumnCount%2!=0 and columnColour%2!=0:
                sS.setFill(colour1)
                sS.setOutline(colour1)
            elif rowColumnCount%2!=0 and columnColour%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            if rowColumnCount%2==0 and count%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            elif rowColumnCount%2==0 and count%2==0:
                c1.setFill(colour2)
                c1.setOutline(colour2)

            if rowColumnCount%2!=0 and count%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            elif rowColumnCount%2!=0 and count%2==0:
                c1.setFill(colour1)
                c1.setOutline(colour1)
            c1.draw(window)

            c2 = Circle(c2c, r)
            if rowColumnCount%2==0 and count%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            elif rowColumnCount%2==0 and count%2==0:
                c2.setFill(colour2)
                c2.setOutline(colour2)

            if rowColumnCount%2!=0 and count%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            elif rowColumnCount%2!=0 and count%2==0:
                c2.setFill(colour1)
                c2.setOutline(colour1)
            c2.draw(window)

            c3 = Circle(c3c, r)
            if rowColumnCount%2==0 and count%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            elif rowColumnCount%2==0 and count%2==0:
                c3.setFill(colour2)
                c3.setOutline(colour2)

            if rowColumnCount%2!=0 and count%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            elif rowColumnCount%2!=0 and count%2==0:
                c3.setFill(colour1)
                c3.setOutline(colour1)
            c3.draw(window)

            c4 = Circle(c4c, r)
            if rowColumnCount%2==0 and count%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            elif rowColumnCount%2==0 and count%2==0:
                c4.setFill(colour2)
                c4.setOutline(colour2)

            if rowColumnCount%2!=0 and count%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            elif rowColumnCount%2!=0 and count%2==0:
                c4.setFill(colour1)
                c4.setOutline(colour1)
            c4.draw(window)

            




            
        hCount = 1

        for i in range(4):
            hCount = hCount + 1

            h = h - 80
            k = k - 80

            x = x - 80
            v = v - 80

            g = g + 20
            j = j + 20

            z = z + 20
            c = c + 20

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if rowColumnCount%2==0 and hCount%2!=0:
                sS.setFill(colour2)
                sS.setOutline(colour2)
            elif rowColumnCount%2==0 and hCount%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            
            if rowColumnCount%2!=0 and hCount%2!=0:
                sS.setFill(colour1)
                sS.setOutline(colour1)
            elif rowColumnCount%2!=0 and hCount%2==0:
                sS.setFill("white")
                sS.setOutline("white")
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            if rowColumnCount%2==0 and hCount%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            elif rowColumnCount%2==0 and hCount%2==0:
                c1.setFill(colour2)
                c1.setOutline(colour2)

            if rowColumnCount%2!=0 and hCount%2!=0:
                c1.setFill("white")
                c1.setOutline("white")
            elif rowColumnCount%2!=0 and hCount%2==0:
                c1.setFill(colour1)
                c1.setOutline(colour1)
            c1.draw(window)

            c2 = Circle(c2c, r)
            if rowColumnCount%2==0 and hCount%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            elif rowColumnCount%2==0 and hCount%2==0:
                c2.setFill(colour2)
                c2.setOutline(colour2)

            if rowColumnCount%2!=0 and hCount%2!=0:
                c2.setFill("white")
                c2.setOutline("white")
            elif rowColumnCount%2!=0 and hCount%2==0:
                c2.setFill(colour1)
                c2.setOutline(colour1)
            c2.draw(window)

            c3 = Circle(c3c, r)
            if rowColumnCount%2==0 and hCount%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            elif rowColumnCount%2==0 and hCount%2==0:
                c3.setFill(colour2)
                c3.setOutline(colour2)

            if rowColumnCount%2!=0 and hCount%2!=0:
                c3.setFill("white")
                c3.setOutline("white")
            elif rowColumnCount%2!=0 and hCount%2==0:
                c3.setFill(colour1)
                c3.setOutline(colour1)
            c3.draw(window)

            c4 = Circle(c4c, r)
            if rowColumnCount%2==0 and hCount%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            elif rowColumnCount%2==0 and hCount%2==0:
                c4.setFill(colour2)
                c4.setOutline(colour2)

            if rowColumnCount%2!=0 and hCount%2!=0:
                c4.setFill("white")
                c4.setOutline("white")
            elif rowColumnCount%2!=0 and hCount%2==0:
                c4.setFill(colour1)
                c4.setOutline(colour1)
            c4.draw(window)

            # creating a column of 4 under the top line square 
            vCount = 1

            for i in range(4):
                vCount = vCount + 1

                h = h + 20
                k = k + 20

                x = x + 20
                v = v + 20

                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if rowColumnCount%2==0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                    sS.setFill("white")
                    sS.setOutline("white")
                elif rowColumnCount%2==0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                    sS.setFill(colour2)
                    sS.setOutline(colour2)

                if rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                    sS.setFill("white")
                    sS.setOutline("white")
                elif rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                    sS.setFill(colour1)
                    sS.setOutline(colour1)
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c1.setFill(colour2)
                    c1.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c1.setFill(colour2)
                    c1.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                    c1.setFill("white")
                    c1.setOutline("white")

                if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c1.setFill(colour1)
                    c1.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c1.setFill(colour1)
                    c1.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c1.setFill("white")
                    c1.setOutline("white")
                c1.draw(window)
                c2 = Circle(c2c, r)
                if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c2.setFill(colour2)
                    c2.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c2.setFill(colour2)
                    c2.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                    c2.setFill("white")
                    c2.setOutline("white")

                if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c2.setFill(colour1)
                    c2.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c2.setFill(colour1)
                    c2.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c2.setFill("white")
                    c2.setOutline("white")
                c2.draw(window)
                c3 = Circle(c3c, r)
                if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c3.setFill(colour2)
                    c3.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c3.setFill(colour2)
                    c3.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                    c3.setFill("white")
                    c3.setOutline("white")

                if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c3.setFill(colour1)
                    c3.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c3.setFill(colour1)
                    c3.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c3.setFill("white")
                    c3.setOutline("white")
                c3.draw(window)
                c4 = Circle(c4c, r)
                if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                    c4.setFill(colour2)
                    c4.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                    c4.setFill(colour2)
                    c4.setOutline(colour2)
                elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                    c4.setFill("white")
                    c4.setOutline("white")

                if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                    c4.setFill(colour1)
                    c4.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                    c4.setFill(colour1)
                    c4.setOutline(colour1)
                elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                    c4.setFill("white")
                    c4.setOutline("white")
                c4.draw(window)

        g = g - 80
        j = j - 80
        z = z - 80
        c = c - 80

        h = h - 80
        k = k - 80
        x = x - 80
        v = v - 80
        

        ######################################################################

        #  R E P S   A S   B L O C K 
        # 
        #  



        #!#!#!#!#!#!#!#!#!!#!#!#!#!!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

        #  Horizontal patches
        
    colourCount = 1
    rowColumnCount = 1
    

    for i in range(winSize - 1):

       

        colourCount = colourCount + 1

        g = g - ((winSize*100)-100)
        j = j - ((winSize*100)-100)
        z = z - ((winSize*100)-100)
        c = c - ((winSize*100)-100)
        
        h = h + 100
        k = k + 100
        x = x + 100
        v = v + 100
        
        

        if colourCount%2!=0:
            colourA = colour2
            colourB = colour1
        elif colourCount%2==0:
            colourA = colour1
            colourB = colour2


        
        

            

        for i in range(winSize - 1):

            

            rowColumnCount = rowColumnCount + 1

            # creaoting first column

            g = g + 100
            j = j + 100
            z = z + 100
            c = c + 100

            #!#!#!#!#!#!#!#!#!!#!#!#!#!!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

            # creating first square with it's circles

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            if rowColumnCount%2==0:
                sS.setFill(colourA)
                sS.setOutline(colourA)
            elif rowColumnCount%2!=0:
                sS.setFill(colourB)
                sS.setOutline(colourB)
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            c1.setFill("white")
            c1.setOutline("white")
            c1.draw(window)
            c2 = Circle(c2c, r)
            c2.setFill("white")
            c2.setOutline("white")
            c2.draw(window)
            c3 = Circle(c3c, r)
            c3.setFill("white")
            c3.setOutline("white")
            c3.draw(window)
            c4 = Circle(c4c, r)
            c4.setFill("white")
            c4.setOutline("white")
            c4.draw(window)



            square = 1
            columnColour = 1
            count = 1

            for i in range(4):
                square = square + 1
                columnColour = columnColour + 1
                count = count + 1

                h = h + 20
                k = k + 20

                x = x + 20
                v = v + 20



                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if rowColumnCount%2==0 and columnColour%2!=0:
                    sS.setFill(colourA)
                    sS.setOutline(colourA)
                elif rowColumnCount%2==0 and columnColour%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                
                if rowColumnCount%2!=0 and columnColour%2!=0:
                    sS.setFill(colourB)
                    sS.setOutline(colourB)
                elif rowColumnCount%2!=0 and columnColour%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if rowColumnCount%2==0 and count%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2==0 and count%2==0:
                    c1.setFill(colourA)
                    c1.setOutline(colourA)

                if rowColumnCount%2!=0 and count%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2!=0 and count%2==0:
                    c1.setFill(colourB)
                    c1.setOutline(colourB)
                c1.draw(window)

                c2 = Circle(c2c, r)
                if rowColumnCount%2==0 and count%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2==0 and count%2==0:
                    c2.setFill(colourA)
                    c2.setOutline(colourA)

                if rowColumnCount%2!=0 and count%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2!=0 and count%2==0:
                    c2.setFill(colourB)
                    c2.setOutline(colourB)
                c2.draw(window)

                c3 = Circle(c3c, r)
                if rowColumnCount%2==0 and count%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2==0 and count%2==0:
                    c3.setFill(colourA)
                    c3.setOutline(colourA)

                if rowColumnCount%2!=0 and count%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2!=0 and count%2==0:
                    c3.setFill(colourB)
                    c3.setOutline(colourB)
                c3.draw(window)

                c4 = Circle(c4c, r)
                if rowColumnCount%2==0 and count%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2==0 and count%2==0:
                    c4.setFill(colourA)
                    c4.setOutline(colourA)

                if rowColumnCount%2!=0 and count%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2!=0 and count%2==0:
                    c4.setFill(colourB)
                    c4.setOutline(colourB)
                c4.draw(window)

                




                
            hCount = 1

            for i in range(4):
                hCount = hCount + 1

                h = h - 80
                k = k - 80

                x = x - 80
                v = v - 80

                g = g + 20
                j = j + 20

                z = z + 20
                c = c + 20

                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if rowColumnCount%2==0 and hCount%2!=0:
                    sS.setFill(colourA)
                    sS.setOutline(colourA)
                elif rowColumnCount%2==0 and hCount%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                
                if rowColumnCount%2!=0 and hCount%2!=0:
                    sS.setFill(colourB)
                    sS.setOutline(colourB)
                elif rowColumnCount%2!=0 and hCount%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if rowColumnCount%2==0 and hCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2==0:
                    c1.setFill(colourA)
                    c1.setOutline(colourA)

                if rowColumnCount%2!=0 and hCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2==0:
                    c1.setFill(colourB)
                    c1.setOutline(colourB)
                c1.draw(window)

                c2 = Circle(c2c, r)
                if rowColumnCount%2==0 and hCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2==0:
                    c2.setFill(colourA)
                    c2.setOutline(colourA)

                if rowColumnCount%2!=0 and hCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2==0:
                    c2.setFill(colourB)
                    c2.setOutline(colourB)
                c2.draw(window)

                c3 = Circle(c3c, r)
                if rowColumnCount%2==0 and hCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2==0:
                    c3.setFill(colourA)
                    c3.setOutline(colourA)

                if rowColumnCount%2!=0 and hCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2==0:
                    c3.setFill(colourB)
                    c3.setOutline(colourB)
                c3.draw(window)

                c4 = Circle(c4c, r)
                if rowColumnCount%2==0 and hCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2==0 and hCount%2==0:
                    c4.setFill(colourA)
                    c4.setOutline(colourA)

                if rowColumnCount%2!=0 and hCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                elif rowColumnCount%2!=0 and hCount%2==0:
                    c4.setFill(colourB)
                    c4.setOutline(colourB)
                c4.draw(window)

                # creating a column of 4 under the top line square 
                vCount = 1

                for i in range(4):
                    vCount = vCount + 1

                    h = h + 20
                    k = k + 20

                    x = x + 20
                    v = v + 20

                    p1 = Point(g,h)
                    p2 = Point(j, k)
                    sS = Rectangle(p1,p2)
                    if rowColumnCount%2==0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                        sS.setFill("white")
                        sS.setOutline("white")
                    elif rowColumnCount%2==0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                        sS.setFill(colourA)
                        sS.setOutline(colourA)

                    if rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                        sS.setFill("white")
                        sS.setOutline("white")
                    elif rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                        sS.setFill(colourB)
                        sS.setOutline(colourB)
                    sS.draw(window)

                    c1c = Point(z,x)
                    c2c = Point(c,v)
                    c3c = Point(z + 10, x)
                    c4c = Point(c + 10, v)
                    
                    c1 = Circle(c1c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c1.setFill(colourA)
                        c1.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c1.setFill(colourA)
                        c1.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c1.setFill("white")
                        c1.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c1.setFill(colourB)
                        c1.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c1.setFill(colourB)
                        c1.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    c1.draw(window)

                    c2 = Circle(c2c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c2.setFill(colourA)
                        c2.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c2.setFill(colourA)
                        c2.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c2.setFill("white")
                        c2.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c2.setFill(colourB)
                        c2.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c2.setFill(colourB)
                        c2.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    c2.draw(window)

                    c3 = Circle(c3c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c3.setFill(colourA)
                        c3.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c3.setFill(colourA)
                        c3.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c3.setFill("white")
                        c3.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c3.setFill(colourB)
                        c3.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c3.setFill(colourB)
                        c3.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    c3.draw(window)
                    c4 = Circle(c4c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c4.setFill(colourA)
                        c4.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c4.setFill(colourA)
                        c4.setOutline(colourA)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c4.setFill("white")
                        c4.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c4.setFill(colourB)
                        c4.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c4.setFill(colourB)
                        c4.setOutline(colourB)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    c4.draw(window)

                    


            g = g - 80
            j = j - 80
            z = z - 80
            c = c - 80

            

            h = h - 80
            k = k - 80
            x = x - 80
            v = v - 80       



    ############################################################
    #   O V E R L A P P I N G   C O L O U R  3   P A T C H E S #
    ############################################################


    h = h - ((winSize*100)-100)
    k = k - ((winSize*100)-100)
    x = x - ((winSize*100)-100)
    v = v - ((winSize*100)-100)



    for i in range(winSize - 2):
        
        g = g - ((winSize*100)-100)
        j = j - ((winSize*100)-100)
        z = z - ((winSize*100)-100)
        c = c - ((winSize*100)-100)
        
        h = h + 100
        k = k + 100
        x = x + 100
        v = v + 100
        


        


            
        for i in range(winSize-2):


            # creating first column

            g = g + 100
            j = j + 100
            z = z + 100
            c = c + 100

            #!#!#!#!#!#!#!#!#!!#!#!#!#!!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

            # creating first square with it's circles

            p1 = Point(g,h)
            p2 = Point(j, k)
            sS = Rectangle(p1,p2)
            sS.setFill(colour3)
            sS.setOutline(colour3)
            sS.draw(window)

            c1c = Point(z,x)
            c2c = Point(c,v)
            c3c = Point(z + 10, x)
            c4c = Point(c + 10, v)
            
            c1 = Circle(c1c, r)
            c1.setFill("white")
            c1.setOutline("white")
            c1.draw(window)
            c2 = Circle(c2c, r)
            c2.setFill("white")
            c2.setOutline("white")
            c2.draw(window)
            c3 = Circle(c3c, r)
            c3.setFill("white")
            c3.setOutline("white")
            c3.draw(window)
            c4 = Circle(c4c, r)
            c4.setFill("white")
            c4.setOutline("white")
            c4.draw(window)




            count = 1

            for i in range(4):
                count = count + 1

                h = h + 20
                k = k + 20

                x = x + 20
                v = v + 20

                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if count%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif count%2!=0:
                    sS.setFill(colour3)
                    sS.setOutline(colour3)
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if count%2==0:
                    c1.setFill(colour3)
                    c1.setOutline(colour3)
                elif count%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                c1.draw(window)
                c2 = Circle(c2c, r)
                if count%2==0:
                    c2.setFill(colour3)
                    c2.setOutline(colour3)
                elif count%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                c2.draw(window)
                c3 = Circle(c3c, r)
                if count%2==0:
                    c3.setFill(colour3)
                    c3.setOutline(colour3)
                elif count%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                c3.draw(window)
                c4 = Circle(c4c, r)
                if count%2==0:
                    c4.setFill(colour3)
                    c4.setOutline(colour3)
                elif count%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                c4.draw(window)

                




                
            hCount = 1

            for i in range(4):
                hCount = hCount + 1

                h = h - 80
                k = k - 80

                x = x - 80
                v = v - 80

                g = g + 20
                j = j + 20

                z = z + 20
                c = c + 20

                p1 = Point(g,h)
                p2 = Point(j, k)
                sS = Rectangle(p1,p2)
                if hCount%2==0:
                    sS.setFill("white")
                    sS.setOutline("white")
                elif hCount%2!=0:
                    sS.setFill(colour3)
                    sS.setOutline(colour3)
                sS.draw(window)

                c1c = Point(z,x)
                c2c = Point(c,v)
                c3c = Point(z + 10, x)
                c4c = Point(c + 10, v)
                
                c1 = Circle(c1c, r)
                if hCount%2==0:
                    c1.setFill(colour3)
                    c1.setOutline(colour3)
                elif hCount%2!=0:
                    c1.setFill("white")
                    c1.setOutline("white")
                c1.draw(window)
                c2 = Circle(c2c, r)
                if hCount%2==0:
                    c2.setFill(colour3)
                    c2.setOutline(colour3)
                elif hCount%2!=0:
                    c2.setFill("white")
                    c2.setOutline("white")
                c2.draw(window)
                c3 = Circle(c3c, r)
                if hCount%2==0:
                    c3.setFill(colour3)
                    c3.setOutline(colour3)
                elif hCount%2!=0:
                    c3.setFill("white")
                    c3.setOutline("white")
                c3.draw(window)
                c4 = Circle(c4c, r)
                if hCount%2==0:
                    c4.setFill(colour3)
                    c4.setOutline(colour3)
                elif hCount%2!=0:
                    c4.setFill("white")
                    c4.setOutline("white")
                c4.draw(window)

                # creating a column of 4 under the top line square 
                vCount = 1

                for i in range(4):
                    vCount = vCount + 1

                    h = h + 20
                    k = k + 20

                    x = x + 20
                    v = v + 20

                    p1 = Point(g,h)
                    p2 = Point(j, k)
                    sS = Rectangle(p1,p2)
                    if rowColumnCount%2==0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                        sS.setFill("white")
                        sS.setOutline("white")
                    elif rowColumnCount%2==0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                        sS.setFill(colour3)
                        sS.setOutline(colour3)

                    if rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2!=0) or (hCount%2!=0 and vCount%2==0)):
                        sS.setFill("white")
                        sS.setOutline("white")
                    elif rowColumnCount%2!=0 and ((hCount%2==0 and vCount%2==0) or (hCount%2!=0 and vCount%2!=0)):
                        sS.setFill(colour3)
                        sS.setOutline(colour3)
                    sS.draw(window)

                    c1c = Point(z,x)
                    c2c = Point(c,v)
                    c3c = Point(z + 10, x)
                    c4c = Point(c + 10, v)
                    
                    c1 = Circle(c1c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c1.setFill(colour3)
                        c1.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c1.setFill(colour3)
                        c1.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c1.setFill("white")
                        c1.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c1.setFill(colour3)
                        c1.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c1.setFill(colour3)
                        c1.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c1.setFill("white")
                        c1.setOutline("white")
                    c1.draw(window)
                    c2 = Circle(c2c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c2.setFill(colour3)
                        c2.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c2.setFill(colour3)
                        c2.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c2.setFill("white")
                        c2.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c2.setFill(colour3)
                        c2.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c2.setFill(colour3)
                        c2.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c2.setFill("white")
                        c2.setOutline("white")
                    c2.draw(window)
                    c3 = Circle(c3c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c3.setFill(colour3)
                        c3.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c3.setFill(colour3)
                        c3.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c3.setFill("white")
                        c3.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c3.setFill(colour3)
                        c3.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c3.setFill(colour3)
                        c3.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c3.setFill("white")
                        c3.setOutline("white")
                    c3.draw(window)
                    c4 = Circle(c4c, r)
                    if rowColumnCount%2==0 and hCount%2!=0 and vCount%2!=0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    elif rowColumnCount%2==0 and hCount%2!=0 and vCount%2==0:
                        c4.setFill(colour3)
                        c4.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2!=0:
                        c4.setFill(colour3)
                        c4.setOutline(colour3)
                    elif rowColumnCount%2==0 and hCount%2==0 and vCount%2==0:
                        c4.setFill("white")
                        c4.setOutline("white")

                    if rowColumnCount%2!=0 and hCount%2!=0 and vCount%2!=0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    elif rowColumnCount%2!=0 and hCount%2!=0 and vCount%2==0:
                        c4.setFill(colour3)
                        c4.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2!=0:
                        c4.setFill(colour3)
                        c4.setOutline(colour3)
                    elif rowColumnCount%2!=0 and hCount%2==0 and vCount%2==0:
                        c4.setFill("white")
                        c4.setOutline("white")
                    c4.draw(window)

            g = g - 80
            j = j - 80
            z = z - 80
            c = c - 80

            h = h - 80
            k = k - 80
            x = x - 80
            v = v - 80  

        g = g + 100
        j = j + 100
        z = z + 100
        c = c + 100




    ################################# F I N A L   P A T C H #####################################

    #winSize = int(winSize)
    #window = GraphWin("A Patchwork Sampler", winSize*100, winSize*100)


    # setting point values as variables so they can be reused
    x = 0
    y = 0

    # creating the outline of first patch in the correct position (top left)
    pStart = Point(x,y)
    pEnd = Point(pStart.getX()+100, pStart.getY()+100)
    square1 = Rectangle(pStart,pEnd)
    square1.draw(window)

    # creating smaller squares in order to create the illusion of the lines within the pattern
    i=1
    for i in range(10):
        pTL = Point(pStart.getX(), pStart.getY() + (i*10))
        pBR = Point(pEnd.getX() - (i*10), pEnd.getY()) 
        squares = Rectangle(pTL, pBR)

        # using the Y coordinate of the bottom right point (pBR) to determin whether it is an even or an odd number,
        # and coloured the appropriate square with the colour needed to complete the patch design
        if pBR.getX()%20 == 0:  
            squares.setFill("white")
            squares.setOutline("white")
        else:
            squares.setFill(colour1)
            squares.setOutline(colour1)
        squares.draw(window)

    # a loop that is excecuted as many times as the number of the window size, to create as many clones of the patch needed, in a diagonal position,
    # using X and Y values from before to set the "new" top left corner point (pStart) of each new patch drawn diagonally.
    
    
    for l in range(winSize-1):
        x = x + 100
        y = y + 100

        pStart = Point(x,y)
        pEnd = Point(pStart.getX()+100, pStart.getY()+100)
        square1 = Rectangle(pStart,pEnd)
        square1.draw(window)

        k=1
        for k in range(10):
            pToLe = Point(pStart.getX(), pStart.getY() + (k*10))
            pBoRi = Point(pEnd.getX() - (k*10), pEnd.getY())
            squares = Rectangle(pToLe, pBoRi)
            if pBoRi.getX()%20 == 0:
                squares.setFill("white")
                squares.setOutline("white")
            else:
                squares.setFill(colour3)
                squares.setOutline(colour3)
            squares.draw(window)

    # creating the outline of first patch in the correct position (top left)
    pStart = Point(winSize*100-100 , winSize*100-100)
    pEnd = Point(pStart.getX()+100, pStart.getY()+100)
    square1 = Rectangle(pStart,pEnd)
    square1.draw(window)

    # creating smaller squares in order to create the illusion of the lines within the pattern
    i=1
    for i in range(10):
        pTL = Point(pStart.getX(), pStart.getY() + (i*10))
        pBR = Point(pEnd.getX() - (i*10), pEnd.getY())
        squares = Rectangle(pTL, pBR)

        # using the Y coordinate of the bottom right point (pBR) to determin whether it is an even or an odd number,
        # and coloured the appropriate square with the colour needed to complete the patch design
        if pBR.getX()%20 == 0:  
            squares.setFill("white")
            squares.setOutline("white")
        else:
            squares.setFill(colour1)
            squares.setOutline(colour1)
        squares.draw(window)

    window.getMouse()

main()