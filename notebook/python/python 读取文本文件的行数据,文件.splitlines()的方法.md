一般跟踪训练的ground_truth的数据保存在文本文文件中,故每一行的数据为一张图片的标签数据,这个时候读取每一张图片的标签，具体实现如下：

```python

    test_txt = '/home/zcm/tensorf/siamfc-tf-master/data/Biker/groundtruth.txt'
    def load_label_set(label_dir):
     label_folder = open(label_dir, "r")
     trainlines = label_folder.read().splitlines() #返回每一行的数据
     for line in trainlines:
     line = line.split(" ") #按照空格键分割每一行里面的数据
     box = [float(line[0]), float(line[1]), float(line[2]), float(line[3])]#box读取标签ground_truth
     label_folder.close()
    
     return train_box
    #train_box = load_train_test_set(test_txt)
    
```

以上这篇python
读取文本文件的行数据,文件.splitlines()的方法就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

