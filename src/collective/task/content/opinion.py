from zope.interface import implements

from plone.dexterity.content import Item

from collective.task.interfaces import BaseTask
from collective.task.interfaces import IBaseTask


class IOpinion(IBaseTask):
    """Schema for opinion"""
    pass


class Opinion(BaseTask, Item):
    """Opinion content type"""
    implements(IOpinion)

    meta_type = 'opinion'
    # disable local roles inheritance
    __ac_local_roles_block__ = True
