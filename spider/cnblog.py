import requests
import kuser_agent
import ktool
import random
import json


class X():
    articles = '//div[@id="post_list"]/article'
    href = './/a[@class="post-item-title"]/@href'
    title = './/a[@class="post-item-title"]/text()'
    brief = './/p[@class="post-item-summary"]//text()'
    author = './/footer[@class="post-item-foot"]/a[1]//text()'  # strip
    publishDatetime = './/span[@class="post-meta-item"]//text()'  # strip

keywordstag1 = ['网络','程序员','IT','大数据','机器学习','数据库','分布式','线程安全','项目部署','系统','Linux',]
keywordstag2 = ['日志','Java','缓存','架构','.net','ECS','Redis','Golang']
keywordstag3 = ['Excel','神策','QuickBI','Tableau','PowerBi','统计学','Python','SPSS']
keywordstag4 = ['Django','Flask','Tornado','Bottle','Vue','Bootstrap','JQuery','CSS']


def func(pages,filename,keywordstag):
    datas = []
    for page in range(*pages):
        url = 'https://www.cnblogs.com/pick/#p{page}'.format(page=page)
        content = requests.get(
            url=url,
            headers={'User-Agent': kuser_agent.get()},
        ).content

        articles = ktool.xpath.xpath_all(content, X.articles)
        for article in articles:
            href = ktool.xpath.xpath_union(article, X.href, strip=True)
            title = ktool.xpath.xpath_union(article, X.title, strip=True)
            brief = ktool.xpath.xpath_union(article, X.brief, strip=True)
            author = ktool.xpath.xpath_union(article, X.author, default=None)
            publishDatetime = ktool.xpath.xpath_union(article, X.publishDatetime, strip=True)

            datas.append(
                dict(
                    title = title,
                    outlink = href,
                    content = '',
                    brief = brief,
                    author = author,
                    origin = 'cnblog',
                    publishDatetime = publishDatetime,
                    clickNum = random.randint(0,10000),
                    collectNum = random.randint(0,100),
                    keywords = ','.join(random.sample(keywordstag,random.randint(1,3)))
                )
            )
        print(len(datas))
    json.dump(datas,open('%s.json' % filename,'w'))


if __name__ == '__main__':
    func(pages=[30,50],filename='out2',keywordstag=keywordstag2)

