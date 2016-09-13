#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. 
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line
echo "X-COMP-490: Welcome Harout"
echo "Content-type: text/html"
echo ""

declare -A array

parseQuery(){
		#Parse QUERY_STRING
	saveIFS=$IFS
	IFS='=&'
	param=($QUERY_STRING)
	IFS=$saveIFS

	for ((i=0; i<${#param[@]}; i+=2))
	do
		array[${param[i]}]=${param[i+1]}
	done
}


if [ -n "${QUERY_STRING}" ] ; then
   parseQuery
   http="http://"
   #DOES NOT WORK WELL WITH HTTPS WEBSITE LIKE THIS
   page="$(/usr/bin/curl "$http${array[website]}")"
   echo "$page"
else
echo "No query provided!"
fi

exit 0