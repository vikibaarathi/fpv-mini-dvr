from datetime import datetime

class TimeCalculator:
    timeList = []

    def startTimer(self):
        startTime = self.getCurrentTimeInSeconds()
        self.timeList.append(startTime)
        return

    def tag(self):

        return

    def getCurrentTimeInSeconds(self):
        timestamp = datetime.now().timestamp()
        print(timestamp)
        return timestamp
    
