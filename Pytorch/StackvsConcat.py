import torch

t1 = torch.tensor([1, 2, 3, 4])
t2 = torch.tensor([5, 6, 7, 8])
t3 = torch.tensor([9, 10, 11, 12])

print(torch.cat((t1.unsqueeze(1), t2.unsqueeze(1), t3.unsqueeze(1)), dim=1))
print(torch.stack((t1, t2, t3), dim=1))
