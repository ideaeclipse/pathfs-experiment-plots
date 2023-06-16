import matplotlib.pyplot as plt


def parse(file):
    data_string = open(file).read().splitlines()
    data_int = list(map(int, data_string))
    return data_int


y1 = parse('batch-results-insert-no-latency.txt')
y2 = parse('batch-results-batch-no-latency.txt')
x = [1, 2]

fig, ax = plt.subplots()

ax.violinplot([y1, y2], positions=x, showmeans=True)
ax.set_xticks(x)
ax.set_xticklabels(['Insert', 'Batch'])
ax.set_ylabel('Milliseconds (ms)')
ax.set_title('50K batch size (155 rows per batch)')

plt.savefig("batch.png")
