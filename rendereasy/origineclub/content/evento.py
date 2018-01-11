"""Definition of the Evento content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import IEvento
from rendereasy.origineclub.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

EventoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.IntegerField(
        'tempo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Tempo"),
            description=_(u"Informe o tempo em segundos."),
        ),
        required=True,
        default=5,
        validators=('isInt'),
    ),

    atapi.ImageField(
        'imagem',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),


    atapi.StringField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Data"),
            description=_(u"Informe a data no formato 'dd/mm/aa' ou 'dd/mm/aa a dd/mm/aa'"),
        ),
        required=True,
    ),


    atapi.StringField(
        'hora',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Hora"),
            description=_(u"Informe a hora no formato hh:mm"),
        ),
        required=True,
    ),


    atapi.StringField(
        'local',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Local"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

EventoSchema['title'].storage = atapi.AnnotationStorage()
EventoSchema['description'].storage = atapi.AnnotationStorage()
EventoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
EventoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(EventoSchema, moveDiscussion=False)


class Evento(base.ATCTContent):
    """ """
    implements(IEvento)

    meta_type = "Evento"
    schema = EventoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    tempo = atapi.ATFieldProperty('tempo')
    imagem = atapi.ATFieldProperty('imagem')
    data = atapi.ATFieldProperty('data')
    hora = atapi.ATFieldProperty('hora')
    local = atapi.ATFieldProperty('local')


    def getDados(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        filename = self.getFilename('imagem')

        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [\n'

        aux = aux + '{\n'
        aux = aux + 'name: "vinheta",\n'
        aux = aux + 'texto: ""\n'
        aux = aux + '},\n'
        aux = aux + '{\n'
        aux = aux + 'name: "evento",\n'
        aux = aux + 'tempo: %s,\n' % self.getTempo()
        aux = aux + 'titulo: "%s",\n' % self.Title()
        aux = aux + 'foto: "%s",\n' % filename
        aux = aux + 'data: %s,\n' % self.getData()
        aux = aux + 'hora: %s,\n' % self.getHora()
        aux = aux + 'local: %s,\n' % self.getLocal()
        aux = aux + '},\n'
        aux = aux + '{\n'
        aux = aux + 'name: "assinatura",\n'
        aux = aux + 'texto: "originegroup.com.br"\n'
        aux = aux + '}\n'

        aux = aux + ']; \n'
        aux = aux + 'var arquivos = [("%s/at_download/imagem/", "%s")];' % (self.absolute_url(), filename)

        return aux



atapi.registerType(Evento, PROJECTNAME)
