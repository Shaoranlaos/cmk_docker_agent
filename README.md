# cmk_docker_agent
A docker agent container for Check MK which allows to monitor docker containers on an alpine linux (or some thing equally minimal) docker host. 

# Requirements
This container needs access to the docker.sock.
Configure it with the volume:
/var/run/docker.sock:/var/run/docker.sock
