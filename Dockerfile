FROM scribesecuriy.jfrog.io/scribe-docker-public-local/valint:v0.4.0 as valint
FROM alpine:3.17.0
COPY --from=valint /home/scribe/valint /usr/local/bin
RUN apk add python3 py3-pip
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD src src
WORKDIR /src/
ENTRYPOINT [ "/src/script.py" ]