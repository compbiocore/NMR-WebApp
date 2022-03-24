#!/bin/bash

DIR="/script"
inotifywait -m -r -e create "$DIR" | while read f

do
    # announcement 
    echo new incoming file...processing
    # <whatever_command_or_script_you_liketorun>
    #./fid.com
done