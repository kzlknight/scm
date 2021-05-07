class ArticleListView(View):

    def build(self, request, Article, Category):
        # user
        user = User.objects.first()
        request.session['user'] = dict(id=user.id, name=user.name, password=user.password, tel=user.tel)
        user = request.session.get('user', None)

        # content
        #  filter
        category_id = self.request.GET.get('category_id', None)
        keyword = self.request.GET.get('keyword', None)
        year = self.request.GET.get('year', None)
        # order_bys = self.request.GET.getlist('order_bys')
        order_by = self.request.GET.get('order_by', None)
        if order_by:
            order_bys = (order_by,)
        else:
            order_bys = tuple()

        query_dict = {}
        if category_id:
            query_dict['category_id'] = category_id
        if keyword:
            query_dict['keyword'] = keyword
        if year:
            query_dict['year'] = year
        if order_by:
            query_dict['order_by'] = order_by

        current_page = self.request.GET.get('page', 1)
        filter_dict = {}

        if category_id:
            filter_dict['category_id'] = category_id
        if keyword:
            filter_dict['keywords__contains'] = keyword
        if year:
            filter_dict['createDatetime__year'] = year
        try:
            articles = Article.objects.filter(**filter_dict).order_by(*order_bys).order_by('position')
            paginator = Paginator(articles, 10)
            page = paginator.page(current_page)
        except:
            print(traceback.format_exc())
            return HttpResponse('not ok')

        # headers
        headers = Nav.objects.all()

        # nav-left

        # nav-top

        # page
        context = {'headers': headers, 'user': user, 'articles': articles, 'page': page}
        # url = request.get_full_path()
        url = request.path
        print(paginator.num_pages)
        this_url = get_url(url, query_dict, page=1, keyword='python')
        print(this_url)

        return (request, 'articleList.html', context)