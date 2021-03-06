# 建立稳定的视频分析服务

这是一个针对生产环境设计的例子。

- 数据（图片）采集
- 人工对机器分类好的图片，结合你的实际情况，进行二次分类
- 分类好的数据集 -> 训练好的模型
- 应用你的模型

假设你目前有两个视频 `train.mp4` 与 `predict.mp4` 分别用于训练模型与校验模型。

## 数据（图片）采集

在运行 `cut.py` 之后，你将可以得到 `cut_result` 文件夹，里面有分类好的图片。

参见 [cut.py](./cut.py)。

![structure](https://user-images.githubusercontent.com/13421694/64073910-e8a97c80-ccd6-11e9-9847-39c3a4d277c3.png)

## 二次分类

人工对机器分类好的图片，结合你的实际情况，进行二次分类。具体参见 [issue#48](https://github.com/williamfzc/stagesepx/issues/48)。

## 模型训练

经过上述步骤后，你现在应该有一个符合业务需求的、分类完好的训练（图片）集（文件夹）。接下来我们会基于它构建一个模型。

如何训练参见 [train.py](./train.py)。

## 应用

之后你就可以利用训练好的模型，对类似的视频进行预测。

如何使用模型参见 [predict.py](./predict.py)
