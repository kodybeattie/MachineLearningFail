class StopLight(object):
    """This is a class that represents a stop light"""
    # PROPERTIES
    # ================  
    # INTERSECTION NUMBER
    # TRAFFIC FLOW
    # STATE - RED, YELLOW OR GREEN
    #
    #
    def __init__(self):
        pass
    
    def __init__(self, interNum, traFlow, state, spr):
        self.intersection = interNum
        self.trafficFlow = traFlow
        self.currState = state
        self.sprite = spr
        self.sprite.scale = 0.1

        if self.intersection == 0:
            if self.trafficFlow == 0:
                self.sprite.x = 150
                self.sprite.y = 510
                self.sprite.rotation = 90
            if self.trafficFlow == 1:
                self.sprite.x = 90
                self.sprite.y = 570
                self.sprite.rotation = 270
            if self.trafficFlow == 2:
                self.sprite.x = 150
                self.sprite.y = 570
            if self.trafficFlow == 3:
                self.sprite.x = 90
                self.sprite.y = 510
                self.sprite.rotation = 180
        if self.intersection == 1:
            if self.trafficFlow == 0:
                self.sprite.x = 730
                self.sprite.y = 510
                self.sprite.rotation = 90
            if self.trafficFlow == 1:
                self.sprite.x = 670
                self.sprite.y = 570
                self.sprite.rotation = 270
            if self.trafficFlow == 2:
                self.sprite.x = 730
                self.sprite.y = 570
            if self.trafficFlow == 3:
                self.sprite.x = 670
                self.sprite.y = 510
                self.sprite.rotation = 180
        if self.intersection == 2:
            if self.trafficFlow == 0:
                self.sprite.x = 1460
                self.sprite.y = 510
                self.sprite.rotation = 90
            if self.trafficFlow == 1:
                self.sprite.x = 1400
                self.sprite.y = 570
                self.sprite.rotation = 270
            if self.trafficFlow == 2:
                self.sprite.x = 1460
                self.sprite.y = 570
            if self.trafficFlow == 3:
                self.sprite.x = 1400
                self.sprite.y = 510
                self.sprite.rotation = 180
            

            

