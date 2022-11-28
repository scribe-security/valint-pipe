FROM scribesecuriy.jfrog.io/scribe-docker-public-local/valint:latest as valint
FROM alpine:latest
COPY --from=valint /home/scribe/valint /usr/local/bin
RUN apk add python3 py3-pip
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD src src
WORKDIR /src/
ENTRYPOINT [ "./script.py" ]