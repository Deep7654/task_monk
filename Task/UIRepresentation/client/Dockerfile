FROM node:20-alpine as build

WORKDIR /app

# Copy only package files first
COPY package.json ./

# Clean install (IMPORTANT FIX)
RUN npm install

# Copy rest of files
COPY . .

# Force rebuild native deps
RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "dev" , "--", "--host"]