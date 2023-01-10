
node {
     stage('Clone repository') {
         checkout scm
     }
     stage('Build image') {
         app = docker.build("bart09/test")
     }
     stage ('Dependency-Check Analysis') {
            steps {
                sh '/var/lib/jenkins/dependency-check/bin/dependency-check.sh --scan `pwd` --format HTML --out /var/lib/jenkins/reports/dependency-check-report --prettyPrint'
         }
     }
     stage('SonarQube analysis') {
            withSonarQubeEnv('SonarQube-Server'){
                    sh "mvn sonar:sonar -Dsonar.projectKey=cccr-innogrid -Dsonar.host.url=http://192.168.56.101:9000 -Dsonar.login=sqp_89d07124730b6ee47afaaa9937ba9b3a865d0136 -Dsonar.sources=."
         }
     }
     stage('SonarQube Quality Gate'){
                timeout(time: 3, unit: 'MINUTES') {
                    script{
                        echo "Start~~~~"
                        def qg = waitForQualityGate()
                        echo "Status: ${qg.status}"
                        if(qg.status != 'OK') {
                            echo "NOT OK Status: ${qg.status}"
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        } else{
                            echo "OK Status: ${qg.status}"
                        }
                        echo "End~~~~"
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
