import requests, json
from time import time
from hashlib import md5

class Connect:
  def __init__(self, apikey, secret):
    self.proto = 'https://'
    self.domain = '.wpm.neustar.biz/api/1.0'
    self.apikey = apikey
    self.secret = secret

  def _auth(self):
    sig = self.apikey + self.secret + str(int(time()))
    return md5(sig.encode()).hexdigest()

  def _is_json(self, rstring):
    try:
      j = json.loads(rstring)
    except ValueError as e:
      return False
    return True

  def _build_headers(self, content_type):
      result = {'Accept': 'application/json'}
      if content_type != '':
          result['Content-Type'] = content_type
      return result

  def get(self, host, uri, params=None):
    url = self.proto + host + self.domain + uri
    return self._do_call(url, 'GET', params=params)

  def delete(self, host, uri):
    url = self.proto + host + self.domain + uri
    return self._do_call(url, 'DELETE')

  def post(self, host, uri, body, params=None):
    url = self.proto + host + self.domain + uri
    return self._do_call(url, 'POST', params=params, body=body)

  def put(self, host, uri, body, params=None):
    url = self.proto + host + self.domain + uri
    return self._do_call(url, 'PUT', params=params, body=body)

  def post_multi_part(self, host, uri, file, params=None):
    url = self.proto + host + self.domain + uri
    return self._do_call(url, 'POST', params=params, files=file, content_type='')

  def _do_call(self, url, method, params=None, body=None, files=None, content_type='application/json'):
    h1 = self._build_headers(content_type)
    if params == None:
      params = {'sig': self._auth(), 'apikey': self.apikey}
    else:
      params.update({'sig': self._auth(), 'apikey': self.apikey})
    r = requests.request(method, url, params=params, data=body, headers=h1, files=files)
    if r.status_code == requests.codes.NO_CONTENT:
      return '{}'
    if self._is_json(r.text):
      return r.json()
    else:
      return r.text