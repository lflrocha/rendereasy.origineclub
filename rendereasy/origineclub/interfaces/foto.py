from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IFoto(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    tempo = schema.Int(
        title=_(u"Tempo"),
        required=True,
        description=_(u"Field description"),
    )
#
    arquivo = schema.Bytes(
        title=_(u"Arquivo"),
        required=True,
        description=_(u"Field description"),
    )
#
    legenda = schema.TextLine(
        title=_(u"Legenda"),
        required=False,
        description=_(u"Field description"),
    )
#
