from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IVinheta(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    video = schema.Bytes(
        title=_(u"Video"),
        required=True,
        description=_(u"Field description"),
    )
#
