from human import Human


class Alice(Human):

    def __init__(self, age=None):
        super(Alice, self).__init__(name='Alice', age=age)

    def execute(self):
        print("execute Alice")
        print("アリスは{}歳だぞ".format(self.age))


if __name__ == '__main__':
    # 単体でうごかすよー
    alice = Alice(19)
    alice.execute()
