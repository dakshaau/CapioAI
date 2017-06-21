# CapioAI Python Challenge

**By:** Daksh Gupta

**Language:** Python 3.5

**Packages Required:** python-docx, requests, bottle

### Testing:

`test.py` has **unittest** testing implemented to test the code.

To run the tests, use the following command:

```Batchfile
python -m unittest test -v
```

### Execution:

There are two options available, either use the executable script or run the server which returns the static docx file if generated successfully.

**NOTE:** Administrator priviledges may be needed

To execute the script simply use the following command after navigating to the program directory:

```Batchfile
python main.py <transcriptID> <APIKey>
```

To run the server simply use the following command after navigating to the program directory:

```Batchfile
python server.py <IP> <PORT_as_integer>
```

The server accepts **GET** requests with the request header having `apiKey` label and an associated string.

The requests are only accepted at the URL: `http://IP:PORT/transcript/<transcriptID>`

## Docker:

There is a containerized version of main module availablle that sends a request to CapioAI API and creates a docx file. Go to [docker_build](docker_build/) for further instructions.