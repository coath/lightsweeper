
# Lightsweeper additions
from LSApi import LSApi

# individually addressable segment class
# not derived from the API, this only does segment display
class LSEmulateSevenSegment():

    # class vbles - do not change these in objects :)
    backgroundColor = "black"

    def __init__(self, row=0, col=0):
        super(self).__init__()
        # prefer to remove spacing, but at least make it background
        str = "QFrame {{background-color: {0} }}".format(self.backgroundColor)
        self.setStyleSheet(str)
        self.row = row
        self.col = col
        # just a blank thing to paint on
        #self.segments = QWidget()
        #self.segments.setMinimumSize(30, 40)
        # define seven individual segments as color strings
        self.colorA = "white"
        self.colorB = "white"
        self.colorC = "white"
        self.colorD = "white"
        self.colorE = "white"
        self.colorF = "white"
        self.colorG = "white"
        #self.segColors = [self.colorG, self.colorF, self.colorE, self.colorD, self.colorC, self.colorB, self.colorA]
        self.segColors = [self.colorA, self.colorB, self.colorC, self.colorD, self.colorE, self.colorF, self.colorG]
        self.queueColor = "white"
        self.queueDigit = 8
        self.setContentsMargins(0,0,0,0)
        rows = 5 #7
        cols = 5 # 3 #5

    def setSegments(self, segments, setItNow=True):
        #print("SevenSegments.setSegments", segments)

        if segments is not 126:
            print(bin(segments))
        #print(segments & 0b1000000 > 0, segments & 0b0100000 > 0, segments & 0b0010000 > 0, segments & 0b0001000 > 0,
        #      segments & 0b0000100 > 0, segments & 0b0000010 > 0, segments & 0b0000001 > 0)
        colors = []
        colors.append(self.queueColor if segments & 0b1000000 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0100000 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0010000 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0001000 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0000100 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0000010 > 0 else "black")
        colors.append(self.queueColor if segments & 0b0000001 > 0 else "black")
        self.setSegmentsCustom(colors)
        #str = "QWidget {{background-color: {0} }}".format(self.queueColor)
        #for i in range(7):
        #   self.segments[i].setStyleSheet(str)

    def setSegmentsCustom(self, colors):
        print(colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6])
        self.segColors[0] = colors[0]
        self.segColors[1] = colors[1]
        self.segColors[2] = colors[2]
        self.segColors[3] = colors[3]
        self.segColors[4] = colors[4]
        self.segColors[5] = colors[5]
        self.segColors[6] = colors[6]
        str = "QWidget {{background-color: {0} }}".format(self.queueColor)
        for i in range(7):
           self.segments[i].setStyleSheet(str)

    def bin(s):
        return str(s) if s<=1 else bin(s>>1) + str(s&1)

    def flushQueue(self):
        self.display()

    def setColor (self, newColor, setItNow = True):
        #print("setting color to", newColor)
        self.queueColor = newColor
        if setItNow:
            self.display()

    # set immediately or queue these segments in addressed tiles
    # segments is a seven-tuple interpreted as True or False
    #def setSegments(self, row, column, segments, setItNow = True):
        #self.segments.setSegments(segments, setItNow)
        #for i in len(self.segments):
        #    self.segments[i] = segments[i]


	# TODO - split out part of display() to here
	# and make each segment color independent

    def setDigit (self, newDigit, setItNow = True):
        self.queueDigit = newDigit
        if setItNow:
            self.display()

    def display (self):
        if self.queueDigit == " " or self.queueDigit == ".":
            self.queueDigit=8
            self.queueColor="black"

        if self.queueDigit == "-":
            # There is clearly a better way to do this
            segs = LSApi.getDash()
        else:
            segs = LSApi.segMasks[int(self.queueDigit)]  # map digit to segment mask
        for idx in range(len(segs)):
            litSeg = segs[idx]
            if litSeg:
                newColor = self.queueColor
            else:
                newColor = LSEmulateSevenSegment.backgroundColor
            self.segColors[idx] = newColor
            str = "QWidget {{background-color: {0} }}".format(newColor)
            self.segments[idx].setStyleSheet(str)

    def getCol (self):
        return self.col

    def getRow (self):
        return self.row