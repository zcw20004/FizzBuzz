# coding=utf-8

class FizzBuzz:
    def __init__(self, fizz, buzz):
        self.fizz = fizz
        self.buzz = buzz

    def checkFizz(self):
        return self.checkIn(self.fizz)

    def checkBuzz(self):
        return self.checkIn(self.buzz)

    def checkIn(self, num):
        if 0 <= num < 10:
            return True
        return False

    def checkNum(self, num, compareNum, flag):
        ret = ''
        if num % compareNum == 0 or num % 10 == compareNum or num / 10 == compareNum:
            ret = flag
        return ret

    def say(self, num):
        ret = self.checkNum(num, self.fizz, 'Fizz')
        ret += self.checkNum(num, self.buzz, 'Buzz')
        if ret == '':
            ret = num

        return ret

    def teacherSay(self):
        for i in xrange(1, 101):
            print self.say(i)

