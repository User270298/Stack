class Stack:
    def __init__(self):
        self.lst = []
        self.lenght = 0
        self.size = 5

    def add(self, v):
        self.lenght += 1
        self.lst.append(v)

    def remove(self):
        if self.lenght == 0:
            return
        self.lenght -= 1
        return self.lst.pop()

    def empty_stack(self):
        if self.lenght == 0:
            return True
        return False

    def clear(self):
        self.lenght = 0
        return self.lst.clear()

    def search(self):
        if self.lenght == 0:
            return
        return self.lst[-1]

    def __str__(self):
        return f'{self.lst}'


st = Stack()
st.add('proof')
st.add('prodoof')
st.add('my')
st.add('caver')
st.add('mail')
st.add('peit')
st.remove()
st.remove()
st.remove()
print(st.empty_stack())
print(st.lenght)
print(st)
print(st.search())
st.clear()
print(st.lenght)
