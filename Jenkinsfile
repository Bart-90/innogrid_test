
node {
     stage('Clone repository') {
         checkout scm
     }
     /*stage('Build image') {
         app = docker.build("sjin1105/django", "--network host -f Dockerfile .")
     }*/
     stage('OWASP Dependency-Check Vulnerabilities ') {
        dependencyCheck additionalArguments: '''
		-s "." 
		-f "ALL"
		-o "./report/" 
		--prettyPrint
		--disableYarnAudit''', odcInstallation: 'OWASP Dependency-check'
		dependencyCheckPublisher pattern: 'report/dependency-check-report.xml'
     }
     stage('SonarQube analysis') {
	def scannerHome = tool 'sonarqube';
            withSonarQubeEnv('sonarserver'){
                    sh "${scannerHome}/bin/sonar-scanner \
		-Dsonar.projectKey=sonaruser \
		-Dsonar.host.url=http://192.168.160.244:9000 \
		-Dsonar.login=8f74a3057b93ec2c2bb9816a7e7e14d17b21c837 \
		-Dsonar.sources=. \
		-Dsonar.report.export.path=sonar-report.json \
		-Dsonar.exclusions=report/* \
		-Dsonar.dependencyCheck.jsonReportPath=./report/dependency-check-report.json \
		-Dsonar.dependencyCheck.xmlReportPath=./report/dependency-check-report.xml \
		-Dsonar.dependencyCheck.htmlReportPath=./report/dependency-check-report.html"
         }
     }
        stage('SonarQube Quality Gate'){
    	 timeout(time: 1, unit: 'HOURS') {
              def qg = waitForQualityGate(credentialsId:'8f74a3057b93ec2c2bb9816a7e7e14d17b21c837')
              if (qg.status != 'OK') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
          
          }
     }
     /* stage('Push image') {
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub id, pwd') {
             app.push("$BUILD_NUMBER")
	 app.push("latest")
         }
     }*/
}
