import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

def main():
    raw_data = load_diabetes()
    data = pd.DataFrame(raw_data.data, columns = raw_data.feature_names)

    print("## BUILDING LINEAR REGRESSION MODEL")
    print("X = BMI")
    print("Y = how much symptom got worse in a year")
    print("This model is trying to draw uni-variation linear regression model \
to explain relationship between decease progression and BMI")

    train_x = raw_data.data
    train_y = raw_data.target
    data_siz, input_siz = train_x.shape

    eta = 0.01

    w = np.random.rand(input_siz) * 1e+3
    b = np.random.rand() * 1e+3

    for _ in range(int(5e+5)):
        rnd = np.random.randint(0, data_siz)
        x = train_x[rnd]
        y = train_y[rnd]

        # linear neuron trigger
        rez = x * w + b
        e = rez - y

        w -= (eta * e * x)
        b -= (eta * e)
    
    print(f"y={w}x+{b}")





if __name__ == '__main__':
    main()