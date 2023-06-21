import matplotlib.pyplot as plt


def parse(file):
    data_string = open(file).read().splitlines()
    data_int = list(map(int, data_string))
    return data_int


y1 = parse('eager-results-1.txt')
y2 = parse('lazy-results-1-1-single.txt')
y3 = parse('lazy-results-1-10-single.txt')
y4 = parse('lazy-results-1-1-multi.txt')
y5 = parse('lazy-results-1-10-multi.txt')
x = [1, 2, 3, 4, 5]

fig, ax = plt.subplots()

ax.violinplot([y1, y2, y3, y4, y5], positions=x)
ax.set_xticks(x)
ax.set_xticklabels(['Eager', 'Single Lazy\n(1ms)', 'Single Lazy\n(10ms)', 'Multi Lazy\n(1ms)', 'Multi Lazy\n(10ms)'])
ax.set_ylabel('Milliseconds (ms)')
ax.set_title('1 Millisecond Delay 5K Writes')

plt.savefig("plot1.png")
plt.show()

fig2, ax2 = plt.subplots()

z1 = parse('eager-results-0.txt')
z2 = parse('lazy-results-0-1-single.txt')
z3 = parse('lazy-results-0-10-single.txt')
z4 = parse('lazy-results-0-1-multi.txt')
z5 = parse('lazy-results-0-10-multi.txt')

ax2.violinplot([z1, z2, z3, z4, z5], positions=x)
ax2.set_xticks(x)
ax2.set_xticklabels(['Eager', 'Single Lazy\n(1ms)', 'Single Lazy\n(10ms)', 'Multi Lazy\n(1ms)', 'Multi Lazy\n(10ms)'])
ax2.set_ylabel('Milliseconds (ms)')
ax2.set_title('0 Millisecond Delay 5K Writes')

plt.savefig("plot2.png")
plt.show()

fig3, ax3 = plt.subplots()

a1 = parse('eager-results-0-semaphore-100.txt')
a2 = parse('lazy-results-0-1-single.txt')
a3 = parse('lazy-results-0-10-single.txt')
a4 = parse('lazy-results-0-1-multi.txt')
a5 = parse('lazy-results-0-10-multi.txt')

ax3.violinplot([a1, a2, a3, a4, a5], positions=x)
ax3.set_xticks(x)
ax3.set_xticklabels(['Eager (100 Max\n Concurrent)', 'Single Lazy\n(1ms)', 'Single Lazy\n(10ms)', 'Multi Lazy\n(1ms)',
                     'Multi Lazy\n(10ms)'])
ax3.set_ylabel('Milliseconds (ms)')
ax3.set_title('0 Millisecond Delay 5K Writes')

plt.savefig("plot3.png")
plt.show()
