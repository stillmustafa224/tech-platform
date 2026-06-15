# syntax=docker/dockerfile:1

# ── Stage 1: Build ────────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

=======

ARG REACT_APP_S3_IMAGE_URL
ENV REACT_APP_S3_IMAGE_URL=${REACT_APP_S3_IMAGE_URL}


COPY package*.json ./
RUN npm ci --omit=dev

COPY . .
RUN npm run build


# ── Stage 2: Serve ────────────────────────────────────────────────
FROM nginx:stable-alpine AS runner

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
