pipeline {
    environment {
        registryURL = "$URL"
        registry = "$imageName"
        registryCredentials = "$credentialsId"
        dockerImage = ''
        imageVersion = "1.0"

    }
    agent any

    stages {
	    stage('Checkout sources') {
            steps {
                echo "Downloading source code..."
                git branch: "master",
                    credentialsId: "$gitlabCredentials",
                    url: "$gitlabProjectURL"

            }

        }

        stage('Quality scan') {

            steps {
                echo "Running SonarQube quality scan..."
                withSonarQubeEnv("SonarQube") {
                    sh "${SONARSCANNER}/bin/sonar-scanner"
                }

                timeout(time: 5, unit: 'MINUTES') {
                waitForQualityGate abortPipeline: true
              }

            }

        }

        stage("Build image"){

            steps {
                script {
                    dockerImage = docker.build("$registry:$imageVersion")
                }
            }

        }

        stage('Test') {
            steps {
                sh '''
                echo Unit test inside container
                docker container run --rm $registry:$imageVersion -m unittest test/unit/example_test.py
                '''
            }
        }

        stage('Security scan') {
            steps {
                sh '''
                echo Run security test
                docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/root/.cache/ aquasec/trivy:0.18.3 $registry:$imageVersion
                '''
            }
        }

        stage('Push Image to registry') {
            steps {
                script {
                    docker.withRegistry(registryURL, registryCredentials ) {
                        dockerImage.push()
                    }

                }
            }
        }

        stage('Remove local image') {
            steps {
                sh "docker image rm $registry:$imageVersion"
            }
        }
    }

}
