from urllib import quote
from inflection import parameterize
from werkzeug.routing import BaseConverter
from flask import url_for, redirect, request
from werkzeug.urls import Href
from soogic import __version__


class IDSlugConverter(BaseConverter):
    """Matches an int id and optional slug, separated by "/".

    :param attr: name of field to slugify, or None for default of str(instance)
    :param length: max length of slug when building url
    """

    regex = r'-?\d+(?:/[\w\-]*)?'

    def __init__(self, map, attr=None, length=80):
        self.attr = attr
        self.length = int(length)

        super(IDSlugConverter, self).__init__(map)

    def to_python(self, value):
        id, slug = (value.split('/') + [None])[:2]

        return int(id)

    def to_url(self, value):
        raw = str(value) if self.attr is None else getattr(value, self.attr, '')
        slug = parameterize(raw)[:self.length].rstrip('-')

        return '{}/{}'.format(value.id, slug).rstrip('/')


class WikiTitleConverter(BaseConverter):
    """Matches words separated by spaces or underscores.

    When parsing the url, underscores are converted to spaces.
    When building the url, spaces are converted to underscores.
    """

    def to_python(self, value):
        return value.replace('_', ' ')

    def to_url(self, value):
        return quote(value.replace(' ', '_'))


def query_update(**kwargs):
    """Update the query string with new values.

    This is useful, for example, for updating the pagination for a search query.

    :param kwargs: items to add to the query
    :return: path with updated query
    """

    q = request.args.copy()

    # can't use update since that appends values to the multi-dict instead of replacing
    for key, value in kwargs.items():
        q[key] = value

    return Href(request.path)(q)


def view_context():
    return {
        'query_update': query_update,
        '__version__': __version__
    }


def init_app(app):
    app.url_map.converters['id_slug'] = IDSlugConverter
    app.url_map.converters['wiki_title'] = WikiTitleConverter
    # app.add_template_filter(markdown)
    app.add_template_global(query_update)
    app.context_processor(view_context)
