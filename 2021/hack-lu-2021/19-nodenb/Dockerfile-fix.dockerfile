FROM node:17-alpine

ENV NODE_ENV=production

RUN mkdir -p /app/ && chown -R node:node /app/
WORKDIR /app/

# ADD package.json yarn.lock /app/
# Copy files with proper permissions
COPY --chown=node:node package.json yarn.lock /app/
RUN yarn install

# Copy files with proper permissions
COPY --chown=node:node . /app/
# ADD . /app/

# USER 1000
USER node
ENV BIND_ADDR=0.0.0.0 PORT=3000

RUN npm config set unsafe-perm true

CMD ["node", "server.js"]
