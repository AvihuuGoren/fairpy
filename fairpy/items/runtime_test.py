import matplotlib.pyplot as plt
import timeit
from fairpy.agents import AdditiveAgent
from course_allocation_by_proxy_auction import course_allocation
# Set up the values of Agents to be tested
ns = [i for i in range(1,300+1)]

execution_times_with_cppyy = []
execution_times_without_cppyy = []
agents = []
for i in ns:
    agents.append(AdditiveAgent({"c1": 1, "c2": 2, "c3": 3,"c4":4}, name=f"{i}"))
    execution_times_with_cppyy.append(timeit.timeit('course_allocation_by_proxy_auction.course_allocation(agents,5,["c1","c2","c3","c4"],4,True)', setup='import course_allocation_by_proxy_auction\nfrom __main__ import agents', number=1))
    execution_times_without_cppyy.append(timeit.timeit('course_allocation_by_proxy_auction.course_allocation(agents,5,["c1","c2","c3","c4"],4,False)', setup='import course_allocation_by_proxy_auction\nfrom __main__ import agents', number=1))

plt.plot(ns, execution_times_with_cppyy, label='with_cppyy')
plt.plot(ns, execution_times_without_cppyy, label='without_cppyy 2')
plt.xlabel('Number of Agents')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.show()
