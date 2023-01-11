
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
                    sh "mvn sonar:sonar \
		-Dsonar.projectKey=sonarqube \
		-Dsonar.host.url=http://192.168.160.234:9000 \
		-Dsonar.login=1089bf1c1f3fd28c831ce744752e9f0a1124a5d6 \
		-Dsonar.sources=. \
		-Dsonar.dependencyCheck.jsonReportPath=./report/dependency-check-report.json \
		-Dsonar.dependencyCheck.xmlReportPath=./report/dependency-check-report.xml \
		-Dsonar.dependencyCheck.htmlReportPath=./report/dependency-check-report.html"
         }
     }
        stage('SonarQube Quality Gate'){
      
                timeout(time: 1, unit: 'MINUTES') {
                    waitUntil {
				try {
					result = httpRequest "http://<sonarqube-instance>/api/project_analyses/search?project=<project-name>:${env.BRANCH_NAME}"
					def analyses = readJSON text: result.content
					analysisId = analyses.analyses[0].key
					
					for (event in analyses.analyses[0].events) {
						if (event.category == "VERSION") {
							eventName = event.name
							break
						}
					}
					
					echo "AnalysisId: ${analysisId}"
					echo "EventName: ${eventName}"
					echo "Looking for: ${version}"
					
					if (eventName == "${version}") {
						return true
					} else {
						return false
					}
				} catch (NullPointerException e) {
					print "No analysis yet"
					return false
				}
			} 
		}		
		
		// read gate via API
		// use analysisId to find results
		result = httpRequest "http://<sonarqube-instance>/api/qualitygates/project_status?analysisId=${analysisId}"
	
		def object = readJSON text: result.content
		def status = result.status

		// OK, WARN, ERROR, NONE
		echo "Quality Gate state: ${status}"

		if (object.projectStatus.status == "NONE") {
			error "No Quality Gate defined for ${env.BRANCH_NAME}"
		} else if (object.projectStatus.status != "OK") {
			error "Pipeline aborted due to quality gate failure: ${object.projectStatus.status}"
		} else {
			echo "Quality Gate passed (${object.projectStatus.status})"
		}
                
            }
        }

     /* stage('Push image') {
         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
             app.push("$BUILD_NUMBER")
	 app.push("latest")
         }
     } */
}
