Reference code: https://www.kaggle.com/nachiket273/flower-classification-lookahead-radam

--> Used for training.

1. Installation

   - Python
   - pytorch (torch, torchvision)
   - PIL

   If use Anaconda install torch and torchvision
   $ conda install -c pytorch torchvision

2. Run

```
$ python orai_prediction.py path/to/input_image
```

Example:

```
$ python orai_prediction.py flower_data/train/87/image_05460.jpg
```

Output:

    [('magnolia', 99.99963), ('gaura', 0.0001732754), ('columbine', 3.281055e-05), ('cyclamen', 2.7263155e-05), ('lotus', 2.605411e-05)]

Inference time: 0.306687593460083

Ouput is a list of tuple (recognized name of flower, confidence)

3. Test cases:
   - With labels: flower_data/valid/ ----> subfolder title is the class id; to convert to flower name, use flower_data/cat_to_name.json
   - Without label: flower_data/test
