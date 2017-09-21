from mimetypes import MimeTypes
from ntpath import basename

""" File Interface 

Retrieve and delete or create new data files in script.wpm.neustar.biz.
PATCH and PUT are not supported by this endpoint.

"""

class File:
  def __init__(self, connection, uid=None):
    self.connection = connection
    self.uid = uid
    self.host = 'script'
    self.uri = '/file'

  def retrieve(self):
    """ Get info on a specific data file or a list of data files, dependent
    on whether a uid property is present.

    """
    if self.uid == None:
      return self.connection.get(self.host, self.uri)
    return self.connection.get(self.host, self.uri + '/' + self.uid)

  def delete(self):
    """ Delete an existing data file. A valid uid constructor must have been
    supplied to the File interface.

    """
    if self.uid == None:
      raise Exception('A unique id is needed for this method')
    return self.connection.delete(self.host, self.uri + '/' + self.uid)

  def create(self, file_path, mime_type=None):
    """ Upload a new data file.

    Args:
    file_path -- Path to the file on the system making the request.

    Kwargs:
    mime_type -- The MIME type of the file. If not specified, it will attempt
                 to use the mimetypes library to guess. 

    """
    if mime_type == None:
      mime = MimeTypes()
      mime_type = mime.guess_type(file_path)[0]
    file_name = basename(file_path)
    file = {'file': (file_name, open(file_path, 'rb'), mime_type)}
    params = {'qqfile': file_name}
    return self.connection.post_multi_part(self.host, self.uri, file, params=params)