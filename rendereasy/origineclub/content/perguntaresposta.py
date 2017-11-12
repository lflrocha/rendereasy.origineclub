# -*- coding: utf-8 -*-
"""Definition of the PerguntaResposta content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import IPerguntaResposta
from rendereasy.origineclub.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

PerguntaRespostaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'nomepergunta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Nome - Pergunta"),
        ),
    ),


    atapi.StringField(
        'creditopergunta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Crédito - Pergunta"),
        ),
    ),


    atapi.FileField(
        'videopergunta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Vídeo - Pergunta"),
        ),
        validators=('isNonEmptyFile'),
    ),


    atapi.StringField(
        'nomeresposta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Nome - Resposta"),
        ),
        required=True,
    ),


    atapi.StringField(
        'creditoresposta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Crédito - Resposta"),
        ),
    ),


    atapi.FileField(
        'videoresposta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Vídeo - Resposta"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PerguntaRespostaSchema['title'].widget.label = _(u"Pergunta")
PerguntaRespostaSchema['title'].storage = atapi.AnnotationStorage()
PerguntaRespostaSchema['description'].storage = atapi.AnnotationStorage()
PerguntaRespostaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
PerguntaRespostaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(PerguntaRespostaSchema, moveDiscussion=False)


class PerguntaResposta(base.ATCTContent):
    """Description of the Example Type"""
    implements(IPerguntaResposta)

    meta_type = "PerguntaResposta"
    schema = PerguntaRespostaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    nomepergunta = atapi.ATFieldProperty('nomepergunta')
    creditopergunta = atapi.ATFieldProperty('creditopergunta')
    videopergunta = atapi.ATFieldProperty('videopergunta')
    nomeresposta = atapi.ATFieldProperty('nomeresposta')
    creditoresposta = atapi.ATFieldProperty('creditoresposta')
    videoresposta = atapi.ATFieldProperty('videoresposta')

    def getDados(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [{\n'
        aux = aux + 'name: "perguntaresposta",\n'
        aux = aux + 'pergunta: "%s",\n' % self.Title()
        aux = aux + 'nomepergunta: "%s",\n' % self.getNomepergunta()
        aux = aux + 'creditopergunta: "%s",\n' % self.getCreditopergunta()
        aux = aux + 'videopergunta: "%s",\n' % self.getVideopergunta()
        aux = aux + 'nomeresposta: "%s",\n' % self.getNomeresposta()
        aux = aux + 'creditoresposta: "%s",\n' % self.getCreditoresposta()
        aux = aux + 'videoresposta: "%s",\n' % self.getVideoresposta()
        aux = aux + '}]; \n'

        return aux


atapi.registerType(PerguntaResposta, PROJECTNAME)
