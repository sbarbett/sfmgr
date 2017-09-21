# sfmgr

Compact client for managing scripts and data files in Neustar Web Performance Management.

## Classes

[Connect](#Connect)
[Client](#Client)
[File](#File)
[Script](#Script)

### <a name="Connect">Connect</a>

Manages a connection to the API as a state, as well as different forms of HTTP connections. Only directly accessible through the Client. *Note:* None of WPM's endpoints support PATCH.

#### Constructors

**apikey** -- API key for a WPM account
**secret** -- shared secret for a WPM account

#### Private Methods

**\_auth()** -- creates a signature using the apikey and secret
**\_is_json(rstring)** -- helper method, checks to see if a string is valid json

#### Public Methods

**get(host, uri, \*params)** -- performs an HTTP GET request
**delete(host, uri)** -- performs an HTTP DELETE request
**post(host, uri, body, \*params)** -- performs an HTTP POST request
**put(host, uri, body, \*params)** -- performs an HTTP PUT request
**post_multi_part(host, uri, file, \*params)** -- performs a multi-part POST request (specifically for uploading data files)

### <a name="Client">Client</a>

The main client which stores the API connection and provides access to the file and script management sub-modules.

#### Constructors

**apikey** -- API key for a WPM account
**secret** -- shared secret for a WPM account

#### Public Methods

**script(\*id)** -- accesses the script management interface
**file(\*id)** -- accesses the file management interface

### <a name="File">File</a>

An interface for managing data files.

#### Constructors

**connection** -- an API connection inherited from the Client
**uid** -- a file ID which is optional but required by some methods

#### Public Methods

**retrieve()** -- retrieves information for either all data files or for a specific ID
**delete()** -- deletes a specified file by ID
**create(file\_path, \*mime\_type)** -- uploads a file... if a MIME type isn't specified it will attempt to guess it

### <a name="Script">Script</a>

An interface for managing test scripts.

#### Constructors

**connection** -- an API connection inherited from the Client
**uid** -- a script ID which is optional but required by some methods

#### Public Methods

**retrieve()** -- retrieves information for either all scripts or for a specific ID
**delete()** -- deletes a specified script by ID
**create(name, body, \*\*kwargs)** -- creates a new test script... see script.py for valid keyword arguments
**replace(name, body, \*\*kwargs)** -- replaces an existing test script by ID... see script.py for valid keyword arguments