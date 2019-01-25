FROM python:3.7.1-slim

COPY ["./requirements.txt", "/usr/src/"]
WORKDIR /usr/src/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install vim -y

COPY [".", "."]

# User info
ARG user
ENV USERNAME=${user}
ARG id
ENV CLIENT_ID=${id}
ARG secret
ENV CLIENT_SECRET=${secret}

# Playlist stuff
ARG src
ENV PLAYLIST_SRC=${src}
ARG goal
ENV PLAYLIST_GOAL=${goal}
ARG uri
ENV REDIRECT_URI=${uri}

CMD ["python", "main.py"]