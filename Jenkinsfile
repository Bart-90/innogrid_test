
node {
     stage('Clone repository') {
         checkout scm
     }
     stage('Build image') {
         app = docker.build("bart09/test", "--network host -f Dockerfile .")
     }
     stage('OWASP Dependency-Check Vulnerabilities ') {
        dependencyCheck additionalArguments: '''
		-s "." 
		-f "ALL"
		-o "report/" 
		--prettyPrint
		--disableYarnAudit''', odcInstallation: 'OWASP Dependency-check'
		dependencyCheckPublisher pattern: 'report/dependency-check-report.xml'
     }
     stage('SonarQube analysis') {
            withSonarQubeEnv('sonarserver'){
                    sh "mvn sonar:sonar -Dsonar.projectKey=sonarqube -Dsonar.host.url=http://192.168.160.234:9000 -Dsonar.login=1089bf1c1f3fd28c831ce744752e9f0a1124a5d6 -Dsonar.sources=. -Dsonar.dependencyCheck.jsonReportPath=./report/dependency-check-report.json -Dsonar.dependencyCheck.xmlReportPath=./report/dependency-check-report.xml -Dsonar.dependencyCheck.htmlReportPath=./report/dependency-check-report.html"
         }
     }
     /* stage('Push image') {
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             app.push("$BUILD_NUMBER")
	 app.push("latest")
         }
     } */
}
