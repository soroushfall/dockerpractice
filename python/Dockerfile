FROM ubuntu:latest

# Commands to run and install dependencies
RUN apt-get update  -y
RUN apt-get install -y python3

# When you pass commands to the container, what should interpret them
ENTRYPOINT ["python3"]

# Command to run when the container starts
CMD ["app.py"]

# Working Directory
WORKDIR /app

# Copy apps from the local folder to the docker container
COPY app.py app.py
# COPY alternate.py alternate.py

# Make Port Available
EXPOSE 8080
