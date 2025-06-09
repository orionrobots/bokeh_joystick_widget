# Build with docker build . -f test.Dockerfile -t bokeh_joystick_widget:test-${python_version}
ARG python_version=3.10
FROM python:${python_version}-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

    # libnss3 \
    # libnspr4 \
    # libasound2t64 \

    # build-essential \
    # git \

# Install Poetry
COPY test_requirements.txt /tmp/test_requirements.txt
RUN pip install -r /tmp/test_requirements.txt

# Set the working directory
WORKDIR /app
# Copy poetry configuration files
COPY pyproject.toml poetry.lock /app/

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --with test --with dev

# Install Playwright
RUN poetry run playwright install

# Copy the application code
COPY . /app

# Make the CMD the test run
CMD ["poetry", "run", "pytest", "src/tests"]
