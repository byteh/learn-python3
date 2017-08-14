 #!/usr/bin/python
 #coding:utf-8

#1.初始化两个句子
st_1 = "dogs chase cats like dogs ."
st_2 = "dogs hate cats like cats !"

#2.从字符串中创建词的集合
st_1_words = set(st_1.split())
st_2_words = set(st_2.split())

#3.找出每个集合中不重复的词总数，即词表大小
no_words_st_1 = len(st_1_words)
no_words_st_2 = len(st_2_words)

#4.找出两个集合中共有的词，保存到列表中，并统计总数.交集
cmn_words = st_1_words.intersection(st_2_words)
no_cmn_words = len(st_1_words.intersection(st_2_words))

#5.找出两个集合并集中不重复的词，保存到列表中，并统计总数
unq_words = st_1_words.union(st_2_words)
no_unq_words = len(st_1_words.union(st_2_words))

#6.计算Jaccard相似度.给定两个集合A,B，Jaccard 系数定义为A与B交集的大小与A与B并集的大小的比值.比较文本相似度，用于文本查重与去重；计算对象间距离，用于数据聚类等
similarity = no_cmn_words / (1.0 * no_unq_words)

#6.output
print "No words in sent_1 = %d "%(no_words_st_1)
print "Sentence 1 words =",st_1_words
print "No words in sent_2=%d"%(no_words_st_2)
print "Sentence 2 words =",st_2_words
print "No words in common= %d "%(no_cmn_words)
print "Common words =",cmn_words
print "Total unique words = %d "%(no_unq_words)
print "Unique words =",unq_words
print "Similarity = No words in common/No unique words, %d/%d = %.2f"%(no_cmn_words,no_unq_words, similarity)
