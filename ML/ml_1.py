from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()


figure,axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))


for axes, image, target in zip(axes.ravel(), digits.images, digits.target):
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()

plt.show()