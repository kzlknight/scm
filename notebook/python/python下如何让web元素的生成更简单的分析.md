1. 引用css。这可能是最常见的做法了，对一些特定的元素定义特定的样式。那么使用它，你需要在HTML   
页面中加入<link>标签。  
2. 引入js。许多特效也可以通过javascript来进行处理，比如动态显示效果，或对元素进行封装。使用   
它你需要在HTML页面加入<script>标签，必要时还要加一些javascript代码。  
3. HTML元素。需要设定一些特殊的属性，比如class=某个属性。这块还相对简单。   
  
因此从上面的分析可以看出，在通常情况下，加入一个好看的web元素可能到许多地方的修改。因此我一  
直在思考如何让这个过程可以更简化，麻烦的地方就是如何处理这些资源，如何让这些资源可以与原始的  
HTML很好的结合呢？最终我想出的办法就是：代码组装。  
  
对于css, javascript链接和代码，它们可以按调用的顺序依次拼成一段文本，然后插入到</head>元素前  
面。然后对于html代码，在模板中直接输出。对于css, javascript的链接可以检查是否重复。  
  
那么如何定义web元素类和如何在模板中对其进行处理？  
  
一个web元素类定义如下：  
  
class Snippet(object):  
css = ''  
csslink = ''  
jslink = ''  
html = ''  
js = ''  
  
def render(self):  
return ''  
  
def __str__(self):  
return self.render()  
  
定义为类属性的将输出到HTML的头部，而render()的结果将显示在模板中调用类的地方。先看一下在模板  
中调用的示例：  
  
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"  
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
<html xmlns="http://www.w3.org/1999/xhtml">  
<head>  
<title>HTML Helper</title>  
<script type="text/javascript" src="/static/js/jquery.js"></script>  
</head>  
<body>  
{{  
htmlbuf << htmlwidgets.Message('This is a test')  
}}  
</body>  
</html>  
  
这里你可以看到htmlbuf，它是什么，它就是用来采集每个Snippet类的类属性的。这里使用<<来将一个  
Snippet对象加到htmlbuf中去。同时它还会将Snippet的HTML代码在调用位置输出。  
  
如何输出？首先uliweb的模板将转为python代码，它有一个内置的out对象，可以调用它的方法来输出  
HTML代码。那么htmlbuf对象将在调用模板前被创建，在调用模板后被处理，在创建时将传入out的write  
属性。这一切都是在SImpleFrame.py中通过plugin方法来实现的，但是这只是定义了一个调用点，如：  
  
fname, code = template.render_file(filename, vars, env, dirs)  
out = template.Out()  
template._prepare_run(vars, env, out)  
callplugin(self, 'before_render_template', env, out)  
  
if isinstance(code, (str, unicode)):  
code = compile(code, fname, 'exec')  
exec code in env, vars  
text = out.getvalue()  
output = execplugin(self, 'after_render_template', text, vars, env)  
  
before_render_template 会在调用模板前被调用。after_render_template 会在调用模板后被调用。因  
此你可以通过plugin机制来加入额外的处理。这是在settings.py中定义的，如：  
  
@plugin('before_render_template')  
def before_render_template(sender, env, out):  
from uliweb.core import js  
from uliweb.core.SimpleFrame import url_for  
from uliweb.helpers import htmlwidgets  
  
htmlbuf = js.HtmlBuf(write=out.noescape,
static_suffix=url_for('Portal.views.static',  
filename=''))  
env['htmlbuf'] = htmlbuf  
env['htmlwidgets'] = htmlwidgets  
  
这里注入htmlbuf和htmlwidgets到模板的env环境中，所以可以在模板中直接使用。在htmlwidgets中已经  
定义了一些Snippet。htmlbuf在创建时，会使用out.noescape方法，它将不会对Snippet中的代码进行转  
义。static_suffix表示静态文件的前缀，缺省为/static/，这里由于使用了静态服务，所以通过url_for  
来得到静态URL前缀。  
  
@plugin('after_render_template')  
def after_render_template(sender, text, vars, env):  
import re  
r_links =
re.compile('<link\s.*?\shref\s*=\s*"?(.*?)["\s>]|<script\s.*?\ssrc\s*=\s*"?  
(.*?)["\s>]', re.I)  
if 'htmlbuf' in env:  
htmlbuf = env['htmlbuf']  
if htmlbuf.modified:  
b = re.search('(?i)</head>', text)  
if b:  
pos = b.start()  
#find links  
links = [x or y for x, y in r_links.findall(text[:pos])]  
htmlbuf.remove_links(links)  
t = htmlbuf.render()  
if t:  
return ''.join([text[:pos], t, text[pos:]])  
else:  
return t+text  
return text  
  
这里将在模板处理完毕后查找生成的HTML文本中的</head>标签，然后将相应的信息插入到它的前面。同  
时这里增加了对原HTML中已经存在的链接进行了判断，如果存在则删除之，这是通过remove_links来处理  
的。  
  
经过这些的处理，你只要定义一个Snippet，Uliweb将自动为你处理css, js的链接包括代码，和HTML代码  
的生成。因此你就可以简单的：  
  
{{  
htmlbuf << htmlwidgets.Message('This is a test')  
}}  
  
来生成一个消息的提示信息。  
  
我会慢慢扩展这个htmlwidgets库。  
  
再简单描述一下如何配置：  
  
1. 在settings.py中   
  
INSTALLED_APPS = ['Documents', 'Examples', 'Portal', 'Post',  
'uliweb.builtins.auth', 'uliweb.helpers.htmlwidgets']  
  
这里要加入'uliweb.helpers.htmlwidgets'，让static目录生效  
  
2. 加入：   
  
@plugin('before_render_template')  
def before_render_template(sender, env, out):  
  
和  
  
@plugin('after_render_template')  
def after_render_template(sender, text, vars, env):  
  
3. 可以使用了。   
  

