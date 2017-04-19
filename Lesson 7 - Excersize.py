class TestContext:
    def __enter__(self):
        print('I started my work...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('I finished my work!')


class NewTestContext(TestContext):
    def __init__(self):
        self.stdout = []

    def write(self, input):
        try:
            self.stdout + [input]
        except TypeError:
            print('Sorry. Something went wrong')
        else:
            self.stdout.append(input)

    def show(self):
        for str in self.stdout:
            print(str)


with NewTestContext() as tc:
    #tc is the result of method enter, not экземпляр класса
    tc.write('I am inside and working hard')
    tc.write('')
    tc.write('Still working')
    tc.show()


#Написать свой open, можно использовать и готовый open внутри. Вконце редактирования файл exit должен записать,
# кто отредактировал файл
