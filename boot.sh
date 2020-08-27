#!/bin/bash

flask db upgrade
if [ "$1" == "run" ]; then
  exec gunicorn --reload -b :5000 --access-logfile - --error-logfile - 'kailio:create_app()'
else
  flask $@
fi
