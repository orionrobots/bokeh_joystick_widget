# Build with:
# PYTHON_VERSION=3.11
# docker build . -f test.Dockerfile \
#   --arg python_version=${PYTHON_VERSION} \
#   -t bokeh_joystick_widget:test-${PYTHON_VERSION}
# docker run --init --rm -it -v "${PWD}:/app" bokeh_joystick_widget:test-${PYTHON_VERSION}
ARG python_version=3.11
FROM python:${python_version}-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    poetry config virtualenvs.create false

# Build the setup
WORKDIR /setup
COPY src/tests/poetry.lock src/tests/pyproject.toml /setup/
# Install  test project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install
# Install Playwright
RUN poetry run playwright install --with-deps

# Now build the app
WORKDIR /app

# Copy poetry configuration files
COPY pyproject.toml poetry.lock /app/

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --with test --with dev

# Copy the application code
COPY . /app

RUN poetry install

# Clean up pip cache (optional, but helps)
RUN rm -rf /root/.cache/pip

# Make the CMD the test run
CMD ["poetry", "run", "pytest", "src/tests"]
