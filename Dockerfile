# Imagen base de Node.js
FROM node:14

# Directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar las dependencias
RUN npm install

# Construir el proyecto
RUN make

# Exponer el puerto 8000
EXPOSE 8000

# Ejecutar el servidor web
CMD ["npm", "start"]
