from src import mnist_loader, network

if __name__ == '__main__':
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    net = network.Network([784, 50, 50, 50, 50, 50, 50, 50, 50, 10])
    net.SGD(training_data, 300, 1000, 10.0, test_data=test_data)
