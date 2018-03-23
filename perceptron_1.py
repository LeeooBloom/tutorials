import numpy as np


def main():
    data = init_data()
    weights = init_weights()
    check(data,weights)
    return None


def init_data():
    data = np.matrix('1,0.3,1;'
                     '0.4,0.5,1;'
                     '0.7,0.8,0')
    print data
    return data


def init_weights():
    weights = np.array([0, 0, 0])[np.newaxis]
    print weights.T


def check(data, weights):
    input_count = data.shape[1] - 1
    expected_result = np.copy(data[:,input_count])
    inputs = np.delete(data,1,1)
    print expected_result
    print inputs
    return None


if __name__ == "__main__":
    main()
