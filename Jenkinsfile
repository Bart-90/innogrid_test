node {
  def app
  def dockerfile
  def anchorefile
  
  try {
    stage('Checkout') {
      // Clone the git repository
      checkout scm
      def path = sh returnStdout: true, script: "pwd"
      path = path.trim()
      dockerfile = path + "/Dockerfile"
      anchorefile = path + "/anchore_images"
    }
     stage('Build') {
      // Build the image and push it to a staging repository
      app = docker.build("innogrid/$JOB_NAME", "--network host -f Dockerfile .")
      docker.withRegistry("https://core.innogrid.duckdns.org", "harbor") {
	      app.push("$BUILD_NUMBER")
	      app.push("latest")
      }
      sh script: "echo Build completed"
    }
    
    stage('Grype Image Scan') {
    	grypeScan scanDest: 'https://core.innogrid.duckdns.org/innogrid/latest', repName: 'myGrypeScanResult.txt'
	currentBuild.result = "SUCCESS"
     }
    /*
    stage('OWASP Dependency-Check Vulnerabilities ') {
        dependencyCheck additionalArguments: '''
		-s "."
		-o "./report/"
		-f "ALL"
		--prettyPrint
		--disableYarnAudit''', odcInstallation: 'OWASP-Dependency-check'
		dependencyCheckPublisher pattern: 'report/dependency-check-report.xml'
     }
    
         stage('SonarQube analysis') {
	    def scannerHome = tool 'sonarqube';
            withSonarQubeEnv('sonarserver'){
                    sh "${scannerHome}/bin/sonar-scanner \
 		-Dsonar.projectKey=test \
  		-Dsonar.sources=. \
  		-Dsonar.host.url=http://192.168.160.229:9000 \
 		-Dsonar.login=7a9786bbb0cff283184d7b1034aaff8be7cc1b14 \
		-Dsonar.exclusions=report/* \
		-Dsonar.report.export.path=sonar-report.json \
		-Dsonar.dependencyCheck.jsonReportPath=./report/dependency-check-report.json \
		-Dsonar.dependencyCheck.xmlReportPath=./report/dependency-check-report.xml \
		-Dsonar.dependencyCheck.htmlReportPath=./report/dependency-check-report.html"
         }
     }
    
     stage('Grype Image Scan') {
    	docker.withRegistry('https://core.innogrid.duckdns.org', 'harbor') {
	    sh 'grype innogrid/$JOB_NAME:latest --scope AllLayers'
	}
	currentBuild.result = "SUCCESS"
     }
    
    
     stage('Anchore Image scan') {
        writeFile file: anchorefile, text: "core.innogrid.duckdns.org/innogrid/$JOB_NAME" + ":${BUILD_NUMBER}" + " " + dockerfile
        anchore name: anchorefile, \
	      engineurl: "http://192.168.160.244:8228/v1", \
	      engineCredentialsId: "anchore", \
	      annotations: [[key: 'added-by', value: 'jenkins']], \
	      forceAnalyze: true
    }
    */
  } catch (e) {
 	currentBuild.result = "FAILURE"
	echo "Exception=${e}"
	throw e
  } finally {
    stage('Pipeline End') {
      sh script: "echo Pipeline End"
    }
    if(currentBuild.result.equals("SUCCESS")){
	slackSend (channel: '#jenkins-notification', color: '#00FF00', message: "빌드 성공 : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
     }else{
	slackSend (channel: '#jenkins-notification', color: '#F01717', message: "빌드 실패 : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
     }
   }
}
 

