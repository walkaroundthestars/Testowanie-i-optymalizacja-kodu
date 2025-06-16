import time
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import accuracy_score

from clearml import Task, Logger

#task = Task.init(project_name="CNN psy", task_name="Trening ResNet")

params = {
    "batch_size": 32,
    "image_size": 224,
    "num_epochs": 10,
    "learning_rate": 0.001,
    "model_name": "resnet50",
    "pretrained": False,
    "dropout": False,
    "transfer_learning": False,
    "normalization": False,
    "augmentation": False,
    "extra_data": False,
}

#task.connect(params)

data_dir = r"C:\Users\przyb\OneDrive\Pulpit\Dogs"

def settings(batch_size=32, image_size=224, augment=False, normalize=False, extra_data=False):
  transform_list = []

  if augment:
    transform_list.extend([
      transforms.RandomHorizontalFlip(),
      transforms.RandomRotation(15),])

  transform_list.append(transforms.Resize((image_size, image_size))),
  transform_list.append(transforms.ToTensor())

  if normalize:
    transform_list.append(transforms.Normalize(mean=[0.5]*3, std=[0.5]*3))

  transform = transforms.Compose(transform_list)
  base_dataset = datasets.ImageFolder(root=data_dir, transform=transform)

  if extra_data:
      dataset_extra = datasets.ImageFolder(root=r"C:\Users\przyb\OneDrive\Pulpit\Dogs_extra", transform=transform)
      full_dataset = torch.utils.data.ConcatDataset([base_dataset, dataset_extra])
  else:
      full_dataset = base_dataset

  train_size = int(0.8 * len(full_dataset))
  val_size = len(full_dataset) - train_size
  train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

  train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
  val_loader = DataLoader(val_dataset, batch_size=batch_size)

  return train_loader, val_loader

def get_model(model_name, num_classes=4, pretrained=False, dropout=False):
    if model_name == 'resnet50':
        model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1 if pretrained else None)
        in_features = model.fc.in_features
        if dropout:
            model.fc = nn.Sequential(
                nn.Dropout(p=0.5),
                nn.Linear(in_features, num_classes)
            )
        else:
            model.fc = nn.Linear(in_features, num_classes)

    elif model_name == 'vgg16':
        model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1 if pretrained else None)
        in_features = model.classifier[6].in_features
        if dropout:
            model.classifier[6] = nn.Sequential(
                nn.Dropout(p=0.5),
                nn.Linear(in_features, num_classes)
            )
        else:
            model.classifier[6] = nn.Linear(in_features, num_classes)

    elif model_name == 'mobilenet_v2':
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1 if pretrained else None)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, num_classes)

    elif model_name == 'inception_v3':
        model = models.inception_v3(weights=models.Inception_V3_Weights.IMAGENET1K_V1 if pretrained else None, aux_logits=False)
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, num_classes)

    else:
        raise ValueError("Unsupported model name")

    if pretrained:
        for param in model.parameters():
            param.requires_grad = False
        for param in model.fc.parameters():
            param.requires_grad = True

    return model

def train(model, train_loader, val_loader, device, num_epochs=5, learning_rate=0.001):
  history = {
      'train_loss': [],
      'train_acc': [],
      'val_loss': [],
      'val_acc': []
  }
  criterion = nn.CrossEntropyLoss()
  optimizer = optim.Adam(model.parameters(), lr=learning_rate)
  model.to(device)

  start_time = time.time()

  for epoch in range(num_epochs):
      model.train()
      train_loss = 0.0
      train_preds = []
      train_labels = []

      for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        train_preds.extend(predicted.cpu().numpy())
        train_labels.extend(labels.cpu().numpy())

      model.eval()
      val_preds = []
      val_labels = []

      with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            val_preds.extend(predicted.cpu().numpy())
            val_labels.extend(labels.cpu().numpy())

      train_acc = accuracy_score(train_labels, train_preds)
      val_acc = accuracy_score(val_labels, val_preds)

      history["train_acc"].append(train_acc)
      history["val_acc"].append(val_acc)

      Logger.current_logger().report_scalar("Accuracy", "Train", train_acc, epoch + 1)
      Logger.current_logger().report_scalar("Accuracy", "Validation", val_acc, epoch + 1)

      print(f"Epoch {epoch+1}/{num_epochs} | Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f} | Val Acc: {val_acc:.4f}")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"\nTime of training: {elapsed_time:.2f} seconds.")
  Logger.current_logger().report_scalar("Time", "Total", elapsed_time, 0)
  return history

#train_loader, val_loader = settings(params["batch_size"], params["image_size"])

#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#model = get_model(params["model_name"], num_classes=4, pretrained=params["pretrained"], dropout=params["dropout"])

#train(model, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])

#Trening na samym CPU bez transfer learningu
#task = Task.init(project_name="CNN psy", task_name="Trening CPU")
#task.connect(params)
#train_loader, val_loader = settings(params["batch_size"], params["image_size"])
#device = torch.device("cpu")
#model_cpu = get_model(params["model_name"], num_classes=4, pretrained=params["pretrained"], dropout=params["dropout"])
#train(model_cpu, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])
#task.close()

#Trening na GPU bez transfer learningu
#task = Task.init(project_name="CNN psy", task_name="Trening GPU")
#task.connect(params)
#train_loader, val_loader = settings(params["batch_size"], params["image_size"])
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model_cpu = get_model(params["model_name"], num_classes=4, pretrained=params["pretrained"], dropout=params["dropout"])
#train(model_cpu, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])
#task.close()

#Trening na CPU z transfer learningiem
#task = Task.init(project_name="CNN psy", task_name="Trening CPU - transfer learning")
#task.connect(params)
#train_loader, val_loader = settings(params["batch_size"], params["image_size"])
#device = torch.device("cpu")
#model_cpu = get_model(params["model_name"], num_classes=4, pretrained=True, dropout=params["dropout"])
#train(model_cpu, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])
#task.close()

#Trening na GPU z transfer learningiem
#task = Task.init(project_name="CNN psy", task_name="Trening GPU - transfer learning")
#task.connect(params)
#train_loader, val_loader = settings(params["batch_size"], params["image_size"])
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model_cpu = get_model(params["model_name"], num_classes=4, pretrained=True, dropout=params["dropout"])
#train(model_cpu, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])
#task.close()

#Trening z dynamicznymi parametrami
task = Task.init(project_name="CNN psy", task_name="Trening pod HPO - GPU + tl")
task.connect(params)
train_loader, val_loader = settings(params["batch_size"], params["image_size"], params["augmentation"], params["normalization"], params["extra_data"])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_cpu = get_model(params["model_name"], num_classes=4, pretrained=True, dropout=params["dropout"])
train(model_cpu, train_loader, val_loader, device, num_epochs=params["num_epochs"], learning_rate=params["learning_rate"])
task.close()
