FROM scribesecuriy.jfrog.io/scribe-docker-public-local/gensbom:latest as builder1
FROM scribesecuriy.jfrog.io/scribe-docker-public-local/valint:latest as builder2
FROM alpine:latest
COPY --from=builder1 /home/scribe/gensbom /usr/local/bin
COPY --from=builder2 /home/scribe/valint /usr/local/bin
RUN apk add python3 py3-pip
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD src src
WORKDIR /src/
ENTRYPOINT [ "./script.py" ]