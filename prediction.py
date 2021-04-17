import numpy as np  # linear algebra
import torch
from torchvision import transforms, datasets
from torch import nn
import torch.nn.functional as F
import torchvision.models as models
import os
import pickle
from PIL import Image
import json
from io import BytesIO
import base64


def get_cat_name(index):
    with open('cat_to_name.json', 'r') as f:
        cat_to_name = json.load(f)

    idx_to_class = pickle.load(open("idx_to_class.pkl", "rb"))
    return cat_to_name[idx_to_class[index]]


def main_flower(data_input):
    # Load model
    model = models.resnet50()
    model.fc = nn.Linear(in_features=model.fc.in_features, out_features=102)

    model_name = "saved_models/after_unfreeze_resnet50.pth.tar"

    if torch.cuda.is_available():
        checkpoint = torch.load(model_name)
    else:
        checkpoint = torch.load(model_name, map_location=torch.device('cpu'))

    model.load_state_dict(checkpoint)
    model.eval()

    # read and preprocess one data
    # data_input = data_input.split(",")[-1]
    # input_image = Image.open(BytesIO(base64.b64decode(data_input)))
    input_image = data_input

    preprocess = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        ),
    ])
    input_tensor = preprocess(input_image)
    # create a mini-batch as expected by the model
    input_batch = input_tensor.unsqueeze(0)

    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    # inference
    with torch.no_grad():
        out = model(input_batch)

    percentage = torch.nn.functional.softmax(out, dim=1)[0]*100

    _, indices = torch.sort(out, descending=True)
    indices = indices[0].cpu().numpy()
    percentage = percentage.cpu().numpy()

    result = []
    for idx in indices[:3]:
        score = int(percentage[idx])
        if score > 10:
            result.append({
                "label": get_cat_name(idx),
                "score": score
            })

    print(result)
    return result
