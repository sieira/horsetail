"""
Copyright © 2016 Luis Sieira Garcia
This file is part of horsetail.
    Horsetail is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Horsetail is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with along with horsetail. If not, see <http://www.gnu.org/licenses/>.
"""
import mongoengine


class Content(mongoengine.Document):
    """This class defines an abstract content.
        URI: Is the unique identifier of the content object
    """
    meta = {'allow_inheritance', True}

    URI = mongoengine.StringFied(primary_key=True,
                                 null=False, regex=r'^[a-zA-Z0-9_-]*$', unique=True)
    # TODO reference to creator
    # TODO reference to owner
    # TODO auth


class Tag(mongoengine.Document):
    label = mongoengine.StringField(required=True, unique=True)
    description = mongoengine.StringField()
    parents = mongoengine.ListField(mongoengine.ReferenceField('Tag', mongoengine.NULLIFY))


class Page(Content):
    """Pages are a particular kind of content, which have a body and a title.
    Pages can only be in a limited range of formats.
    Currently, only markdown and html are allowed.
    """
    # TODO Check that the body actually is in the given format
    title = mongoengine.StringField(unique=True)
    page_format = mongoengine.StringField(required=True,
                                          regex=r'^(md|html)$',
                                          default='html')
    body = mongoengine.StringField(required=True)


class Article(Page):
    """Articles are Pages containing a summary and a list of tags
    """
    summary = mongoengine.StringField()
    tags = mongoengine.ListField(mongoengine.ReferenceField(Tag))


class ContentSet(Content):
    """Contentsets are groups or content intended to be displayed by views
    """
    pass


class View(Page):
    """Views are pages that display other contents
    """
    pass


class Widget(View):
    """Widgets are independant views that do not depend on a display port
    """
    pass
