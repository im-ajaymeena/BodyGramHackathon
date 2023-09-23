FROM node as build

WORKDIR /app
COPY . .
RUN npm ci

FROM build as development
EXPOSE 5173
CMD ["npm", "run", "dev"]

# FROM nginx as production

# COPY --from=build /app/dist /app
# COPY nginx.conf /etc/nginx/nginx.conf
# EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]
