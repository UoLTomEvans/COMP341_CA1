import torch
import Dataset
import models.CNN
import torch.optim as optim
import argparse
def main():
    parser = argparse.ArgumentParser(description="Training Process")
    # Network structure relevant
    parser.add_argument('--network',type=str,default="CNN",help="Choose network type")

    # Dataset relevant
    parser.add_argument('--path',type=str,help="Path to dataset")
    parser.add_argument('--use-depth',type=int,default=0,help="Use Depth Image in training")
    parser.add_argument('--split',type=float,default=0.9,help="Fraction of dataset as validation")
    parser.add_argument('--epochs',type=int,default=20,help="Number of epochs in training")
    # Maybe more argument can be specified.

    # Take 90% of total dataset as training set.
    train_dataset = Dataset(dataset_path,start=0,end=0.9)
    # Take 10% of total dataset as validation set.
    val_dataset = Dataset(dataset_path,start=0.9,end=1.0)
    train_data = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=1,
        shuffle=False,
        num_workers=4
    )
    print("Data preparation DONE")
    # This should change for step 3's depth pic.
    input_channels = 3
    network = models.CNN
    net = models.CNN(input_channels=3)
    # TODO:better add an if-else for non-cuda user
    device = torch.device("cuda")
    net = net.to(device)
    # This might need to change later
    optimizer = optim.Adam(net.parameters())
    print("Network loading COMPLETE")

    for epoch in range(args.epochs):
        # May add batch number for each epoch
        train_results = train(epoch,net,device,train_data,optimizer)

        test_results = validate(...)

        # Find the best performed network and save it to model file.


    return

# Waiting to complete
def train():
    return
# Waiting to complete
def validate():
    return

if __name__ == '__main__':
    main()