from docutils.nodes import reference
from docutils.utils import unescape
from docutils.parsers.rst.roles import set_classes

def bl_task_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    if " " in text:
        msg = inliner.reporter.error(
            '"task" role expected a sha1; '
            '"%s" is invalid.' % text, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    app = inliner.document.settings.env.app
    node = make_link_node(rawtext, app, text, options)
    return [node], []


def make_link_node(rawtext, app, slug, options):
    try:
        base = app.config.phabricator_base
        if not base:
            raise AttributeError
    except AttributeError as err:
        raise ValueError('"phabricator_base" configuration value is not set (%s)' % str(err))
    slash = '/' if base[-1] != '/' else ''
    ref = base + slash + "T" + slug

    set_classes(options)
    node = reference(
            rawtext,
            # text to draw
            "T" + unescape(slug),
            # url to link to
            refuri=ref,
            **options)
    return node


def setup(app):
    app.add_role('task', bl_task_role)
    try:
        app.add_config_value('phabricator_base', None, 'env')
    except:
        pass
    return
