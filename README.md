# CapioAI Python Challenge

**By:** Daksh Gupta

**Language:** Python 3.5

**Packages Required:** python-docx, requests, bottle

## Updates:

For updates after June 13, please check [this branch](https://github.com/dakshaau/CapioAI/tree/daksh)

I have implemented Unit testing using `unittest` module of python and containerized the server. There is also a sample curl request to demonstrate how to retrieve the .docx file using the server I created.

### Testing:

The code has assertions written into it. I haven't used any additional testing module to implement testcases

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