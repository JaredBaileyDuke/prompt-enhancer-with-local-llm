FROM python:3.9.9-slim

# copy the app files to the container
COPY . /app/

# set the working directory in the container
WORKDIR /app

# install required packages from requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# expose the port the app runs on
# EXPOSE 5000

# run the app
CMD ["streamlit", "run", "app.py"]

# # make a dockerfile that will run the streamlit app using python

# # Use the official lightweight Python image.
# # https://hub.docker.com/_/python
# FROM python:3.9-slim

# # Set the working directory.
# WORKDIR /app

# # Copy the file from your host to your current location.
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your app's code.
# COPY . .

# # Run the specified command within the container.
# CMD [ "streamlit", "run", "app.py" ]