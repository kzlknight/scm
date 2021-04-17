ppt通过其精美的可视化技巧以及良好的演示效果，成为了职场人士的必备技能。ppt的设计是一门大学问，无论是设计技巧，还是操作方法，都衍生出了专门的课程。

本文主要介绍python操作ppt的技巧，编程的优势在于处理速度，对于高大上的ppt设计，还是需要"以人为本",
所以该模块的使用场景主要是ppt基本元素的提取和添加，适合大量内容的转化，比如word转ppt,
减少大量繁琐的人工操作，尽管提供了一些基本的样式设计，但是并不能满足日常办公对ppt美观性的要求。

在该模块中，将ppt拆分为了以下多个元素

1. presentations, 表示整个ppt文档 

2. sliders. 表示ppt文档的每一页 

3. shapes 

4. placeholders 

上述分类对应的常用操作如下

**1. presentations**

用于打开，创建，保存ppt文档，用法如下

```python

    >>> from pptx import Presentation
    # 创建新的ppt文档
    >>> prs = Presentation()
    # 打开一个ppt文档
    >>> prs = Presentation('input.pptx')
    # 保存ppt文档
    >>> prs.save('test.pptx')
```

**2. slides**

在创建一页ppt时，需要指定对应的布局，在该模块中， 内置了以下9种布局

1. Title 

2. Title and Content 

3. Section Header 

4. Two Content 

5. Comparison 

6. Title Only 

7. Blank 

8. Content with Caption 

9. Picture with Caption 

通过数字下标0到9来访问，指定布局添加一页ppt的用法如下

```python

    >>> title_slide_layout = prs.slide_layouts[0]
    >>> slide = prs.slides.add_slide(title_slide_layout)
```

**3. shapes**

shapes表示容器，在制作ppt时，各种基本元素，比如文本框，表格，图片等都占据了ppt的一个部分，或者矩形区域，或者其他各种自定义的形状。shapes表示所有基本元素的和，
通过如下方式来访问对应的shapes

```python

    shapes = slide.shapes
```

对于shapes而言，我们可以获取和设置其各种属性，比如最常用的text属性，用法如下

```python

    >>> shapes.text = 'hello world'
```

还可以通过add系列方法来添加各种元素，添加文本框的方法如下

```python

    >>> from pptx.util import Inches, Pt
    >>> left = top = width = height = Inches(1)
    >>> txBox = slide.shapes.add_textbox(left, top, width, height)
    >>> tf = txBox.text_frame
    >>> tf.text = "first paragraph"
    >>> p = tf.add_paragraph()
    >>> p.text = "second paragraph"
```

添加表格的方法如下

```python

    >>> rows = cols = 2
    >>> left = top = Inches(2.0)
    >>> width = Inches(6.0)
    >>> height = Inches(0.8)
    >>> table = shapes.add_table(rows, cols, left, top, width, height).table
    >>> table.columns[0].width = Inches(2.0)
    >>> table.columns[1].width = Inches(4.0)
    >>> # write column headings
    >>> table.cell(0, 0).text = 'Foo'
    >>> table.cell(0, 1).text = 'Bar'
```

**4. placeholders**

shapes表示所有基本元素的总和，而placeholders则表示每一个具体的元素，所以placeholders是shapes的子集，
通过数字下标来访问对应的placeholder，用法如下

```python

    >>> slide.placeholders[1]
    <pptx.shapes.placeholder.SlidePlaceholder object at 0x03F73A90>
    >>> slide.placeholders[1].placeholder_format.idx
    1
    >>> slide.placeholders[1].name
    'Subtitle 2'
```

placeholders是页面上已有的元素，获取对应的placeholders之后，可以通过insert系列方法来向其中新添元素。

了解上述层级结构，有助于我们对ppt的读写操作。除了写操作之外，也可以通过读操作来批量提取ppt中的特定元素，以文字为例，提取方式如下

```python

    from pptx import Presentation
     
    prs = Presentation(path_to_presentation)
     
    text_runs = []
     
    for slide in prs.slides:
     for shape in slide.shapes:
      if not shape.has_text_frame:
       continue
      for paragraph in shape.text_frame.paragraphs:
       for run in paragraph.runs:
        text_runs.append(run.text)
```

通过该模块，可以快速搭建ppt的基本框架，也可以批量提取ppt中的特定元素，比如提取文字转换成word,
或者提取表格转换成excel文件。总而言之，该模块适合替代大量繁琐的人工复制粘贴操作。

到此这篇关于通过python-pptx模块操作ppt文件的方法的文章就介绍到这了,更多相关python-
pptx模块操作ppt文件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

