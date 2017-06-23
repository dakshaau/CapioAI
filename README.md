# CapioAI Python Challenge

**By:** Daksh Gupta

**Language:** Python 3.5

**Packages Required:** python-docx, requests, bottle

**Sections:**

- [Testing](https://github.com/dakshaau/CapioAI/tree/daksh#testing) 
- [Execution](https://github.com/dakshaau/CapioAI/tree/daksh#execution)
- [Docker](https://github.com/dakshaau/CapioAI/tree/daksh#docker)

### Testing:

`test.py` has **unittest** testing implemented to test the code.

To run the tests, use the following command:

```shell
python -m unittest test -v
```

### Execution:

There are two options available, either use the executable script or run the server which returns the static docx file if generated successfully.

**NOTE:** Administrator priviledges may be needed

To execute the script simply use the following command after navigating to the program directory:

```shell
python main.py <transcriptID> <APIKey>
```

To run the server simply use the following command after navigating to the program directory:

```shell
python server.py <IP> <PORT_as_integer>
```

The server accepts **GET** requests with the request header having `apiKey` label and an associated string.

The requests are only accepted at the URL: `http://IP:PORT/transcript/<transcriptID>`

## Docker:

There is a containerize version of server module available in [docker_build](docker_build/) in the form of an archive named as `CapioAI-server.tar.gz`.

To run the server from the container, execute the commands as follows:

```shell
docker load CapioAI-server.tar.gz
docker run -it -p 8080:8080 --name capio-ai capio-ai
```

The above commands will start the server within the contaainer.

For **linux** systems, requests should be sent as:

```shell
curl -X GET http://0.0.0.0:8080/transcript/<transcriptID> --header "apiKey: <APIKey>" -o <filename>.docx
```

For **Windows** systems, requests should be sent as:

```shell
curl -X GET http://<docker-machine-IP>:8080/transcript/<transcriptID> --header "apiKey: <APIKey>" -o <filename>.docx
```