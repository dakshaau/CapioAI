## Containerized `main.py`

There is a `Dockerfile` present that will help you to create the docker image of the `main.py` module

**To Create:**

- Start the docker Daemon
- Navigate to this directory on the console
- Execute the following comand to build the image with the name `capio-ai`
```Batchfile
sudo docker build -t capio-ai .
```

**To Run:**

Execute the following command:

```Batchfiile
sudo docker run -i -t -e "API=<APIKey>" -e "trans=<TranscriptID>" capio-ai
```

To copy the docx file from the container to the host, execute the following command:

```Batchfile
sudo docker cp <container_id>:/<TranscriptID>.docx <path_on_host>
```