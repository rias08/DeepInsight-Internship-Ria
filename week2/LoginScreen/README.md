# Local Servers, HTTP, and URL's
## How to run python http server locally
### file:// --> local file
### http:// --> remote file
### Method 1
#### Use Python in CMD: py -V --> cd Desktop --> python -m http.server --> search [localhost]:8000 for the local server
### Method 2
#### using liveserver in vscode --> http://localhost:[port number]/[folder name]/[file name]/
## HTTP, Request + Response headers, and Body
###
## URL + Parameters
### URL -> Uniform Resource Locator -> The address of a web page
### Parameters are used to specify the address of the web application needed 
#### Example: http://example.com?product=1234&utm_source=google : looking for product 1234 from google, on example.com
## Extracting path + query parameters from the URL or http request
### What is in the URL itself is a path parameter --> tells the server where to go --> identified with {}
### What comes after the '?' are the query parameters --> additional information attached to a URL
## How to send a HTTP response
## Sources
### https://www.semrush.com/blog/url-parameters/
### https://apidog.com/blog/path-param-vs-query-param/
### https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/set_up_a_local_testing_server