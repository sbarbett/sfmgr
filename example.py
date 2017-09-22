import sfmgr, sys

if len(sys.argv) != 4:
  raise Exception('Expected use: python example.py apikey secret file_to_upload')

apikey = sys.argv[1]
secret = sys.argv[2]
file_to_upload = sys.argv[3]

c = sfmgr.Client(apikey, secret)

# Script
# Get a list of all scripts
scripts = c.script().retrieve()
# Store the id of the first script
script_id = scripts['data']['items'][0]['id']
print 'first script id: ' + script_id
# Get script info by id
script = c.script(script_id).retrieve()
# Store the name and script body
script_name = script['data']['script']['name']
print 'first script name: ' + script_name
script_body = script['data']['script']['scriptBody']
print 'first script body: ' + script_body
# Create a new test script then store the id, name and body
test_script = c.script().create('my module test', 'beginTransaction(function() { \r\n  beginStep(function() {\r\n    // testing\r\n  }) \r\n})')
test_script_id = test_script['data']['script']['id']
print 'test script id: ' + test_script_id
test_script_name = test_script['data']['script']['name']
print 'test script name: ' + test_script_name
test_script_body = test_script['data']['script']['scriptBody']
print 'test script body: ' + test_script_body
# Replace the test script with a new name
renamed_script = c.script(test_script_id).replace('this is a new name', test_script_body)
new_test_script_name = renamed_script['data']['script']['name']
print 'new test script name: ' + new_test_script_name
# Delete the test script
print c.script(test_script_id).delete()

# File
# Upload a new data file
test_file = c.file().create(file_to_upload)
test_file_id = test_file['data']['filesReceived'][0]['id']
print 'test file id: ' + test_file_id
# Delete file
print c.file(test_file_id).delete()