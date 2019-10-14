# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class WhitelistItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id=None, gate=None, trigger_id=None):  # noqa: E501
        """WhitelistItem - a model defined in Swagger

        :param id: The id of this WhitelistItem.  # noqa: E501
        :type id: str
        :param gate: The gate of this WhitelistItem.  # noqa: E501
        :type gate: str
        :param trigger_id: The trigger_id of this WhitelistItem.  # noqa: E501
        :type trigger_id: str
        """
        self.swagger_types = {
            'id': str,
            'gate': str,
            'trigger_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'gate': 'gate',
            'trigger_id': 'trigger_id'
        }

        self._id = id
        self._gate = gate
        self._trigger_id = trigger_id

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WhitelistItem of this WhitelistItem.  # noqa: E501
        :rtype: WhitelistItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this WhitelistItem.


        :return: The id of this WhitelistItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhitelistItem.


        :param id: The id of this WhitelistItem.
        :type id: str
        """

        self._id = id

    @property
    def gate(self):
        """Gets the gate of this WhitelistItem.


        :return: The gate of this WhitelistItem.
        :rtype: str
        """
        return self._gate

    @gate.setter
    def gate(self, gate):
        """Sets the gate of this WhitelistItem.


        :param gate: The gate of this WhitelistItem.
        :type gate: str
        """
        if gate is None:
            raise ValueError("Invalid value for `gate`, must not be `None`")  # noqa: E501

        self._gate = gate

    @property
    def trigger_id(self):
        """Gets the trigger_id of this WhitelistItem.


        :return: The trigger_id of this WhitelistItem.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this WhitelistItem.


        :param trigger_id: The trigger_id of this WhitelistItem.
        :type trigger_id: str
        """
        if trigger_id is None:
            raise ValueError("Invalid value for `trigger_id`, must not be `None`")  # noqa: E501

        self._trigger_id = trigger_id
