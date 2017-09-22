# sfmgr

Compact client for managing scripts and data files in Neustar Web Performance Management.

## Install

Run setup.py from a terminal or command line.

```
python setup.py install
```

## Usage

Import the 'sfmgr' library into your Python script and define a connection object using your WPM apikey and secret.

```python
import sfmgr
c = sfmgr.Client('apikey', 'secret')
```

For additional info see example.py.

## Classes

[Connect](#Connect)<br />
[Client](#Client)<br />
[File](#File)<br />
[Script](#Script)

### <a name="Connect">Connect</a>

Manages a connection to the API as a state, as well as different forms of HTTP connections. Only directly accessible through the Client. *Note:* None of WPM's endpoints support PATCH.

#### Constructors

*apikey* -- API key for a WPM account<br />
*secret* -- shared secret for a WPM account

#### Private Methods

*\_auth()* -- creates a signature using the apikey and secret<br />
*\_is\_json(rstring)* -- helper method, checks to see if a string is valid json<br />
*\_build\_headers* -- helper method, construct headers for request<br />
*\_do\_call* -- perform HTTP requests

#### Public Methods

*get(host, uri, \*params)* -- performs an HTTP GET request<br />
*delete(host, uri)* -- performs an HTTP DELETE request<br />
*post(host, uri, body, \*params)* -- performs an HTTP POST request<br />
*put(host, uri, body, \*params)* -- performs an HTTP PUT request<br />
*post_multi_part(host, uri, file, \*params)* -- performs a multi-part POST request (specifically for uploading data files)

### <a name="Client">Client</a>

The main client which stores the API connection and provides access to the file and script management sub-modules.

#### Constructors

*apikey* -- API key for a WPM account<br />
*secret* -- shared secret for a WPM account

#### Public Methods

*script(\*id)* -- accesses the script management interface<br />
*file(\*id)* -- accesses the file management interface

### <a name="File">File</a>

An interface for managing data files.

#### Constructors

*connection* -- an API connection inherited from the Client<br />
*uid* -- a file ID which is optional but required by some methods

#### Public Methods

*retrieve()* -- retrieves information for either all data files or for a specific ID<br />
*delete()* -- deletes a specified file by ID<br />
*create(file\_path, \*mime\_type)* -- uploads a file... if a MIME type isn't specified it will attempt to guess it

### <a name="Script">Script</a>

An interface for managing test scripts.

#### Constructors

*connection* -- an API connection inherited from the Client<br />
*uid* -- a script ID which is optional but required by some methods

#### Public Methods

*retrieve()* -- retrieves information for either all scripts or for a specific ID<br />
*delete()* -- deletes a specified script by ID<br />
*create(name, body, \*\*kwargs)* -- creates a new test script... see script.py for valid keyword arguments<br />
*replace(name, body, \*\*kwargs)* -- replaces an existing test script by ID... see script.py for valid keyword arguments