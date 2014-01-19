import wtforms
import wtformsparsleyjs
from django.utils.translation import ugettext as _


class BootstrapRadioButtonWidget(wtforms.widgets.RadioInput):
    pass


class BootstrapRadioButtonsWidget(object):
    DELETE_BUTTON = '''
    <label class="btn btn-xs btn-danger active">
        <input type="radio" name="%(name)s" value="">
        <span class="glyphicon glyphicon-remove"></span>
    </label>
    '''

    def __init__(self, add_delete='before'):
        self.add_delete = add_delete

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('class', 'btn-group btn-small')
        kwargs.setdefault('data-toggle', 'buttons')
        html = ['<div %s>' % wtforms.widgets.html_params(**kwargs)]

        if self.add_delete == 'before':
            html.append(self.DELETE_BUTTON % dict(name=field.name))

        for subfield in field:
            html.append(subfield.label(
                subfield() + subfield.label.text,
                **{'class': 'btn btn-xs btn-success'}))

        if self.add_delete == 'after':
            html.append(self.DELETE_BUTTON % dict(name=field.name))

        html.append('</div>')
        return wtforms.widgets.HTMLString(''.join(html))


class BootstrapRadioButtonField(wtforms.RadioField):
    widget = BootstrapRadioButtonsWidget()
    option_widget = BootstrapRadioButtonWidget()


class TagListField(wtforms.Field):
    widget = wtforms.widgets.TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []


class DinnerForm(wtforms.Form):
    name = wtformsparsleyjs.TextField(_('Name'))
    description = wtformsparsleyjs.TextField(_('Description'))
    cooks = TagListField()

