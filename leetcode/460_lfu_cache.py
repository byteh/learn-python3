#https://leetcode.com/problems/lfu-cache/description/

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.frequentQueue = []
        self.storedContent = []

    def initFreqDict(self, key, capacity):
        self.freqDict[key] = 0;

    def incFreq(self,key):
        if(self.freqDict[key]):
            self.freqDict[key] += 1
        # storeKey = key
        # if(storeKey < capacity):
        # for x in range(1, capacity+1):
        #     self.CapacityDict[x] = 0;

    def beforePut(self):
        if (len(self.frequentQueue) >= self.capacity):
            self.frequentQueue.pop(0)
            del

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.beforePut(self)
        self.frequentQueue.append(key)
        self.storedContent[key] = value



        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)