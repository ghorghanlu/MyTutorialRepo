from sklearn.utils import shuffle
import torch.nn as nn
import torch
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.tensorboard import SummaryWriter


torch.set_printoptions(linewidth=120)
torch.set_grad_enabled(True)

def get_num_correct(preds, labels):
    return preds.argmax(dim=1).eq(labels).sum().item()


class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)

        self.fc1 = nn.Linear(in_features=12*4*4, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=10)

    def forward(self, t):

        t = F.relu(self.conv1(t))
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        t = F.relu(self.conv2(t))
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        t = F.relu(self.fc1(t.reshape(-1, 12*4*4)))
        t = F.relu(self.fc2(t))
        t = self.out(t)
        return t


train_set = torchvision.datasets.FashionMNIST(
    root='./data/FashionMNIST',
    train=True,
    download=True,
    transform=transforms.Compose([transforms.ToTensor()]))

batch_size_list = [100, 1000, 10000]
lr_list = [0.01, 0.001, 0.0001, 0.00001]

for batch_size in batch_size_list:
    for lr in lr_list:
        network = Network()
        train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
        optimizer = optim.Adam(network.parameters(), lr=lr)

        images, labels = next(iter(train_loader))
        grid = torchvision.utils.make_grid(images)

        comment = f"batch_size = {batch_size}, lr = {lr}"
        tb = SummaryWriter(comment=comment)
        tb.add_image("images", grid)
        tb.add_graph(network, images)
        
        for epoch in range(5):
            total_loss = 0
            total_correct = 0
            for batch in train_loader:
                images, labels = batch

                preds = network(images)
                loss = F.cross_entropy(preds, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item() * batch_size
                total_correct += get_num_correct(preds, labels)
            
            tb.add_scalar("Loss", total_loss, epoch)
            tb.add_scalar("Correct Number", total_correct, epoch)
            tb.add_scalar("accuracy", total_correct/len(train_set), epoch)
            # tb.add_histogram("conv1.bias", network.conv1.bias, epoch)
            # tb.add_histogram("conv1.weight", network.conv1.weight, epoch)
            # tb.add_histogram("conv1.weight.grad", network.conv1.weight.grad, epoch)
            for name, weight in network.named_parameters():
                tb.add_histogram(name, weight, epoch)
                tb.add_histogram(f"{name}.grad", weight, epoch)


            print("epoch:", epoch, "total_correct:", total_correct, "total_loss:", total_loss, "accuracy:", total_correct/len(train_set))

        tb.close()
