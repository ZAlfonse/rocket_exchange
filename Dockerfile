FROM django:1.10.1-python3

# Create workspace
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Move python requirements into workspace and install
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Move code into workspace
COPY . /usr/src/app


# Expose dev environment and 
EXPOSE 8000

#Set entrypoint to management command and cmd to dev server
ENTRYPOINT ["python", "manage.py"] 
CMD ["runserver", "0.0.0.0:8000"]
