#有一个列表，其中包括 10 个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。最终样式是[2,3,4,5,6,7,8,9,0,1]

#!/usr/bin/env python
# coding=utf-8

opponents = [1,2,3,4,5,6,7,8,9,0]
print opponents

b = opponents.pop(0)
opponents.append(b)
print opponents
