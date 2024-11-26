# https://education.yandex.ru/ege/variants/5fc3c948-182b-495f-9d5a-acff30e93c71/task/25

from fnmatch import *
for x in range(0, 10 ** 10, 96437):
  if fnmatch(str(x), "7?2*4??9?"):
    print(x, x // 96437)
