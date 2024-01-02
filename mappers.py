__full_format = '<a href="{link}"><b>{title}</b></a>\n\n{description}'
__no_link_no_description_format = '<b>{title}</b>'
__no_link_format = '<b>{title}</b>\n\n{description}'
__no_description_format = '<a href="{link}"><b>{title}</b></a>'


def to_pretty_text_message(self: dict) -> str:
    if self['link'] is None and self['description'] is None:
        return __no_link_no_description_format.format(
            title=self['title']
        )
    elif self['link'] is None:
        return __no_link_format.format(
            title=self['title'],
            description=self['description'],
        )
    elif self['description'] is None:
        return __no_description_format.format(
            title=self['title'],
            link=self['link'],
        )
    else:
        return __full_format.format(
            link=self['link'],
            title=self['title'],
            description=self['description'],
        )
