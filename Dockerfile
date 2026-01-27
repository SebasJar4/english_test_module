FROM  node:alpine3.23 as base
RUN apk add pnpm

FROM base as frontend_service
WORKDIR /usr/local/frontend/

FROM base as backend_service
WORKDIR /usr/local/backend/
