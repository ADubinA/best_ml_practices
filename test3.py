import torchvision
import torch
import torch.nn as nn
# Download and load the pretrained ResNet-18.
resnet = torchvision.models.resnet18(pretrained=True)

# If you want to finetune only the top layer of the model, set as below.
for param in resnet.parameters():
    param.requires_grad = False

# Replace the top layer for finetuning.
resnet.fc = nn.Linear(resnet.fc.in_features, 100)  # 100 is an example.

# Forward pass.
print(torch.cuda.is_available())
images = torch.randn(64, 3, 224, 224)
images = images.cuda()
resnet = resnet.cuda()
outputs = resnet(images)
print (outputs.size())     # (64, 100)