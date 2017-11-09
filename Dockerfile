FROM 192.168.3.28:8000/sirc/base-api-pymongo2

# Make directory which will be mounted to store configs & logs
RUN mkdir -p /opt/sirc/app/agentstats-api

# supervisor config
COPY docker-config/supervisord.conf /etc/supervisor/supervisord.conf
COPY docker-config/app.conf /etc/supervisor/conf.d/agentstats-api.conf

# Copy source code to container
COPY . /opt/sirc/app/agentstats-api

# Run supervisord as service on this container
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
