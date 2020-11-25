From python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /mypro
WORKDIR /mypro
COPY . /mypro/
RUN pip install -r requiremnts.txt


# ENV PATH="/scripts:{PATH}"

# COPY ./requiremnts.txt /requiremnts.txt

# RUN apk add --no-cache gcc libc-dev linux-headers
# # RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

# RUN pip install -r /requiremnts.txt
# RUN apk del .tmp
# RUN mkdir /mypro
# COPY ./mypro /mypro
# WORKDIR /mypro
# COPY ./scripts /scripts
# RUN chmod + /scripts/*

# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# RUN adduser -D user
# RUN chown -R user:user /vol
# RUN chmod -R 755 /vol/web
# USER user

CMD ["entrypoint.sh"]