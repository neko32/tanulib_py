from tlib.ml import *
from unittest import TestCase, main
import numpy as np

class MLBaseTest(TestCase):

    def test_gpu_available(self):
        rez = get_available_gpu_devices()
        print(rez)
        self.assertTrue(True)    

    def test_simple_linear_model_gen(self):
        mb = ModelBuilder([3,])
        mb.set_output(1, 'linear')
        x = np.random.uniform(size = [1000, 3], low = -1., high = 1.)
        y = np.sum(x, axis = 1) / 3
        t_x = np.array([[10., 20., 30.], [100., 50., 40.]])
        t_y = np.sum(t_x, axis = 1) / 3
        m = mb.build()
        sgd = gen_default_SGD()
        m.summary()
        m.compile(optimizer = sgd, loss = 'mse', metrics = ['accuracy'])
        m.fit(x, y, epochs = 100)
        r = m.predict(t_x)
        rr = np.sum(r, axis = 1)
        print(rr)
        print(t_y)

if __name__ == "__main__":
    main()

