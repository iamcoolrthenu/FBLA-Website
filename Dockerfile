FROM baseImage
COPY . fbla_app
RUN make fbla_app
CMD [ python /fbla_app/build_databases ]