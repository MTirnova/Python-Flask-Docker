FROM python:alpine
COPY . /app
WORKDIR /app
ENV KULLANICIADI="MUSTAFA"
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py