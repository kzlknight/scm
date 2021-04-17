最近在做一个仿知乎网站的项目了，里面涉及很多图片和文件上传。趁此机会我给大家总结下Django自定义图片和文件上传路径的2种方式吧。

**方法1: 在Django模型中定义upload_to选项。**

Django模型中的ImageField和FileField的upload_to选项是必填项，其存储路径是相对于MEIDA_ROOT而来的。

我们来看一个简单案例（如下所示)。如果你的MEDIA_ROOT是/media/文件夹，而你的上传文件夹upload_to=“avatar",
那么你上传的文件会自动存储到/media/avatar/文件夹。

```python

    class UserProfile(models.Model):
     
      user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
      avatar = models.ImageField(upload_to='avatar', verbose_name="头像")
    
```

如果你的文件名是sky.jpg, 那么图片上传后数据库中的avatar字段为avatar/sky.jpg,
该字段指向图片对象，而非绝对路径。要在模板中使用该图片，应该使用avatar.url (即/media/avatar/sky.jpg）。

但在实际应用中，请千万别这么做。这里有2个严重问题。

  * 所有用户都把头像上传到了同一个avatar文件夹了 
  * 原文件名是什么，那么新文件名就是什么 

试想用户很多，很可能发生文件重名问题，造成后来用户上传的文件把前面用户上传的头像覆盖了，造成了用户A挂用户B头像的状况。

正确的做法是动态定义上传路径，把图片存储到用户自己的文件夹下，并对其重命名。如下图所示。这样图片就会保存在/media/1/avatar/里了，而且文件以uuid命名。

```python

    from django.db import models
    from django.contrib.auth.models import User
    import uuid
     
    # Create your models here.
     
    def user_directory_path(instance, filename):
      ext = filename.split('.')[-1]
      filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
      # return the whole path to the file
      return "{0}/{1}/{2}".format(instance.user.id, "avatar", filename)
     
    class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
      avatar = models.ImageField(upload_to=user_directory_path, verbose_name="头像")
    
```

上述案例显然还有一个问题，不同系统路径分隔符/和\是不一样的，为保证代码在不同系统中能重用，更好的方式是使用python的os模块来拼接路径。如下图所示。

```python

    from django.db import models
    from django.contrib.auth.models import User
    import uuid
    import os
     
    # Create your models here.
     
    def user_directory_path(instance, filename):
      ext = filename.split('.')[-1]
      filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
      # return the whole path to the file
      return os.path.join(instance.user.id, "avatar", filename)
     
    class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
      avatar = models.ImageField(upload_to=user_directory_path, verbose_name="头像")
    
```

用户上传文件可能是图片，也可能是pdf文件，我们如何把它们放在同一用户的不同文件夹下呢？实现这个很简单，如下图所示。

```python

    def user_directory_path(instance, filename):
      ext = filename.split('.')[-1]
      filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
      sub_folder = 'file'
      if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "avatar"
      if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
      return os.path.join(instance.user.id, sub_folder, filename)
    
```

**方法2: 在视图中自定义上传图片或文件路径**

方法1最简单直白，但有一个较大缺陷，文件上传后未经处理就直接存储了。假如用户上传了图片，我们希望先对其压缩或裁剪，然后再存储，或者我们不希望上传图片或文件到默认的路径，这时我们就有必要在视图中自定义图片或文件路径了。例子如下。

```python

    @login_required
    def ajax_avatar_upload(request):
      user = request.user
      user_profile = get_object_or_404(UserProfile, user=user)
     
      if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
          img = request.FILES['avatar_file'] # 获取上传图片
          cropped_avatar = crop_image(img, user.id)
          user_profile.avatar = cropped_avatar # 将图片路径修改到当前会员数据库
         user_profile.save()
      return HttpResponseRedirect(reverse('myaccount:profile'))
     
     
    def crop_image(file, uid):
     
      # 随机生成新的图片名，自定义路径。
      ext = file.name.split('.')[-1]
      file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
      cropped_avatar = os.path.join(uid, "avatar", file_name)
      # 相对根目录路径
      file_path = os.path.join("media", uid, "avatar", file_name)
     
      # 裁剪图片,压缩尺寸为200*200。
      img = Image.open(file)
      crop_im = img.crop((50,50,300, 300)).resize((200, 200), Image.ANTIALIAS)
      crop_im.save(file_path)
     
      return cropped_avatar
```

到此这篇关于详解Django自定义图片和文件上传路径(upload_to)的2种方式的文章就介绍到这了,更多相关Django
上传路径内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

