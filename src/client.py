from .connect import Connect
from .file import File
from .script import Script

class Client:
  def __init__(self, apikey, secret):
    self.connection = Connect(apikey, secret)

  def file(self, uid=None):
    return File(self.connection, uid)

  def script(self, uid=None):
    return Script(self.connection, uid)