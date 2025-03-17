FROM amazoncorretto:11
ENV SPRING_PROFILES_ACTIVE docker,mysql
COPY ./target/*.jar /app.jar
EXPOSE 8083
ENTRYPOINT ["java", "-jar", "./app.jar"]