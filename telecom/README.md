### Launch

`cd .../telecom`

`docker build -t launch_requests_image .`

`docker run -d --name make_requests launch_requests_image`

`docker logs make_requests`