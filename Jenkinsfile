
node {
     stage('Clone repository') {
         checkout scm
     }
     /* stage('Build image') {
         app = docker.build("bart09/test")
     }*/
     stage('OWASP Dependency-Check Vulnerabilities ') {
        dependencyCheck additionalArguments: '''
		-s "." 
		-f "ALL"
		-o "./report/" 
		--prettyPrint''', odcInstallation: 'OWASP Dependency-check'
		dependencyCheckPublisher pattern: 'dependency-check-report.xml'
     }
     stage('SonarQube analysis') {
            withSonarQubeEnv('SonarQube-Server'){
                    sh "mvn sonar:sonar -Dsonar.projectKey=sonarqube -Dsonar.host.url=http://192.168.160.234.:9000 -Dsonar.login=1089bf1c1f3fd28c831ce744752e9f0a1124a5d6 -Dsonar.sources=. -Dsonar.dependencyCheck.jsonReportPath=./dependency-check-report.json -Dsonar.dependencyCheck.xmlReportPath=./dependency-check-report.xml -Dsonar.dependencyCheck.htmlReportPath=./dependency-check-report.html"
         }
     }
     /* stage('Push image') {
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             app.push("$BUILD_NUMBER")
	     app.push("latest")
         }
     } */
}
