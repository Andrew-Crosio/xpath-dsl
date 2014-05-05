class XPathBase(object):
    def __init__(self, parent=None):
        self._parent = parent

    def __repr__(self):
        return '<{class_name}: {info}>'.format(
            class_name=self.__class__.__name__,
            info=str(self)
        )

    def __unicode__(self):
        return unicode(self.render())

    def __str__(self):
        return self.render()

    def render_object(self, child=None):
        raise NotImplementedError()

    def render(self, child=None):
        if self._parent:
            return self._parent.render(child=self) + self.render_object(child=child)
        else:
            return self.render_object(child=child)

    def __or__(self, other):
        # TODO: fix this
        from xpath_dsl.conditional import Or
        return Or(self, other)
