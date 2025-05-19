### Launch

`cd .../radio_frequency_system`
`docker build -t launch_scripts_image .`
`docker run -it --rm launch_scripts_image /bin/bash`
`cd /tmp`
`./search_path.sh config.txt "name"`
`python3 extract_path_value.py config.txt "file"`