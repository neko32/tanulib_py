from unittest import TestCase, main
from tlib.peripheral import *


class DockerTest(TestCase):
    print(is_localstack_running())


if __name__ == '__main__':
    main()
