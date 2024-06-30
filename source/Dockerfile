FROM python:3.9.19-alpine

# copy the app files to the container
COPY . /app/

# set the working directory in the container
WORKDIR /app

# install required packages from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# expose the port the app runs on
EXPOSE 5000

# run the app
CMD ["python", "app.py"]