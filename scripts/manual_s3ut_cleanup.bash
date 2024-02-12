#!/bin/bash

aws s3 --endpoint http://localhost:4566 rm --recursive s3://testbk1
aws s3 --endpoint http://localhost:4566 rb s3://testbk1
aws s3 --endpoint http://localhost:4566 ls
