FROM amazoncorretto:11
ENV SPRING_PROFILES_ACTIVE docker,mysql
COPY ./target/*.jar /app.jar
EXPOSE 8081
ENTRYPOINT ["java", "-jar", "./app.jar"]