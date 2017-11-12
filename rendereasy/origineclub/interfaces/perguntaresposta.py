from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IPerguntaResposta(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    nomepergunta = schema.TextLine(
        title=_(u"Nome - Pergunta"),
        required=False,
        description=_(u"Field description"),
    )
#
    creditopergunta = schema.TextLine(
        title=_(u"Credito - Pergunta"),
        required=False,
        description=_(u"Field description"),
    )
#
    videopergunta = schema.Bytes(
        title=_(u"Video - Pergunta"),
        required=False,
        description=_(u"Field description"),
    )
#
    nomeresposta = schema.TextLine(
        title=_(u"Nome - Resposta"),
        required=True,
        description=_(u"Field description"),
    )
#
    creditoresposta = schema.TextLine(
        title=_(u"Credito - Resposta"),
        required=True,
        description=_(u"Field description"),
    )
#
    videoresposta = schema.Bytes(
        title=_(u"Video - Resposta"),
        required=True,
        description=_(u"Field description"),
    )
#
