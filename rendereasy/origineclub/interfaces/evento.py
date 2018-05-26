from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IEvento(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    tempo = schema.Int(
        title=_(u"Tempo"),
        required=True,
        description=_(u"Informe o tempo em segundos."),
    )
#
    imagem = schema.Bytes(
        title=_(u"Foto"),
        required=True,
        description=_(u"Field description"),
    )
#
    data = schema.TextLine(
        title=_(u"Data"),
        required=True,
        description=_(u"Informe a data"),
    )
#
    hora = schema.TextLine(
        title=_(u"Hora"),
        required=True,
        description=_(u"Field description"),
    )
#
    local = schema.TextLine(
        title=_(u"Local"),
        required=True,
        description=_(u"Nome do Local - Cidade/UF"),
    )
#
