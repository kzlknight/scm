#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    """
    from appSite.models import Nav

    for i in range(1,6):
        Nav(
            name='name' + str(i),
            position=i,
            url = 'https://www.baidu.com/?a=' + str(i),
            level = 1,
        ).save()

    for i in range(6,8):
        nav = Nav(
            name='name' + str(i),
            position=i,
            url = 'https://www.baidu.com/?a=' + str(i),
            level = 2,
        )
        nav.save()
        nav.subNavs.add(
            Nav.objects.get(id=5)
        )
        nav.save()
    """

    """
    
    from appArticle.models import Article,Category

    c1 = Category.objects.all()[0]
    c2 = Category.objects.all()[1]

    for i in range(100):
        Article(title=str(i),category=c1).save()
    for i in range(100,200):
        Article(title=str(i),category=c2).save()
    """

    from appExpert.models import Category,Expert
    # c1 = Category(name='c1')
    # c1.save()
    # c2 = Category(name='c2')
    # c2.save()

    # for i in range(100):
    #     e = Expert(name=str(i))
    #     e.save()
    #     e.categorys.add(c1)
    #     e.save()
    # for i in range(101,200):
    #     e = Expert(name=str(i))
    #     e.save()
    #     e.categorys.add(c2)
    #     e.save()
    c1 = Category.objects.filter(name='c1').first()
    c2 = Category.objects.filter(name='c2').first()

    for i in range(100):
        e = Expert.objects.get(id=i)
        e.category = c1
        e.save()

    for i in range(101,200):
        e = Expert.objects.get(id=i)
        e.category = c2
        e.save()




