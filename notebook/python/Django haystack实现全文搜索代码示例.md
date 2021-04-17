**一、使用的工具**

[ haystack ](http://django-haystack.readthedocs.org/) 是django的开源搜索框架，该框架支持 [
Solr ](http://django-haystack.readthedocs.org/en/v2.4.1/tutorial.html#solr)
,Elasticsearch,Whoosh,*Xapian*搜索引擎，不用更改代码，直接切换引擎，减少代码量。

搜索引擎使用 [ Whoosh ](https://whoosh.readthedocs.org/en/latest/)
，这是一个由纯Python实现的全文搜索引擎，没有二进制文件等，比较小巧，配置比较简单，当然性能自然略低。

中文分词 [ Jieba ](https://github.com/fxsjy/jieba)
，由于Whoosh自带的是英文分词，对中文的分词支持不是太好，故用jieba替换whoosh的分词组件。

其他：Python 3.4.4, Django 1.8.3，Debian 4.2.6_3

**二、配置说明**

现在假设我们的项目叫做Project,有一个myapp的app，简略的目录结构如下。

> - Project  
>  - Project  
>  - settings.py  
>  - blog  
>  - models.py

此models.py的内容假设如下：

```python

    from django.db import models
    from django.contrib.auth.models import User
    class Note(models.Model):
      user = models.ForeignKey(User)
      pub_date = models.DateTimeField()
      title = models.CharField(max_length=200)
      body = models.TextField()
    
      def __str__(self):
        return self.title
```

1. 首先安装各工具 

pipinstall whoosh django-haystack jieba

2. 添加 Haystack 到Django的INSTALLED_APPS 

配置Django项目的settings.py里面的INSTALLED_APPS添加Haystack,例子：

```python

    INSTALLED_APPS = [ 
        'django.contrib.admin',
        'django.contrib.auth', 
        'django.contrib.contenttypes', 
        'django.contrib.sessions', 
        'django.contrib.sites', 
    
         # Added. haystack先添加，
         'haystack', 
         # Then your usual apps... 自己的app要写在haystakc后面
         'blog',
    ]
```

[ 点我看英文原版 ](http://django-
haystack.readthedocs.org/en/v2.4.1/tutorial.html#add-haystack-to-installed-
apps)

3. 修改 你的settings.py，以配置引擎 

本教程使用的是Whoosh，故配置如下：

```python

    import os
    HAYSTACK_CONNECTIONS = {
      'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
      },
    }
```

其中顾名思义，ENGINE为使用的引擎必须要有，如果引擎是Whoosh，则PATH必须要填写，其为Whoosh 索引文件的存放文件夹。

其他引擎的配置见 [ 官方文档 ](http://django-
haystack.readthedocs.org/en/v2.4.1/tutorial.html#configuration)

4.创建索引

如果你想针对某个app例如mainapp做全文检索，则必须在mainapp的目录下面建立search_indexes.py文件，文件名不能修改。内容如下：

```python

    import datetime
    from haystack import indexes
    from myapp.models import Note
    
    class NoteIndex(indexes.SearchIndex, indexes.Indexable):
      text = indexes.CharField(document=True, use_template=True)
      
      author = indexes.CharField(model_attr='user')
      pub_date = indexes.DateTimeField(model_attr='pub_date')
    
      def get_model(self):
        return Note
    
      def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
```

每个索引里面必须有且只能有一个字段为document=True，这代表haystack 和搜索引擎将使用此字段的内容作为索引进行检索(primary
field)。其他的字段只是附属的属性，方便调用，并不作为检索数据。

注意：如果使用一个字段设置了document=True，则一般约定此字段名为text，这是在SearchIndex类里面一贯的命名，以防止后台混乱，当然名字你也可以随便改，不过不建议改。

并且，haystack提供了use_template=True在text字段，这样就允许我们使用数据模板去建立搜索引擎索引的文件，使用方便（官方推荐，当然还有其他复杂的建立索引文件的方式，目前我还不知道），数据模板的路径为yourapp/templates/search/indexes/yourapp/note_text.txt，例如本例子为blog/templates/search/indexes/blog/note_text.txt文件名必须为要索引的类名_text.txt,其内容为

> {{ object.title }}  
>  {{ object.user.get_full_name }}  
>  {{ object.body }}

这个数据模板的作用是对Note.title,Note.user.get_full_name,Note.body这三个字段建立索引，当检索的时候会对这三个字段做全文检索匹配。

5.在URL配置中添加SearchView，并配置模板

在urls.py中配置如下url信息，当然url路由可以随意写。

(r'^search/', include('haystack.urls')),

其实haystack.urls的内容为，

```python

    from django.conf.urls import url
    from haystack.views import SearchView
    
    urlpatterns = [
      url(r'^$', SearchView(), name='haystack_search'),
    ]
```

SearchView()视图函数默认使用的html模板为当前app目录下，路径为myapp/templates/search/search.html  
所以需要在blog/templates/search/下添加search.html文件，内容为

```python

    {% extends 'base.html' %}
    
    {% block content %}
      <h2>Search</h2>
    
      <form method="get" action=".">
        <table>
          {{ form.as_table }}
          <tr>
            <td> </td>
            <td>
              <input type="submit" value="Search">
            </td>
          </tr>
        </table>
    
        {% if query %}
          <h3>Results</h3>
    
          {% for result in page.object_list %}
            <p>
              <a href="{{ result.object.get_absolute_url }}" rel="external nofollow" >{{ result.object.title }}</a>
            </p>
          {% empty %}
            <p>No results found.</p>
          {% endfor %}
    
          {% if page.has_previous or page.has_next %}
            <div>
              {% if page.has_previous %}<a href="?q={{ query }}&page={{ page.previous_page_number }}" rel="external nofollow" >{% endif %}« Previous{% if page.has_previous %}</a>{% endif %}
              |
              {% if page.has_next %}<a href="?q={{ query }}&page={{ page.next_page_number }}" rel="external nofollow" >{% endif %}Next »{% if page.has_next %}</a>{% endif %}
            </div>
          {% endif %}
        {% else %}
          {# Show some example queries to run, maybe query syntax, something else? #}
        {% endif %}
      </form>
    {% endblock %}
```

很明显，它自带了分页。

6.最后一步，重建索引文件

使用python manage.py rebuild_index或者使用update_index命令。

好，下面运行项目，进入该url搜索一下试试吧。

三、下面要做的，使用jieba分词第一步

将文件whoosh_backend.py（该文件路径为python路径/lib/python3.4/site-
packages/haystack/backends/whoosh_backend.py  
）拷贝到app下面，并重命名为whoosh_cn_backend.py，例如blog/whoosh_cn_backend.py。修改如下  
添加from jieba.analyse import ChineseAnalyzer  
修改为如下

> schema_fields[field_class.index_fieldname] =  
>  TEXT(stored=True, analyzer=ChineseAnalyzer(),  
>  field_boost=field_class.boost)

第二步

在settings.py中修改引擎，如下

```python

    import os
    HAYSTACK_CONNECTIONS = {
      'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'
      },
    }
```

第三步

重建索引，在进行搜索中文试试吧。

索引自动更新

如果没有索引自动更新，那么每当有新数据添加到数据库，就要手动执行update_index命令是不科学的。自动更新索引的最简单方法在settings.py添加一个信号。

> HAYSTACK_SIGNAL_PROCESSOR =  
>  "haystack.signals.RealtimeSignalProcessor"

[ 官方文档 ](http://django-
haystack.readthedocs.org/en/v2.4.1/signal_processors.html#realtime-
realtimesignalprocessor)

看了这入门篇，你现在应该大概能配置一个简单的全文搜索了吧，如果想自定义怎么办？ 建议阅读官方文档和github的源码。

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

