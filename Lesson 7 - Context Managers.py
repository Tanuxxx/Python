#Without Context Manager
# r = acquire_resource()
# try:
#     do_someting(r)
# finally:
#     release_resource(r)


# With Context Manager
# with acquire_resource() as r:
#     do_something(r)

#Менеджер контекста-  любой класс с методами enter and exit
#Enter инициализирует контекст. Результат записывается в имя, ыказанное после as
#Exit

#tempfile
import tempfile
with tempfile.TemporaryFile() as handle:
    pass

#contextlib
#redirect_stdout in contextlib
#supress in contextli - можно указать какую ошибку нужно подавить
