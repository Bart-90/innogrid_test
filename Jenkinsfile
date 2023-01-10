
node {
     stage('Clone repository') {
         checkout scm
     }
     stage('Build image') {
         app = docker.build("bart09/test")
     }
     stage('Dependency Check Report') {
        dependencyCheck additionalArguments: '-o "/home/vagrant/report" -s "./" -f "HTML, XML, JSON" --prettyPrint', odcInstallation: 'OWASP Dependency-check'
     }
     stage('SonarQube analysis') {
            withSonarQubeEnv('SonarQube-Server'){
                    sh "mvn sonar:sonar -Dsonar.projectKey=cccr-innogrid -Dsonar.host.url=http://192.168.56.101:9000 -Dsonar.login=sqp_89d07124730b6ee47afaaa9937ba9b3a865d0136 -Dsonar.sources=."
         }
     }
     /* stage('Push image') {
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             app.push("$BUILD_NUMBER")
	     app.push("latest")
         }
     } */
}
