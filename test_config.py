from src.configuration import ConfigurationManager

config = ConfigurationManager()

training = config.get_training_config()

print(training)

print(training.epochs)

print(training.batch_size)