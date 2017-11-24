#https://leetcode.com/problems/lfu-cache/description/
import time

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "%s --- capacity[%d] --- "%(curTime, capacity)
        self.capacity = capacity
        self.frequentQueue = []  #list
        self.storedContent = {}  #dict

    def beforePut(self,key):
        if (key not in self.frequentQueue and len(self.frequentQueue) >= self.capacity):
            popKey = self.frequentQueue.pop(0)
            del self.storedContent[popKey]
        self.updateFrequent(key)


    def updateFrequent(self,key):
        for index in range(len(cache.frequentQueue) - 1):
            if cache.frequentQueue[index] == key:
                del cache.frequentQueue[index]
        if(key not in self.frequentQueue):
            self.frequentQueue.append(key)

    def afterGet(self, key):
        queueLen = len(self.frequentQueue)
        if (queueLen > self.capacity):
            self.frequentQueue.pop(0)
        else:
            self.updateFrequent(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.storedContent:
            value = self.storedContent[key]
            self.afterGet(key)
        else:
            value = -1
        print "get key=%d value=%d" % (key, value)
        print "  content:",cache.storedContent
        print "  frequent:",cache.frequentQueue
        print "\n"
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print "put key=%d value=%d" %(key,value)
        self.beforePut(key)
        self.storedContent[key] = value
        print "  content:",cache.storedContent
        print "  frequent:",cache.frequentQueue


        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.get(3)       # returns 3.
cache.put(4, 4)    # evicts key 1.
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
exit()

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(1)
cache.put(1, 10)
cache.get(2)
cache.get(1)
cache.get(3)
# exit()
cache.put(4, 4)
cache.put(5, 55)
cache.get(1)
cache.get(2)
cache.get(3)
cache.get(4)