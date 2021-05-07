import urllib.parse as up

def get_url(url, query_dict, **kwargs):
    for key in kwargs.keys():
        query_dict[key] = kwargs[key]

    query_str = up.urlencode(query_dict)
    full_url = url + '?' + query_str
    return full_url
