from . import Human


class Bob(Human):

    def __init__(self, age=None):
        super(Bob, self).__init__(name='Bob', age=age)

    def execute(self):
        print("execute Bob")
        print("ボブは{}歳だぞ".format(self.age))


if __name__ == '__main__':
    # 単体でうごかすよー
    bob = Bob(21)
    bob.execute()
