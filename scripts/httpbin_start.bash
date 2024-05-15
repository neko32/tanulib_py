#!/bin/bash

docker run -it --name httpbin_srv --rm -d -p 80:80 kennethreitz/httpbin

