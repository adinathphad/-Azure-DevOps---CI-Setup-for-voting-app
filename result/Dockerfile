# Use official Node.js base image
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (better layer caching)
COPY package.json .

# Install project dependencies
RUN npm install

# Copy application source code
COPY server.js .

# Start the Node.js server
CMD ["node", "server.js"]
