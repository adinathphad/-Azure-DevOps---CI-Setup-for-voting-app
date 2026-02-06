# Use official Node.js 18 lightweight image
FROM node:18-slim

# Install curl for health checks
# Install tini to properly handle process signals (start/stop)
# Clean apt cache to keep image small
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl tini && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /usr/local/app

# Install nodemon globally
# Nodemon restarts the app when files change (useful in development)
RUN npm install -g nodemon

# Copy package.json and package-lock.json
# This helps Docker cache dependencies
COPY package*.json ./

# Install exact dependencies from package-lock.json
# npm ci is faster and more stable than npm install
# Clean npm cache and move node_modules to avoid overwrite
RUN npm ci && \
    npm cache clean --force && \
    mv /usr/local/app/node_modules /node_modules

# Copy application source code
COPY . .

# Set application port
ENV PORT=80

# Inform Docker that the app listens on port 80
EXPOSE 80

# Use tini as entrypoint to handle signals correctly
ENTRYPOINT ["/usr/bin/tini", "--"]

# Start the Node.js server
CMD ["node", "server.js"]
