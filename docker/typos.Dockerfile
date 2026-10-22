FROM python:3.14-slim-bookworm@sha256:f8417a152ae83c696bee8861ed715acd93a9c9a925cd868325bc0afd788537e6
RUN pip install --no-cache-dir --disable-pip-version-check typos==1.51.1 \
  && groupadd --gid 10001 dev && useradd --uid 10001 --gid 10001 --no-create-home --shell /usr/sbin/nologin dev
USER 10001:10001
WORKDIR /work
ENTRYPOINT ["typos"]
