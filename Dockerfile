FROM python:3.7.1-slim

COPY ["./requirements.txt", "/usr/src/"]
WORKDIR /usr/src/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install vim -y

COPY [".", "."]

ARG user
ENV USERNAME=${user}
ARG c_id
ENV CLIENT_ID=${c_id}
ARG c_secret
ENV CLIENT_SECRET=${c_secret}
ARG p_src
ENV PLAYLIST_SRC=${p_src}
ARG p_goal
ENV PLAYLIST_GOAL=${p_goal}

CMD ["python", "main.py"]