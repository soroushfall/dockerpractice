FROM ubuntu
ENV appDir=/app message="Welcome to our app"
WORKDIR $appDir
RUN echo $message > README.txt
CMD echo Read ${appDir}/README.txt for a friendly greeting!


# Use These Command to practice:
# docker build -t temp /
# docker run temp
# docker run temp cat /app/README.txt
# docker run -it temp /bin/sh
#   # set
#   # echo $message