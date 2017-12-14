# -*- coding: utf-8 -*-


def dense_neural_net():
    import model_dnn as dnn
    from data import load_data
    x_train, y_train, x_test, y_test = load_data()
    m = dnn.build_model()
    dnn.train(m, x_train, y_train, x_test, y_test, batch_size=128, epochs=20)


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser("MNIST android demo")
    parser.add_argument("-dnn", '--dense_neural_net', action='store_true', help='train dense neural net')

    args = parser.parse_args()

    if args.dense_neural_net:
        dense_neural_net()


if __name__ == '__main__':
    # main()
    dense_neural_net()