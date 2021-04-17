class MaxStack:

    def __init__(self):
        self.main = []
        self.max_in_main = []

    def push(self, data):
        self.main.append(data)

        if self.len_of_main == 1:
            self.max_in_main.append(data)
            return

        temp_variable = self.max_in_main[-1]
        if data > temp_variable:
            self.max_in_main.append(data)
            return
        self.max_in_main.append(temp_variable)

    @property
    def max_item(self):
        return self.max_in_main[-1]

    @property
    def len_of_main(self):
        return len(self.main)


if __name__ == '__main__':
    check = MaxStack()
    check.push(1)
    check.push(10)
    check.push(9)
    print(check.main)
    print(check.max_item)
