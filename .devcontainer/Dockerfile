FROM mcr.microsoft.com/devcontainers/anaconda:1-3
FROM mcr.microsoft.com/dotnet/sdk:9.0

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Create an environment if it does not exist
# ENV CONDA_ENV_NAME my_env_name

# RUN conda create -n $CONDA_ENV_NAME python=3.12 \
#    && conda activate $CONDA_ENV_NAME \
#    && conda install --yes --ignore-pip-version pip setuptools wheel \
#    && conda clean --all --nohup --recursive

# Set the environment variable for Conda
# ENV PATH /opt/conda/bin:$PATH

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
