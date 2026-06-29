"""
Training Entry Point

Runs the complete ANN training pipeline.
"""

from src.pipeline.train_pipeline import TrainPipeline


def main():

    pipeline = TrainPipeline()

    metrics = pipeline.run()

    print("\nTraining Completed Successfully!\n")

    print(metrics)


if __name__ == "__main__":

    main()