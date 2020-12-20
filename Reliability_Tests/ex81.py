from reliability.Reliability_testing import sequential_samling_chart
test_results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
sequential_samling_chart(p1=0.01, p2=0.10, alpha=0.05,
                         beta=0.10, test_results=test_results)

'''
            Failures to accept Failures to reject
Samples
0                        x                  x
1                        x                  x
2                        x                  2
3                        x                  2
4                        x                  2
5                        x                  2
6                        x                  2
7                        x                  2
8                        x                  2
9                        x                  2
10                       x                  2
11                       x                  2
12                       x                  2
13                       x                  2
14                       x                  2
15                       x                  2
16                       x                  2
17                       x                  2
18                       x                  2
19                       x                  2
20                       x                  3
21                       x                  3
22                       x                  3
23                       x                  3
24                       0                  3
25                       0                  3
26                       0                  3
27                       0                  3
28                       0                  3
29                       0                  3
...                    ...                ...
71                       1                  5
72                       1                  5
73                       1                  5
74                       2                  5
75                       2                  5
76                       2                  5
77                       2                  5
78                       2                  5
79                       2                  5
80                       2                  5
81                       2                  5
82                       2                  5
83                       2                  5
84                       2                  5
85                       2                  5
86                       2                  5
87                       2                  5
88                       2                  5
89                       2                  5
90                       2                  5
91                       2                  5
92                       2                  5
93                       2                  5
94                       2                  5
95                       2                  5
96                       2                  6
97                       2                  6
98                       2                  6
99                       2                  6
100                      3                  6
'''
