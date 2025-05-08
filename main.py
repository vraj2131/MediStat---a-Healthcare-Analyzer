from mediStat.data_loader import DataLoader
from mediStat.structures import Stack, Queue

s = Stack()
s.push(1); s.push(2)
assert s.pop() == 2
assert s.peek() == 1
print(s.__repr__)

q = Queue()
q.enqueue("a"); q.enqueue("b")
assert q.dequeue() == "a"
assert q.peek() == "b"
print(q.__repr__)

# loader = DataLoader()
# df = loader.load_dataframe()
# print(df.head())