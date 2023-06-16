import matplotlib.pyplot as plt


def parse(file):
    data_string = open(file).read().splitlines()
    data_int = list(map(int, data_string))
    return data_int


y1 = parse('eager-results-1.txt')
y2 = parse('lazy-results-1-1.txt')
y3 = parse('lazy-results-1-10.txt')
x = [1, 2, 3]

fig, ax = plt.subplots()

ax.violinplot([y1, y2, y3], positions=x)
ax.set_xticks(x)
ax.set_xticklabels(['Eager', 'Lazy (1ms)', 'Lazy (10ms)'])
ax.set_ylabel('Milliseconds (ms)')
ax.set_title('1 Millisecond Delay 10K Writes')

plt.show()

fig2, ax2 = plt.subplots()

z1 = parse('eager-results-0.txt')
z2 = parse('lazy-results-0-1.txt')
z3 = parse('lazy-results-0-10.txt')

ax2.violinplot([z1, z2, z3], positions=x)
ax2.set_xticks(x)
ax2.set_xticklabels(['Eager', 'Lazy (1ms)', 'Lazy (10ms)'])
ax2.set_ylabel('Milliseconds (ms)')
ax2.set_title('0 Millisecond Delay 5K Writes')

plt.show()

fig3, ax3 = plt.subplots()

a1 = parse('eager-results-0-semaphore-100.txt')
a2 = parse('lazy-results-0-1.txt')
a3 = parse('lazy-results-0-10.txt')

ax3.violinplot([a1, a2, a3], positions=x)
ax3.set_xticks(x)
ax3.set_xticklabels(['Eager (100 Max Outgoing)', 'Lazy (1ms)', 'Lazy (10ms)'])
ax3.set_ylabel('Milliseconds (ms)')
ax3.set_title('0 Millisecond Delay 5K Writes')

plt.show()
