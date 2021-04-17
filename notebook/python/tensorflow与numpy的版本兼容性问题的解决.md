在Python交互式窗口导入tensorflow出现了下面的错误：

```python

    root@ubuntu:~# python3 
    Python 3.6.8 (default, Oct 7 2019, 12:59:55) 
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tensorflow as tf;
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:516: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint8 = np.dtype([("qint8", np.int8, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:517: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_quint8 = np.dtype([("quint8", np.uint8, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:518: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint16 = np.dtype([("qint16", np.int16, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:519: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_quint16 = np.dtype([("quint16", np.uint16, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:520: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint32 = np.dtype([("qint32", np.int32, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorflow/python/framework/dtypes.py:525: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     np_resource = np.dtype([("resource", np.ubyte, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:541: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint8 = np.dtype([("qint8", np.int8, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:542: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_quint8 = np.dtype([("quint8", np.uint8, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:543: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint16 = np.dtype([("qint16", np.int16, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:544: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_quint16 = np.dtype([("quint16", np.uint16, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:545: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     _np_qint32 = np.dtype([("qint32", np.int32, 1)])
    /usr/local/lib/python3.6/dist-packages/tensorboard/compat/tensorflow_stub/dtypes.py:550: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
     np_resource = np.dtype([("resource", np.ubyte, 1)])
    
```

我的错误原因是numpy的版本较高造成的，换成1.14.0版本后解决了

出错时的Numpy版本

```python

    root@ubuntu:~# pip3 show numpy
    Name: numpy
    Version: 1.17.3
    Summary: NumPy is the fundamental package for array computing with Python.
    Home-page: https://www.numpy.org
    Author: Travis E. Oliphant et al.
    Author-email: None
    License: BSD
    Location: /usr/local/lib/python3.6/dist-packages
    Requires: 
    
```

安装1.14.0的Numpy版本

```

```python

