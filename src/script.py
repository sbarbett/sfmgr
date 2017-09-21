import json

""" Script Interface

Retrieve, delete, replace and create scripts in script.wpm.neustar.biz.
PATCH is not supported by this endpoint.

"""

class Script:
    def __init__(self, connection, uid=None):
      self.connection = connection
      self.uid = uid
      self.host = 'script'
      self.uri = '/script'

    def retrieve(self):
      """ Get info on a specific script or a list of scripts, dependent on
      whether a uid property is present.

      """
      if self.uid == None:
        return self.connection.get(self.host, self.uri)
      return self.connection.get(self.host, self.uri + '/' + self.uid)

    def delete(self):
      """ Delete an existing script. A valid uid constructor must have been
      supplied to the Script interface.

      """
      if self.uid == None:
        raise Exception('A unique id is needed for this method')
      return self.connection.delete(self.host, self.uri + '/' + self.uid)

    def create(self, name, body, **kwargs):
      """ Create a new script.

      Args:
      name -- A unique name. It can't be the name of an already-existing
              script.
      body -- The script body.

      Kwargs:
      description -- An optional description of the script.
      tabs -- Tab keywords. This can be a string or a list.
      validation_bypassed -- A boolean value for whether or not to bypass
                             validation.

      """
      payload = {'name': name, 'scriptBody': body}
      if kwargs:
        if 'description' in kwargs:
          payload.update({'description': kwargs['description']})
        if 'tabs' in kwargs:
          if type(kwargs['tabs']) is not list:
            kwargs['tabs'] = [kwargs['tabs']]
          payload.update({'tabs': kwargs['tabs']})
        if 'validation_bypassed' in kwargs:
          payload.update({'validationBypassed': kwargs['validation_bypassed']})
      return self.connection.post(self.host, self.uri, json.dumps(payload))

    def replace(self, name, body, **kwargs):
      """ Update an existing script.

      Args:
      name -- A script name. You can use the same name or rename it.
      body -- The script body.

      Kwargs:
      description -- An optional description of the script.
      tabs -- Tab keywords. This can be a string or a list.
      validation_bypassed -- A boolean value for whether or not to bypass
                             validation.
      update_monitors -- A boolean value for whether or not to auto-
                         update monitors associated with the script.

      """
      if self.uid == None:
        raise Exception('A unique id is needed for this method')
      payload = {'id': self.uid, 'name': name, 'scriptBody': body}
      if kwargs:
        if 'description' in kwargs:
          payload.update({'description': kwargs['description']})
        if 'tabs' in kwargs:
          if type(kwargs['tabs']) is not list:
            kwargs['tabs'] = [kwargs['tabs']]
          payload.update({'tabs': kwargs['tabs']})
        if 'validation_bypassed' in kwargs:
          payload.update({'validationBypassed': kwargs['validation_bypassed']})
        if 'update_monitors' in kwargs:
          payload.update({'updateMonitors': kwargs['update_monitors']})
      return self.connection.put(self.host, self.uri + '/' + self.uid, json.dumps(payload))