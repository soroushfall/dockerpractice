FROM ubuntu
RUN useradd sfdocker
WORKDIR /app
RUN chown sfdocker /app
USER sfdocker
RUN whoami > whoami.txt
CMD whoami


# We need additional command to give new user some permissions
# line 2 adds a new user
# line 4 changes owner of /app directory to new user
# line 5 changes the user from root to new user

# Run these commands to practice:
# docker build -t temp .
# docker run temp ls -l /
# docker run temp ls -l /app
# docker run temp cat whoami.txt