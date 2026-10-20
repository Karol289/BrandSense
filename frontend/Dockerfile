FROM node:20-alpine

WORKDIR /app

# Copy package definitions first for dependency caching
COPY package*.json ./

RUN npm install

# Copy application source files
COPY . .

# Expose Vite's default dev server port
EXPOSE 3000

# Start Vite dev server bound to 0.0.0.0 so Docker forwards host traffic
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]