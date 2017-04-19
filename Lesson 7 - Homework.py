class Signiture:
    def __init__(self, user_name, file_path):
        self.user_name = user_name
        self.file_path = file_path

    def __enter__(self):
        try:
            self.file = open(self.file_path, 'w')
            return self
        except IOError as err:
            print('Ooops... Unable to open file. Error {0}'.format(err))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.write('\nEdited by {0}\n'.format(str(self.user_name)))
            self.file.close()

    def write(self, text):
        if self.file is not None:
            try:
                self.file.write('{0}\n'.format(text))
            except IOError as err:
                print('Sorry... Can\'t write to the file. Error: {0}'.format())


with Signiture('Grumpy cat', 'C:/Users/Tanuxxx/PycharmProjects/pythonCourses/temp/lesson7_home_work.txt') as sign:
    sign.write('Man: What a nice day, don\'t you think so?')
    sign.write('Grumpy Cat: NO')

