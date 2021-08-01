FROM python
RUN mkdir -p /home/api
WORKDIR /home/api
RUN pip install flask
RUN pip install pickle-mixin
RUN pip install numpy
RUN pip install sklearn
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]