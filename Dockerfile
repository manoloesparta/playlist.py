FROM python:3.7.1-slim

COPY ["./requirements.txt", "/usr/src/"]
WORKDIR /usr/src/
RUN pip install --no-cache-dir -r requirements.txt

COPY [".", "."]

ENV USERNAME=$user
ENV CLIENT_ID=$cid
ENV CLIENT_SECRET=$csecret
ENV PLAYLIST_SRC=$psrc
ENV PLAYLIST_GOAL=$pgoal

CMD ["python", "main.py"]