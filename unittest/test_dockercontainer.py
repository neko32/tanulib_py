from unittest import TestCase, main
from tlib.core.container import *


class DockerContainerTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.httpbin_already_running = is_docker_container_running(
            'httpbin_srv')
        if cls.httpbin_already_running:
            stop_container('httpbin')

    def test_is_dockercontainer_running(self):
        self.assertFalse(is_docker_container_running('httpbin_srv'))
        self.assertTrue("httpbin_srv" not in list_running_docker_containers())
        run_container('httpbin')
        self.assertTrue(is_docker_container_running('httpbin_srv'))
        self.assertTrue("httpbin_srv" in list_running_docker_containers())
        self.assertTrue("httpbin_srv" in list_all_docker_containers())

    @classmethod
    def tearDownClass(cls):
        if cls.httpbin_already_running and not is_docker_container_running('httpbin_srv'):
            run_container('httpbin')
        if not cls.httpbin_already_running and is_docker_container_running('httpbin_srv'):
            stop_container('httpbin')


if __name__ == "__main__":
    main()
