from reloading import reloading
import time
import matplotlib.pyplot as plt
from original_reloading import reloading as original_reloader

def run_loop(loops, reload_after, original_reloading=False):
    times = []
    if not original_reloading:
        for _ in reloading(range(loops), reload_after=reload_after):
            times.append(time.perf_counter_ns())
    else:
        for _ in original_reloader(range(loops)):
            times.append(time.perf_counter_ns())
    return times


run_loop(10, 1)
labels = []
per_loop = {}
def plot_loop(length, step, reload_after, original_reloading=False):
    labels.append(f"r={reload_after},old={original_reloading}")
    inputs = []
    for loops in range(0,length,step):
        if not(loops == 0 or reload_after == 0):
            start = time.perf_counter_ns()
            times = run_loop(loops, reload_after, original_reloading)
            end = time.perf_counter_ns() - start
            
            per_loop[labels[-1]] = sum(times)/len(times)
            inputs.append((loops,end))

    x, y = zip(*inputs)
    plt.plot(x, y)


plot_loop(500,5, 1, original_reloading=True)
for i in [1,10,50,100]:
    plot_loop(500,5,i)

plt.legend(labels)
plt.xlabel("iterations")
plt.ylabel("nanoseconds")
print("show plot")
plt.show()