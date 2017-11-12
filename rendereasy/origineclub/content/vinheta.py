# -*- coding: utf-8 -*-
"""Definition of the Vinheta content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import IVinheta
from rendereasy.origineclub.config import PROJECTNAME

VinhetaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.FileField(
        'video',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Vídeo"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

VinhetaSchema['title'].storage = atapi.AnnotationStorage()
VinhetaSchema['description'].storage = atapi.AnnotationStorage()
VinhetaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
VinhetaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(VinhetaSchema, moveDiscussion=False)


class Vinheta(base.ATCTContent):
    """Description of the Example Type"""
    implements(IVinheta)

    meta_type = "Vinheta"
    schema = VinhetaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    video = atapi.ATFieldProperty('video')

    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [{\n'
        aux = aux + 'name: "vinheta",\n'
        aux = aux + 'texto: "%s",\n' % self.Title()
        aux = aux + 'video: "%s",\n' % self.getVideo()
        aux = aux + '}]; \n'

        return aux

atapi.registerType(Vinheta, PROJECTNAME)
